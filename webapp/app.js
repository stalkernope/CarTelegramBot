// =========================
// CAR LEGENDS MINI APP
// =========================


let userId = 1;



// =========================
// ЗАПУСК
// =========================


document.addEventListener(

    "DOMContentLoaded",

    () => {

        loadPlayer();

        setupButtons();

    }

);





// =========================
// ЗАГРУЗКА ИГРОКА
// =========================


async function loadPlayer(){


    try {


        let response = await fetch(

            `/api/player/${userId}`

        );


        let player = await response.json();



        updatePlayer(player);



    }


    catch(error){


        console.log(

            "Ошибка загрузки игрока",

            error

        );


    }


}






// =========================
// ОТОБРАЖЕНИЕ
// =========================


function updatePlayer(player){



    let block = document.querySelector(

        ".player"

    );



    if(block){


        block.innerHTML =

        `

        👤 Игрок<br>

        ⭐ Level ${player.level}<br>

        🔥 XP ${player.xp}<br>

        💰 ${player.coins}<br>

        💎 ${player.gems}

        `;


    }





    let car = document.querySelector(

        ".car h2"

    );



    if(

        car && player.main_car

    ){


        car.innerHTML =

        player.main_car;


    }



}







// =========================
// КНОПКИ
// =========================


function setupButtons(){



    let buttons = document.querySelectorAll(

        "button"

    );



    buttons.forEach(

        button => {


            button.onclick = () => {


                let text = button.innerText;



                openScreen(text);


            }


        }

    );



}






// =========================
// ПЕРЕХОДЫ
// =========================


function openScreen(action){



    if(action.includes("GARAGE")){


        alert(

            "🚗 Гараж"

        );


    }


    else if(action.includes("RACE")){


        alert(

            "🏁 Гонка"

        );


    }


    else if(action.includes("SHOP")){


        alert(

            "🛒 Магазин"

        );


    }


    else if(action.includes("TUNING")){


        alert(

            "🔧 Тюнинг"

        );


    }


    else if(action.includes("PROFILE")){


        alert(

            "👤 Профиль"

        );


    }



}