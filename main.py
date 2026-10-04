import os, json, random, re, logging, threading, asyncio
from datetime import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from zoneinfo import ZoneInfo

import httpx
from telegram import (Update, InlineKeyboardButton,
                      InlineKeyboardMarkup, InputMediaPhoto)
from telegram.ext import (Application, CommandHandler,
                          CallbackQueryHandler, ContextTypes)

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = os.environ["CHANNEL_ID"]
ADMIN_ID = int(os.environ.get("ADMIN_ID", "0"))
INSTAGRAM = os.environ.get("INSTAGRAM_URL", "https://instagram.com/")
HISTORY = "history.json"
POOL_FILE = "pool.json"
API = "https://en.wikipedia.org/w/api.php"
UA = {"User-Agent": "CarTelegramBot/1.0 (personal channel bot)"}
TZ = ZoneInfo("Europe/Moscow")

# ---------- отобранные эксклюзивы (приоритетный список) ----------
CARS = [
    "Bugatti Chiron", "Bugatti Veyron", "Bugatti Bolide", "Bugatti Divo",
    "Bugatti Centodieci", "Bugatti La Voiture Noire",
    "Pagani Huayra", "Pagani Zonda",
    "Koenigsegg Jesko", "Koenigsegg Agera", "Koenigsegg Regera", "Koenigsegg CCX",
    "Rimac Nevera",
    "Ferrari LaFerrari", "Ferrari F40", "Ferrari F50", "Ferrari Enzo Ferrari",
    "Ferrari SF90 Stradale", "Ferrari 250 GTO", "Ferrari 288 GTO",
    "Ferrari Daytona SP3",
    "McLaren P1", "McLaren F1", "McLaren Senna", "McLaren Speedtail",
    "Porsche 918 Spyder", "Porsche Carrera GT", "Porsche 959",
    "Lamborghini Aventador", "Lamborghini Revuelto", "Lamborghini Miura",
    "Lamborghini Countach", "Lamborghini Veneno",
    "Aston Martin Valkyrie", "Aston Martin One-77", "Aston Martin Vulcan",
    "Mercedes-AMG One", "Mercedes-Benz 300 SL", "Mercedes-Benz CLK GTR",
    "Ford GT40", "Jaguar XJ220", "Lotus Evija", "Lexus LFA",
    "W Motors Lykan HyperSport", "Zenvo ST1", "SSC Tuatara",
    "Hennessey Venom F5", "Czinger 21C", "Pininfarina Battista",
    "Maserati MC12", "Rolls-Royce Boat Tail", "Rolls-Royce Sweptail",
    "Bentley Mulliner Bacalar", "Gordon Murray Automotive T.50",
    "Dodge Viper",
]

# ---------- категории Википедии, из которых собирается большая база ----------
BIG_CATS = [
    "Category:Supercars", "Category:Hypercars",
    "Category:Sports cars", "Category:Grand tourers",
]
BRAND_CATS = [
    "Category:Ferrari vehicles", "Category:Lamborghini vehicles",
    "Category:Porsche vehicles", "Category:Bugatti vehicles",
    "Category:McLaren vehicles", "Category:Aston Martin vehicles",
    "Category:Maserati vehicles", "Category:Mercedes-AMG vehicles",
    "Category:Mercedes-Benz vehicles", "Category:Lotus vehicles",
    "Category:Jaguar vehicles", "Category:Bentley vehicles",
    "Category:Rolls-Royce vehicles", "Category:Lexus vehicles",
    "Category:BMW M vehicles", "Category:Audi vehicles",
    "Category:Alfa Romeo vehicles", "Category:Pagani vehicles",
    "Category:Koenigsegg vehicles", "Category:Concept cars",
    "Category:Muscle cars", "Category:Nissan vehicles",
    "Category:Toyota vehicles", "Category:Ford vehicles",
    "Category:Chevrolet vehicles", "Category:Dodge vehicles",
]
SKIP = re.compile(
    r"(^List of|^Category:|engine|season|championship|grand prix|trophy|"
    r"\bcup\b|\bseries\b|formula|motorsport|\bteam\b|\bcompany\b|"
    r"disambiguation|\bracing\b)", re.I)

POOL = []

