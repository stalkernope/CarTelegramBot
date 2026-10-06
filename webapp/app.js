// =========================
// CAR LEGENDS MINI APP
// =========================


// ID игрока
let userId = 1;




// =========================
// START
// =========================


document.addEventListener(

    "DOMContentLoaded",

    function(){

        loadPlayer();

        setupButtons();

    }

);






// =========================
// ИГРОК
// =========================


async function loadPlayer(){


    try{


        const response = await fetch(

            "/api/player/" + userId

        );


        const player = await response.json();



        updatePlayer(player);



    }

    catch(error){


        console.log(

            "Player error",

            error

        );


    }


}





function updatePlayer(player){



    if(

        document.getElementById("coins")

    ){

        document.getElementById("coins").innerText =

        player.coins;


    }



    if(

        document.getElementById("gems")

    ){

        document.getElementById("gems").innerText =

        player.gems;


    }



    if(

        document.getElementById("rep")

    ){

        document.getElementById("rep").innerText =

        player.xp;


    }



    if(

        document.getElementById("car-name")

        &&

        player.main_car

    ){


        document.getElementById("car-name").innerText =

        player.main_car;


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



            button.onclick = function(){


                openMenu(

                    button.innerText

                );


            };


        }

    );


}






// =========================
// МЕНЮ
// =========================


function openMenu(name){



    if(

        name.includes("GARAGE")

    ){


        openGarage();


    }



    else if(

        name.includes("RACE")

    ){


        alert(

            "🏁 Скоро гонки"

        );


    }



    else if(

        name.includes("TUNING")

    ){


        alert(

            "🔧 Скоро тюнинг"

        );


    }



    else if(

        name.includes("BLACKLIST")

    ){


        alert(

            "🏆 Blacklist"

        );


    }



    else if(

        name.includes("SHOP")

    ){


        alert(

            "🛒 Магазин"

        );


    }



    else if(

        name.includes("PROFILE")

    ){


        alert(

            "👤 Профиль"

        );


    }


}






// =========================
// ГАРАЖ
// =========================


async function openGarage(){



    try{


        const response = await fetch(

            "/api/garage/" + userId

        );



        const cars = await response.json();



        renderGarage(cars);



    }


    catch(error){


        alert(

            "Ошибка гаража"

        );


    }


}






function renderGarage(cars){



    const game = document.querySelector(

        ".game"

    );



    let html = `


    <header class="top">

        <div class="logo">

        🚗 GARAGE

        </div>


    </header>



    <div class="garage-list">


    `;



    if(

        cars.length === 0

    ){


        html += `


        <h2>

        Гараж пуст

        </h2>


        `;


    }



    else{


        cars.forEach(

            car => {


                html += `


                <div class="garage-item">


                    <div class="car-glow">

                    🏎

                    </div>


                    <h2>

                    ${car.name}

                    </h2>


                    <p>

                    💎 ${car.rarity || "Common"}

                    </p>


                    <p>

                    ⚡ ${car.power || 0}

                    |

                    🚀 ${car.speed || 0}

                    </p>



                </div>


                `;


            }

        );


    }




    html += `


    <button onclick="location.reload()">

    ⬅️ Назад

    </button>



    </div>


    `;



    game.innerHTML = html;


}