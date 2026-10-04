import os, json, random, re, logging, threading
from datetime import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from zoneinfo import ZoneInfo

import httpx
from anthropic import AsyncAnthropic
from telegram import (Update, InlineKeyboardButton,
                      InlineKeyboardMarkup, InputMediaPhoto)
from telegram.ext import (Application, CommandHandler,
                          CallbackQueryHandler, ContextTypes)

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = os.environ["CHANNEL_ID"]
ADMIN_ID = int(os.environ.get("ADMIN_ID", "0"))
INSTAGRAM = os.environ.get("INSTAGRAM_URL", "https://instagram.com/")
MODEL = "claude-haiku-4-5-20251001"
HISTORY = "history.json"
UA = {"User-Agent": "CarTelegramBot/1.0 (personal channel bot)"}
TZ = ZoneInfo("Europe/Moscow")

ai = AsyncAnthropic()


# ---------- keep-alive сервер для Render Free ----------
class Ping(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ok")

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def log_message(self, *a):
        pass


def keep_alive():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Ping)
    threading.Thread(target=server.serve_forever, daemon=True).start()


# ---------- helpers ----------
def load_history():
    try:
        return json.load(open(HISTORY, encoding="utf-8"))
    except Exception:
        return []


def save_history(h):
    json.dump(h[-200:], open(HISTORY, "w", encoding="utf-8"), ensure_ascii=False)


async def ask(prompt, max_tokens=800):
    r = await ai.messages.create(
        model=MODEL, max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}])
    return r.content[0].text.strip()


def parse_json(t):
    t = re.sub(r"^```(?:json)?|```$", "", t.strip(), flags=re.M).strip()
    return json.loads(t)


async def wiki(title):
    """Фото + факты из Википедии."""
    params = {
        "action": "query", "format": "json", "redirects": 1,
        "prop": "pageimages|extracts", "piprop": "thumbnail",
        "pithumbsize": 1200, "exintro": 1, "explaintext": 1,
        "titles": title,
    }
    try:
        async with httpx.AsyncClient(headers=UA, timeout=25,
                                     follow_redirects=True) as c:
            r = await c.get("https://en.wikipedia.org/w/api.php", params=params)
            page = next(iter(r.json()["query"]["pages"].values()))
            thumb = page.get("thumbnail", {}).get("source")
            if not thumb:
                return None
            img = await c.get(thumb)
            if img.status_code != 200:
                return None
            return {"title": page.get("title", title),
                    "extract": page.get("extract", "")[:1500],
                    "photo": img.content}
    except Exception as e:
        logging.warning("wiki error: %s", e)
        return None


def insta_kb():
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("📸 Мой Instagram", url=INSTAGRAM)]])


def again_kb():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🎲 Ещё раз", callback_data="again")],
        [InlineKeyboardButton("📸 Мой Instagram", url=INSTAGRAM)],
    ])


# ---------- эксклюзив дня ----------
async def find_car():
    used = load_history()
    for _ in range(5):
        try:
            d = parse_json(await ask(
                "Назови одну по-настоящему эксклюзивную или редкую машину мира "
                "(гиперкар, лимитированная серия, раритет, концепт). Не повторяй: "
                + ", ".join(used[-80:]) +
                '. Верни ТОЛЬКО JSON: {"name": "...", "wiki_title": '
                '"точное название статьи в английской Википедии"}', 200))
            w = await wiki(d["wiki_title"])
            if w:
                used.append(d["name"])
                save_history(used)
                return {"name": d["name"], **w}
        except Exception as e:
            logging.warning("find_car: %s", e)
    return None


async def write_post(name, extract):
    return await ask(
        "Ты ведёшь красивый телеграм-канал про машины. Напиши пост на русском "
        "про «" + name + "» строго по фактам ниже. Формат: яркий заголовок с "
        "эмодзи, 3-4 коротких пункта (история, мотор и характеристики, чем "
        "уникальна), в конце вопрос подписчикам. Ничего не выдумывай. "
        "До 700 символов, без markdown.\n\nФакты:\n" + extract, 700)


async def post_daily(bot, chat_id):
    car = await find_car()
    if not car:
        await bot.send_message(chat_id, "Не получилось найти машину, попробуй ещё раз 🙏")
        return
    text = await write_post(car["name"], car["extract"])
    await bot.send_photo(chat_id, car["photo"],
                         caption=text[:950] + "\n\n📷 Wikipedia",
                         reply_markup=insta_kb())