FUN = [
    "🔥 Ты явно любишь, когда на тебя оборачиваются на светофоре.",
    "😎 Спокойный стиль, сильный характер — всё как у тебя.",
    "🚀 Скорость, адреналин и ни капли компромиссов — это про тебя.",
    "💎 Ты ценишь редкое и особенное, а не то, что у всех.",
    "🌆 Ночной город, пустая трасса и громкий звук — твоя стихия.",
    "🏁 Ты не едешь, а выбираешь, как приехать.",
    "✨ Тебе важно, чтобы машина была не просто транспортом, а историей.",
]


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
    json.dump(h[-3000:], open(HISTORY, "w", encoding="utf-8"), ensure_ascii=False)


def shorten(text, limit=650):
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    cut = text[:limit]
    i = cut.rfind(". ")
    return cut[:i + 1] if i > 200 else cut.rstrip() + "…"


def insta_kb():
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("📸 Мой Instagram", url=INSTAGRAM)]])


def again_kb():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🎲 Ещё раз", callback_data="again")],
        [InlineKeyboardButton("📸 Мой Instagram", url=INSTAGRAM)],
    ])


# ---------- большая база машин из категорий Википедии ----------
def load_pool():
    global POOL
    try:
        POOL = json.load(open(POOL_FILE, encoding="utf-8"))
    except Exception:
        POOL = []


async def api_members(c, cat, kind, limit_total):
    out = []
    params = {"action": "query", "format": "json", "list": "categorymembers",
              "cmtitle": cat, "cmtype": kind, "cmlimit": 500}
    if kind == "page":
        params["cmnamespace"] = 0
    while len(out) < limit_total:
        try:
            r = await c.get(API, params=params)
            j = r.json()
        except Exception as e:
            logging.warning("category error (%s): %s", cat, e)
            break
        out += [m["title"] for m in j.get("query", {}).get("categorymembers", [])]
        if "continue" in j:
            params.update(j["continue"])
        else:
            break
    return out


async def build_pool():
    global POOL
    titles = set()
    try:
        async with httpx.AsyncClient(headers=UA, timeout=30,
                                     follow_redirects=True) as c:
            for cat in BRAND_CATS + BIG_CATS:
                titles.update(await api_members(c, cat, "page", 2000))
            for cat in BIG_CATS:
                subs = await api_members(c, cat, "subcat", 60)
                for sub in subs[:60]:
                    titles.update(await api_members(c, sub, "page", 500))
    except Exception as e:
        logging.warning("build_pool error: %s", e)
    pool = sorted(t for t in titles if not SKIP.search(t))
    if pool:
        POOL = pool
        try:
            json.dump(pool, open(POOL_FILE, "w", encoding="utf-8"),
                      ensure_ascii=False)
        except Exception:
            pass
    logging.info("pool size: %d", len(POOL))


def candidates(used, n=12):
    base = CARS if (not POOL or random.random() < 0.4) else POOL
    pool = [t for t in base if t not in used] or base[:]
    random.shuffle(pool)
    return pool[:n]


async def get_car(en_title):
    """Фото (en.wikipedia) + русский текст (ru.wikipedia)."""
    try:
        async with httpx.AsyncClient(headers=UA, timeout=25,
                                     follow_redirects=True) as c:
            r = await c.get(API, params={
                "action": "query", "format": "json", "redirects": 1,
                "prop": "pageimages|langlinks", "piprop": "thumbnail",
                "pithumbsize": 1200, "lllang": "ru", "titles": en_title,
            })
            page = next(iter(r.json()["query"]["pages"].values()))
            thumb = page.get("thumbnail", {}).get("source")
            ll = page.get("langlinks")
            if not thumb or not ll:
                return None
            ru_title = ll[0]["*"]

            r2 = await c.get("https://ru.wikipedia.org/w/api.php", params={
                "action": "query", "format": "json", "redirects": 1,
                "prop": "extracts", "exintro": 1, "explaintext": 1,
                "titles": ru_title,
            })
            p2 = next(iter(r2.json()["query"]["pages"].values()))
            text = p2.get("extract", "").strip()
            if len(text) < 120:
                return None

            img = await c.get(thumb)
            if img.status_code != 200:
                return None
            return {"name": ru_title, "text": text, "photo": img.content}
    except Exception as e:
        logging.warning("get_car error (%s): %s", en_title, e)
        return None


