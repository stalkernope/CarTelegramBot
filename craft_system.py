import json
import os



CRAFT_FILE = "craft.json"




# =========================
# РЕЦЕПТЫ
# =========================


RECIPES = [

    {

        "id": "street_beast",

        "name": "🔥 Street Beast",

        "need":

        {

            "engine": 3,

            "turbo": 2,

            "carbon": 1

        },


        "result":

        "Street Beast X"

    },


    {

        "id": "legend_project",

        "name": "👑 Legend Project",

        "need":

        {

            "engine": 5,

            "turbo": 5,

            "carbon": 5

        },


        "result":

        "Legend X1"

    }

]




# =========================
# МАТЕРИАЛЫ
# =========================


DEFAULT_ITEMS = {

    "engine": 0,

    "turbo": 0,

    "carbon": 0,

    "metal": 0

}




# =========================
# ЗАГРУЗКА
# =========================


def load_craft():

    if not os.path.exists(CRAFT_FILE):

        return {}



    try:

        with open(

            CRAFT_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_craft(data):

    with open(

        CRAFT_FILE,

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            data,

            file,

            ensure_ascii=False,

            indent=4

        )




# =========================
# ИНВЕНТАРЬ
# =========================


def get_materials(user_id):

    data = load_craft()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "materials":

            DEFAULT_ITEMS.copy(),


            "projects":

            []

        }


        save_craft(data)



    return data[uid]




# =========================
# ДОБАВИТЬ МАТЕРИАЛ
# =========================


def add_material(

    user_id,

    material,

    amount

):

    data = load_craft()


    player = get_materials(

        user_id

    )


    if material not in player["materials"]:

        return False



    player["materials"][material] += amount



    data[str(user_id)] = player


    save_craft(data)



    return True




# =========================
# ПРОВЕРКА РЕЦЕПТА
# =========================


def can_craft(

    user_id,

    recipe_id

):

    player = get_materials(

        user_id

    )



    recipe = None



    for item in RECIPES:


        if item["id"] == recipe_id:

            recipe = item



    if not recipe:

        return False



    for material, amount in recipe["need"].items():


        if player["materials"].get(

            material,

            0

        ) < amount:

            return False



    return True




# =========================
# СОЗДАНИЕ МАШИНЫ
# =========================


def craft_car(

    user_id,

    recipe_id

):

    data = load_craft()


    player = get_materials(

        user_id

    )



    recipe = None



    for item in RECIPES:


        if item["id"] == recipe_id:

            recipe = item



    if not recipe:

        return {

            "success":

            False,

            "message":

            "❌ Рецепт не найден"

        }




    if not can_craft(

        user_id,

        recipe_id

    ):

        return {

            "success":

            False,

            "message":

            "❌ Недостаточно деталей"

        }




    for material, amount in recipe["need"].items():


        player["materials"][material] -= amount




    player["projects"].append(

        recipe["result"]

    )



    data[str(user_id)] = player



    save_craft(data)



    return {

        "success":

        True,

        "car":

        recipe["result"]

    }




# =========================
# ТЕКСТ
# =========================


def craft_text(user_id):

    player = get_materials(

        user_id

    )


    text = (

        "🔨 <b>CAR WORKSHOP</b>\n\n"

    )



    text += "📦 Детали:\n"



    for item, count in player["materials"].items():


        text += (

            f"{item}: {count}\n"

        )



    text += "\n🚗 Проекты:\n"



    for car in player["projects"]:


        text += (

            f"🔥 {car}\n"

        )



    return text