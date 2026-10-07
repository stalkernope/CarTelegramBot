// =========================
// CAR LEGENDS MINI APP FINAL
// =========================


let tg = window.Telegram.WebApp;


let userId = 1;


let player = {};





// =========================
// TELEGRAM
// =========================


if (tg) {

    tg.ready();

    tg.expand();


    if (
        tg.initDataUnsafe &&
        tg.initDataUnsafe.user
    ) {

        userId =
        tg.initDataUnsafe.user.id;

    }

}





// =========================
// START
// =========================


document.addEventListener(
    "DOMContentLoaded",
    ()=>{


        setupNavigation();


        loadPlayer();


        setupActions();


    }
);







// =========================
// PLAYER LOAD
// =========================


async function loadPlayer(){


    try{


        let res = await fetch(

            `/api/player/${userId}`

        );


        player = await res.json();



        updatePlayer();



        if(player.main_car){

            loadCar(
                player.main_car
            );

        }



    }

    catch(e){

        console.log(
            "PLAYER ERROR",
            e
        );

    }


}







// =========================
// UPDATE PLAYER UI
// =========================


function updatePlayer(){


    text(
        "username",
        player.username || "PLAYER"
    );


    text(
        "coins",
        player.coins || 0
    );


    text(
        "gems",
        player.gems || 0
    );


    text(
        "rep",
        player.rep || 0
    );


    text(
        "level",
        player.level || 1
    );


    text(
        "wins",
        player.wins || 0
    );


    text(
        "losses",
        player.losses || 0
    );


    text(
        "cars-count",
        player.garage?.length || 0
    );


    text(
        "pets-count",
        player.pets?.length || 0
    );


}







function text(id,value){


    let el =
    document.getElementById(id);


    if(el){

        el.innerText = value;

    }

}









// =========================
// CAR
// =========================


async function loadCar(name){


    try{


        let res =
        await fetch(
            `/api/car/${name}`
        );


        let car =
        await res.json();



        text(
            "main-car",
            car.name
        );


        text(
            "power",
            car.power || 0
        );


        text(
            "speed",
            car.speed || 0
        );


        text(
            "control",
            car.handling || 0
        );



        if(car.image){


            document
            .getElementById(
                "car-image"
            )
            .src = car.image;


        }



    }

    catch(e){}



}









// =========================
// NAVIGATION
// =========================


function setupNavigation(){


    document
    .querySelectorAll(
        "[data-page]"
    )
    .forEach(btn=>{


        btn.onclick=()=>{


            openPage(
                btn.dataset.page
            );


        };


    });


}







function openPage(page){


    document
    .querySelectorAll(
        ".page"
    )
    .forEach(p=>{


        p.classList.remove(
            "active"
        );


    });



    let target =
    document.getElementById(
        page+"-page"
    );



    if(target){


        target.classList.add(
            "active"
        );


    }



    if(page==="garage"){

        loadGarage();

    }



    if(page==="shop"){

        loadShop();

    }



}








// =========================
// GARAGE
// =========================


async function loadGarage(){


    let box =
    document.getElementById(
        "garage-list"
    );


    box.innerHTML="";



    let res =
    await fetch(
        `/api/garage/${userId}`
    );


    let cars =
    await res.json();




    cars.forEach(car=>{


        box.innerHTML += `


        <div class="car-card">


            <h3>
            ${car.name}
            </h3>


            <p>
            ⚡ ${car.power}
            </p>


            <p>
            🚀 ${car.speed}
            </p>



            <button onclick="
            setMainCar('${car.name}')
            ">

            👑 Сделать главной

            </button>


        </div>


        `;


    });


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



    loadPlayer();


    openPage(
        "home"
    );


}









// =========================
// SHOP
// =========================


async function loadShop(){


    let box =
    document.getElementById(
        "shop-list"
    );


    box.innerHTML="";



    let res =
    await fetch(
        "/api/shop"
    );


    let cars =
    await res.json();



    cars.forEach(car=>{


        box.innerHTML += `


        <div class="car-card">


        <h3>
        ${car.name}
        </h3>


        <p>
        💰 ${car.price}
        </p>


        <p>
        ⚡ ${car.power}
        </p>



        <button onclick="
        buyCar('${car.name}')
        ">

        Купить

        </button>


        </div>


        `;


    });


}








async function buyCar(car){


    let res =
    await fetch(

        "/api/shop/buy",

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



    let data =
    await res.json();



    alert(

        data.success
        ?
        "✅ Машина куплена"
        :
        "❌ "+data.error

    );


    loadPlayer();


}








// =========================
// RACE
// =========================


function setupActions(){


    let npc =
    document.getElementById(
        "npc-race"
    );


    if(npc){


        npc.onclick =
        ()=>race(
            "npc"
        );


    }



    let boss =
    document.getElementById(
        "boss-race"
    );


    if(boss){


        boss.onclick =
        ()=>race(
            "boss"
        );


    }


}







async function race(type){


    let url =
    type==="boss"
    ?
    "/api/race/boss"
    :
    "/api/race/npc";



    let body = {


        user_id:userId,


        car:
        player.main_car


    };



    if(type==="boss"){


        body.boss = 1;


    }



    let res =
    await fetch(

        url,

        {


            method:"POST",


            headers:{


            "Content-Type":
            "application/json"


            },


            body:
            JSON.stringify(body)


        }

    );



    let data =
    await res.json();



    document
    .getElementById(
        "race-result"
    )
    .innerHTML = data.text;


    loadPlayer();


}