async def pick_car():
    used = load_history()
    for t in candidates(used, 12):
        d = await get_car(t)
        if d:
            used.append(t)
            save_history(used)
            return d
    return None


# ---------- эксклюзив дня ----------
async def post_daily(bot, chat_id, notify=True):
    car = await pick_car()
    if not car:
        if notify:
            await bot.send_message(chat_id, "Не получилось найти машину, попробуй ещё раз 🙏")
        return False
    caption = ("🏎 Эксклюзив дня: " + car["name"] + "\n\n"
               + shorten(car["text"], 700)
               + "\n\n❓ А тебе бы такая понравилась? Пиши в комментариях 👇"
               + "\n📷 Wikipedia")
    await bot.send_photo(chat_id, car["photo"], caption=caption[:1020],
                         reply_markup=insta_kb())
    return True


# ---------- голосование ----------
async def post_battle(bot, chat_id, notify=True):
    titles = random.sample(CARS, 3)
    if POOL:
        titles += random.sample(POOL, min(9, len(POOL)))
    random.shuffle(titles)
    cars, seen = [], set()
    for t in titles:
        d = await get_car(t)
        if d and d["name"] not in seen:
            seen.add(d["name"])
            cars.append((d["name"][:90], d["photo"]))
        if len(cars) == 4:
            break
    if len(cars) < 2:
        if notify:
            await bot.send_message(chat_id, "Не получилось собрать голосование 🙏")
        return False
    nums = ["1️⃣", "2️⃣", "3️⃣", "4️⃣"]
    media = [InputMediaPhoto(p, caption=f"{nums[i]} {n}")
             for i, (n, p) in enumerate(cars)]
    await bot.send_media_group(chat_id, media)
    await bot.send_poll(chat_id, "Какая машина лучше? 🔥",
                        options=[n for n, _ in cars], is_anonymous=True)
    return True


# ---------- какая машина тебе подходит ----------
async def send_match(bot, chat_id):
    await bot.send_chat_action(chat_id, "upload_photo")
    for t in candidates([], 10):
        d = await get_car(t)
        if d:
            cap = ("🎯 Твоя машина: " + d["name"] + "\n\n"
                   + random.choice(FUN) + "\n\n" + shorten(d["text"], 350))
            await bot.send_photo(chat_id, d["photo"], caption=cap[:1000],
                                 reply_markup=again_kb())
            return
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
    ok = await post_daily(ctx.bot, CHANNEL, notify=False)
    await update.message.reply_text(
        "✅ Пост в канале" if ok else "❌ Не вышло, смотри логи")


async def admin_vote(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    ok = await post_battle(ctx.bot, CHANNEL, notify=False)
    await update.message.reply_text(
        "✅ Голосование в канале" if ok else "❌ Не вышло, смотри логи")


async def admin_stats(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    await update.message.reply_text(
        f"📊 В базе: {len(POOL)} машин из Википедии + {len(CARS)} отобранных "
        f"эксклюзивов.\nПоказано уже: {len(load_history())}")


async def on_button(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    if q.data == "again":
        await send_match(ctx.bot, q.message.chat_id)


async def job_daily(ctx: ContextTypes.DEFAULT_TYPE):
    await post_daily(ctx.bot, CHANNEL, notify=False)


async def job_battle(ctx: ContextTypes.DEFAULT_TYPE):
    await post_battle(ctx.bot, CHANNEL, notify=False)


async def post_init(app):
    await app.bot.set_my_commands([
        ("start", "Меню"),
        ("match", "Какая машина мне подходит"),
        ("car", "Эксклюзивная машина"),
    ])
    asyncio.create_task(build_pool())


def main():
    load_pool()
    app = Application.builder().token(TOKEN).post_init(post_init).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("match", match))
    app.add_handler(CommandHandler("car", car))
    app.add_handler(CommandHandler("post", admin_post))
    app.add_handler(CommandHandler("vote", admin_vote))
    app.add_handler(CommandHandler("stats", admin_stats))
    app.add_handler(CallbackQueryHandler(on_button))
    app.job_queue.run_daily(job_daily, time(12, 0, tzinfo=TZ))
    app.job_queue.run_daily(job_battle, time(19, 0, tzinfo=TZ))
    print("🚘 Car Telegram Bot запущен!")
    keep_alive()
    app.run_polling()


if __name__ == "__main__":
    main()
