// =========================
// CAR LEGENDS APP
// =========================


// данные игрока
let player = {

    name: "ShadowRacer",

    level: 18,

    rep: 2450,

    coins: 125000,

    gems: 50,


    main_car: {

        name: "BMW M3 GTR",

        power: 8500,

        speed: 320,

        rarity: "LEGENDARY"

    }

};




// =========================
// ЗАГРУЗКА
// =========================


document.addEventListener(

    "DOMContentLoaded",

    () => {


        loadPlayer();


        setupButtons();


    }

);





// =========================
// ИГРОК
// =========================


function loadPlayer(){


    console.log(

        "CAR LEGENDS loaded"

    );


    updateScreen();


}





function updateScreen(){


    let name =
    document.querySelector(
        ".player"
    );


    if(name){


        name.innerHTML =

        `
        👤 ${player.name}<br>
        ⭐ Level ${player.level}<br>
        🔥 REP ${player.rep}
        `;


    }


}





// =========================
// КНОПКИ
// =========================


function setupButtons(){


    let buttons =

    document.querySelectorAll(

        "button"

    );



    buttons.forEach(

        button => {


            button.onclick = () => {


                let action =

                button.innerText;



                openScreen(

                    action

                );


            }


        }

    );


}






// =========================
// ЭКРАНЫ
// =========================


function openScreen(action){



    if(

        action.includes("RACE")

    ){


        alert(

            "🏁 Поиск гонки..."

        );


    }



    else if(

        action.includes("GARAGE")

    ){


        alert(

            "🚗 Открываем гараж"

        );


    }



    else if(

        action.includes("TUNING")

    ){


        alert(

            "🔧 Мастерская"

        );


    }



    else if(

        action.includes("BLACKLIST")

    ){


        alert(

            "🏆 Blacklist"

        );


    }



    else if(

        action.includes("SHOP")

    ){


        alert(

            "🛒 Автосалон"

        );


    }



    else if(

        action.includes("PROFILE")

    ){


        alert(

            "👤 Профиль"

        );


    }


}