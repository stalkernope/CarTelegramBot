// =========================
// CAR LEGENDS MINI APP
// =========================



let userId = null;


let tg = window.Telegram.WebApp;



// =========================
// TELEGRAM USER
// =========================


if(tg){


    tg.ready();


    tg.expand();



    if(

        tg.initDataUnsafe &&

        tg.initDataUnsafe.user

    ){


        userId = tg.initDataUnsafe.user.id;


    }


}



// Для теста через браузер

if(!userId){


    userId = 1;


}








// =========================
// START
// =========================


document.addEventListener(

    "DOMContentLoaded",

    ()=>{


        loadPlayer();


        setupButtons();


    }

);








// =========================
// LOAD PLAYER
// =========================


async function loadPlayer(){


    try{


        let response = await fetch(

            "/api/player/" + userId

        );



        let player = await response.json();



        updatePlayer(player);



    }


    catch(error){


        console.log(

            "PLAYER ERROR",

            error

        );


    }


}







// =========================
// UPDATE UI
// =========================


function updatePlayer(player){



    setText(

        "coins",

        player.coins

    );



    setText(

        "gems",

        player.gems

    );



    setText(

        "xp",

        player.xp

    );



    setText(

        "level",

        player.level

    );





    if(player.main_car){


        setText(

            "main-car",

            player.main_car

        );


        loadCar(

            player.main_car

        );


    }


}







function setText(id,value){



    let element = document.getElementById(

        id

    );



    if(element){


        element.innerText = value;


    }


}








// =========================
// CAR INFO
// =========================


async function loadCar(name){



    try{


        let response = await fetch(

            "/api/car/" + name

        );



        let car = await response.json();



        setText(

            "power",

            car.power || 0

        );


        setText(

            "speed",

            car.speed || 0

        );


        setText(

            "control",

            car.handling || 0

        );


    }

    catch(e){



    }


}








// =========================
// BUTTONS
// =========================


function setupButtons(){



    document

    .querySelectorAll(

        "button"

    )

    .forEach(

        button => {



            button.onclick = ()=>{


                let page =

                button.dataset.page;



                openPage(page);


            };


        }

    );


}








// =========================
// PAGES
// =========================


function openPage(page){



    if(page==="garage"){


        openGarage();


    }



    if(page==="race"){


        openRace();


    }



    if(page==="shop"){


        openShop();


    }



    if(page==="profile"){


        showMessage(

            "👤 Профиль"

        );


    }



    if(page==="tuning"){


        showMessage(

            "🔧 Тюнинг"

        );


    }



    if(page==="blacklist"){


        showMessage(

            "🏆 Blacklist"

        );


    }


}








// =========================
// GARAGE
// =========================


async function openGarage(){



    let response = await fetch(

        "/api/garage/" + userId

    );



    let cars = await response.json();



    let html = `


    <div class="main-car">


    <h1>

    🚗 ГАРАЖ

    </h1>


    `;



    cars.forEach(

        car=>{


            html += `


            <div>


            <h2>

            ${car.name}

            </h2>



            <p>

            ⚡ ${car.power}

            🚀 ${car.speed}

            </p>



            <button onclick="setMainCar('${car.name}')">

            👑 Выбрать

            </button>



            </div>


            `;


        }

    );



    html += `


    <button onclick="location.reload()">

    ⬅️ Назад

    </button>


    </div>


    `;



    document.querySelector(".game").innerHTML = html;


}








async function setMainCar(car){



    await fetch(

        "/api/car/main",

        {


            method:"POST",


            headers:{


                "Content-Type":

                "application/json"


            },


            body:JSON.stringify({


                user_id:userId,


                car:car


            })


        }

    );



    location.reload();


}








// =========================
// RACE
// =========================


function openRace(){



    document.querySelector(".game").innerHTML = `


    <div class="main-car">


    <h1>

    🏁 STREET RACE

    </h1>


    <button onclick="race()">

    START

    </button>



    <button onclick="location.reload()">

    ⬅️ Назад

    </button>



    </div>


    `;


}






async function race(){



    let response = await fetch(

        "/api/race/npc",

        {


            method:"POST",


            headers:{


                "Content-Type":

                "application/json"


            },


            body:JSON.stringify({


                user_id:userId,


                car:""


            })


        }

    );



    let data = await response.json();



    alert(

        data.text

    );


}








// =========================
// SHOP
// =========================


async function openShop(){



    let response = await fetch(

        "/api/shop"

    );



    let cars = await response.json();



    let html = `


    <div class="main-car">


    <h1>

    🛒 SHOP

    </h1>


    `;



    cars.forEach(

        car=>{


            html += `


            <h2>

            ${car.name}

            </h2>


            <p>

            💰 ${car.price}

            </p>


            `;


        }

    );



    html += `


    <button onclick="location.reload()">

    ⬅️ Назад

    </button>


    </div>


    `;



    document.querySelector(".game").innerHTML = html;


}








function showMessage(text){


    alert(text);


}