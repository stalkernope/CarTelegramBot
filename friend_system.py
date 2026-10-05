import json
import os
import time



FRIEND_FILE = "friends.json"




# =========================
# ЗАГРУЗКА
# =========================


def load_friends():

    if not os.path.exists(FRIEND_FILE):

        return {}



    try:

        with open(

            FRIEND_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    except:

        return {}




# =========================
# СОХРАНЕНИЕ
# =========================


def save_friends(data):

    with open(

        FRIEND_FILE,

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
# ПРОФИЛЬ ДРУЗЕЙ
# =========================


def get_friend_profile(user_id):

    data = load_friends()


    uid = str(user_id)



    if uid not in data:


        data[uid] = {

            "friends": [],

            "requests": [],

            "gifts": 0

        }


        save_friends(data)



    return data[uid]




# =========================
# ОТПРАВИТЬ ЗАЯВКУ
# =========================


def send_friend_request(

    user_id,

    target_id

):

    data = load_friends()


    target = get_friend_profile(

        target_id

    )



    if user_id in target["requests"]:

        return False



    if user_id == target_id:

        return False



    target["requests"].append(

        user_id

    )



    data[str(target_id)] = target


    save_friends(data)



    return True




# =========================
# ПРИНЯТЬ ДРУГА
# =========================


def accept_friend(

    user_id,

    friend_id

):

    data = load_friends()


    user = get_friend_profile(

        user_id

    )


    friend = get_friend_profile(

        friend_id

    )



    if friend_id not in user["requests"]:

        return False



    user["requests"].remove(

        friend_id

    )



    if friend_id not in user["friends"]:

        user["friends"].append(

            friend_id

        )



    if user_id not in friend["friends"]:

        friend["friends"].append(

            user_id

        )



    data[str(user_id)] = user

    data[str(friend_id)] = friend



    save_friends(data)



    return True




# =========================
# УДАЛИТЬ ДРУГА
# =========================


def remove_friend(

    user_id,

    friend_id

):

    data = load_friends()


    user = get_friend_profile(

        user_id

    )



    if friend_id in user["friends"]:

        user["friends"].remove(

            friend_id

        )


    data[str(user_id)] = user


    save_friends(data)



    return True




# =========================
# ПОДАРОК
# =========================


def send_gift(

    user_id,

    friend_id

):

    data = load_friends()


    friend = get_friend_profile(

        friend_id

    )


    user = get_friend_profile(

        user_id

    )



    if friend_id not in user["friends"]:

        return False



    friend["gifts"] += 1



    data[str(friend_id)] = friend


    save_friends(data)



    return True




# =========================
# СПИСОК ДРУЗЕЙ
# =========================


def friends_list(user_id):

    profile = get_friend_profile(

        user_id

    )


    return profile["friends"]




# =========================
# ТЕКСТ
# =========================


def friends_text(user_id):

    profile = get_friend_profile(

        user_id

    )


    text = (

        "👥 <b>ДРУЗЬЯ</b>\n\n"

    )


    text += (

        f"👤 Друзей: "

        f"{len(profile['friends'])}\n"

    )


    text += (

        f"🎁 Получено подарков: "

        f"{profile['gifts']}\n\n"

    )



    if profile["friends"]:


        for friend in profile["friends"]:

            text += (

                f"🟢 Игрок {friend}\n"

            )

    else:

        text += "Друзей пока нет"



    return text