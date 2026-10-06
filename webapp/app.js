// =========================
// CAR LEGENDS MINI APP
// =========================


// временный ID игрока
// позже заменим на Telegram ID

let userId = 1;




// =========================
// ЗАПУСК
// =========================


document.addEventListener(

    "DOMContentLoaded",

    function(){

        loadPlayer();

        setupButtons();

    }

);





// =========================
// ЗАГРУЗКА ИГРОКА
// =========================


async function loadPlayer(){


    try {


        const response = await fetch(

            "/api/player/" + userId

        );


        const player = await response.json();


        updatePlayer(player);



    }


    catch(error){


        console.log(

            "API пока недоступен"

        );


    }


}






// =========================
// ОБНОВЛЕНИЕ ЭКРАНА
// =========================


function updatePlayer(player){



    const coins = document.getElementById(

        "coins"

    );


    const gems = document.getElementById(

        "gems"

    );


    const rep = document.getElementById(

        "rep"

    );



    if(coins){

        coins.innerText = player.coins;

    }



    if(gems){

        gems.innerText = player.gems;

    }



    if(rep){

        rep.innerText = player.xp;

    }




    const car = document.getElementById(

        "car-name"

    );



    if(

        car && player.main_car

    ){


        car.innerText = player.main_car;


    }



}






// =========================
// КНОПКИ
// =========================


function setupButtons(){



    const buttons = document.querySelectorAll(

        "button"

    );



    buttons.forEach(

        button => {



            button.addEventListener(

                "click",

                function(){


                    openMenu(

                        button.innerText

                    );


                }

            );


        }

    );


}






// =========================
// МЕНЮ
// =========================


function openMenu(name){



    if(

        name.includes("RACE")

    ){


        showMessage(

            "🏁 Поиск гонки..."

        );


    }



    else if(

        name.includes("GARAGE")

    ){


        showMessage(

            "🚗 Открываем гараж..."

        );


    }



    else if(

        name.includes("TUNING")

    ){


        showMessage(

            "🔧 Тюнинг..."

        );


    }



    else if(

        name.includes("BLACKLIST")

    ){


        showMessage(

            "🏆 Blacklist..."

        );


    }



    else if(

        name.includes("SHOP")

    ){


        showMessage(

            "🛒 Автосалон..."

        );


    }



    else if(

        name.includes("PROFILE")

    ){


        showMessage(

            "👤 Профиль..."

        );


    }


}






// =========================
// УВЕДОМЛЕНИЕ
// =========================


function showMessage(text){


    alert(text);


}