# ---------- голосование ----------
async def post_battle(bot, chat_id):
    cars = []
    for _ in range(3):
        try:
            data = parse_json(await ask(
                "Назови 4 разные красивые машины разных стран и эпох для "
                "голосования «какая лучше». Верни ТОЛЬКО JSON-список из 4 "
                'объектов {"name": "...", "wiki_title": "название статьи в '
                'английской Википедии"}', 500))
            cars = []
            for d in data:
                w = await wiki(d["wiki_title"])
                if w:
                    cars.append((d["name"][:90], w["photo"]))
            if len(cars) >= 2:
                break
        except Exception as e:
            logging.warning("battle: %s", e)
    if len(cars) < 2:
        await bot.send_message(chat_id, "Не получилось собрать голосование 🙏")
        return
    nums = ["1️⃣", "2️⃣", "3️⃣", "4️⃣"]
    media = [InputMediaPhoto(p, caption=f"{nums[i]} {n}")
             for i, (n, p) in enumerate(cars)]
    await bot.send_media_group(chat_id, media)
    await bot.send_poll(chat_id, "Какая машина лучше? 🔥",
                        options=[n for n, _ in cars], is_anonymous=True)


# ---------- какая машина тебе подходит ----------
VIBES = ["спокойный интроверт", "душа компании", "любитель скорости",
         "ценитель классики", "будущий миллионер", "романтик",
         "путешественник", "эстет"]


async def send_match(bot, chat_id):
    await bot.send_chat_action(chat_id, "upload_photo")
    for _ in range(4):
        try:
            d = parse_json(await ask(
                "Выбери случайную красивую машину (любая эпоха и страна) и "
                "придумай весёлый результат викторины «Какая машина тебе "
                "подходит» для человека с характером: " + random.choice(VIBES) +
                '. Верни ТОЛЬКО JSON: {"name": "...", "wiki_title": "...", '
                '"text": "3-4 предложения на русском с эмодзи, почему она '
                'подходит, без markdown"}', 500))
            w = await wiki(d["wiki_title"])
            if w:
                cap = "🎯 Твоя машина: " + d["name"] + "\n\n" + d["text"]
                await bot.send_photo(chat_id, w["photo"], caption=cap[:1000],
                                     reply_markup=again_kb())
                return
        except Exception as e:
            logging.warning("match: %s", e)
    await bot.send_message(chat_id, "Не получилось, жми ещё раз 🙏")


# ---------- команды ----------
async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚘 <b>Привет! Я автобот про самые красивые машины мира.</b>\n\n"
        "🎲 /match — какая машина тебе подходит\n"
        "🏎 /car — эксклюзивная машина прямо сейчас\n\n"
        "А в канале каждый день: эксклюзив дня и битва машин 🔥",
        parse_mode="HTML", reply_markup=insta_kb())


async def match(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await send_match(ctx.bot, update.effective_chat.id)


async def car(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await ctx.bot.send_chat_action(update.effective_chat.id, "upload_photo")
    await post_daily(ctx.bot, update.effective_chat.id)


async def admin_post(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    await post_daily(ctx.bot, CHANNEL)
    await update.message.reply_text("✅ Пост в канале")


async def admin_vote(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    await post_battle(ctx.bot, CHANNEL)
    await update.message.reply_text("✅ Голосование в канале")


async def on_button(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    if q.data == "again":
        await send_match(ctx.bot, q.message.chat_id)


async def job_daily(ctx: ContextTypes.DEFAULT_TYPE):
    await post_daily(ctx.bot, CHANNEL)


async def job_battle(ctx: ContextTypes.DEFAULT_TYPE):
    await post_battle(ctx.bot, CHANNEL)


async def post_init(app):
    await app.bot.set_my_commands([
        ("start", "Меню"),
        ("match", "Какая машина мне подходит"),
        ("car", "Эксклюзивная машина"),
    ])


def main():
    app = Application.builder().token(TOKEN).post_init(post_init).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("match", match))
    app.add_handler(CommandHandler("car", car))
    app.add_handler(CommandHandler("post", admin_post))
    app.add_handler(CommandHandler("vote", admin_vote))
    app.add_handler(CallbackQueryHandler(on_button))
    app.job_queue.run_daily(job_daily, time(12, 0, tzinfo=TZ))
    app.job_queue.run_daily(job_battle, time(19, 0, tzinfo=TZ))
    print("🚘 Car Telegram Bot запущен!")
    keep_alive()
    app.run_polling()


if __name__ == "__main__":
    main()