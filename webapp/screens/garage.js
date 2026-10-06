// =========================
// CAR LEGENDS GARAGE
// =========================


async function openGarage(){


    try {


        const response = await fetch(

            "/api/garage/" + userId

        );


        const cars = await response.json();



        renderGarage(cars);



    }

    catch(error){


        console.log(

            "Ошибка гаража",

            error

        );


    }


}





// =========================
// ОТОБРАЖЕНИЕ ГАРАЖА
// =========================


function renderGarage(cars){


    const game = document.querySelector(

        ".game"

    );



    let html = `


    <div class="garage-page">


        <h1>

        🚗 МОЙ ГАРАЖ

        </h1>



    `;




    if(

        cars.length === 0

    ){


        html += `


        <div class="empty">


        Гараж пуст


        <br><br>


        Отправляйся в магазин


        </div>


        `;


    }



    else {



        cars.forEach(

            car => {


                html += `


                <div class="garage-car">


                    <div class="garage-image">

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



                    <button onclick="selectCar('${car.name}')">


                    👑 Сделать главной


                    </button>



                </div>


                `;


            }

        );


    }




    html += `


        <button onclick="backHome()">


        ⬅️ Назад


        </button>



    </div>


    `;



    game.innerHTML = html;


}





// =========================
// ВЫБОР МАШИНЫ
// =========================


function selectCar(name){


    alert(

        "👑 Главная машина: " + name

    );


}





// =========================
// НАЗАД
// =========================


function backHome(){


    location.reload();


}