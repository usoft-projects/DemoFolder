
function init(){
    var config = {
      apiKey: "AIzaSyDaldjIsm93aZluwjMnLzJ8Kxoeur_qayk",
      authDomain: "moloko-01.firebaseapp.com",
      databaseURL: "https://moloko-01-default-rtdb.firebaseio.com",
      projectId: "moloko-01",
      storageBucket: "moloko-01.appspot.com",
      messagingSenderId: "632037249924",
      appId: "1:632037249924:web:5ed05b7d47a0a5a76983d1"
    };
    
    firebase.initializeApp(config);
    var database = firebase.database();
    
    var ref = firebase.database().ref();
    var key = []
    var data = []
    ref.on("value", function(snapshot) {
        var list_categories = document.getElementById("menu_card")
        var test = snapshot.val()
        var keys = Object.keys(test);
        var datas =  Object.values(test) 
        key =  keys
        data =  datas
        var categories = document.getElementById("categories")

        // console.log(keys)
        // console.log(Object.values(test))
        categories.innerHTML = ''
        for(var i=0;i<(datas[0].length);i++){
            categories.innerHTML += '<button type="button" data-filter="*" data-bs-target=".isotope-grid" data-bs-toggle="pill" class="btn btn-outline-secondary rounded-pill btn-sm is-checked me-2" aria-selected="false" role="tab" tabindex="-1">'+datas[0][i]+'</button>'
        }
    
        // var list_menu = document.getElementById("menu_tabs")
        list_categories.innerHTML = ""
        // console.log(datas[0]) // 1Configurations kısmı
        var icon =  '<svg class="text-primary" xmlns="http://www.w3.org/2000/svg" height="60" width="60" fill="currentColor" viewBox="0 0 5 5"> \
        <path d="M2.53229,2.50962a.08033.08033,0,0,0-.06026.03386c-.08988.111-.18242.22012-.26731.33484a2.19621,2.19621,0,0,0-.18855.3684,1.55123,1.55123,0,0,0-.11406.30783c-.009.03683-.0157.07436-.02328.11159a.42714.42714,0,0,1-.01434.06967c-.037.09462-.05317.13421-.16642.07409-.084-.04468-.16367-.09756-.24379-.14908a.15785.15785,0,0,1-.0484-.05116.78555.78555,0,0,1-.12763-.53026,1.64384,1.64384,0,0,1,.18523-.56756,1.55567,1.55567,0,0,1,.2582-.32213,2.19181,2.19181,0,0,1,.32044-.26236c.08271-.05593.16014-.11971.24216-.17673a1.16809,1.16809,0,0,1,.14767-.087q.2625-.13028.53685-.23439c.25814-.09842.51628-.19713.77254-.30057a2.928,2.928,0,0,1,.30688-.11559l.01209.00565.002.01141a.07664.07664,0,0,1-.01616.02231,3.21947,3.21947,0,0,0-.42484.44183,1.521,1.521,0,0,0-.32711.72084c-.02169.12687-.044.25346-.05338.38211a1.45047,1.45047,0,0,1-.024.155,2.38193,2.38193,0,0,1-.0669.30664,1.36513,1.36513,0,0,1-.35979.59176,1.34157,1.34157,0,0,1-.44527.27926.49875.49875,0,0,1-.25255.03219.04333.04333,0,0,1-.03553-.03858.64114.64114,0,0,1,.045-.32155,1.67711,1.67711,0,0,1,.29445-.4704c.02178-.02517.0442-.04987.0649-.076a.04679.04679,0,0,0,.00558-.02607c.00023-.0096-.02284-.0121-.039-.00272-.037.02152-.07281.04508-.11047.06529a.06715.06715,0,0,1-.03979.00328c-.01317-.00219-.01892-.03155-.01126-.05123.00525-.01333.01149-.02616.01711-.03927a3.58675,3.58675,0,0,1,.22921-.44417.23094.23094,0,0,0,.017-.05328l.017-.0199-.01-.00432Z"></path>\
    </svg>'
        for(var i=0; i<datas[0].length; i++ ){
            console.log(datas[0][i])
            var index_key = keys.indexOf(datas[0][i])
            console.log(index_key)
            list_categories.innerHTML += '<div class="mb-0 px-4 py-5 bg-light position-relative d-flex align-items-end justify-content-center">'+ icon + '<h3 class="mb-0 px-3 display-3">'+datas[0][i]+'</h3>'+icon+'</div>'+
            ''
            for(var k=0; k<datas[index_key].length; k++){
                list_categories.innerHTML += '<div class="d-flex align-items-center">\
                    <div>\
                        <img src="assets/img/menu/food1.jpg" alt=""\
                            class="width-60 rounded-circle shadow me-2 me-lg-3">\
                    </div>\
                    <div class="flex-grow-1">\
                        <div class="d-flex w-100 justify-content-between align-items-center">\
                            <h5 class="mb-2 fs-5 fw-semibold fst-italic font-serif">'+datas[index_key][k].name+'\
                            </h5>\
                            <span class="flex-grow-1 border-dashed-1 mx-3"></span>\
                            <span class="fw-bold">'+datas[index_key][k].price+' TL</span>\
                        </div>\
                        <p class="mb-0">'+datas[index_key][k].details+'</p>\
                    </div>\
                </div><br><br>'
            }
        }
       
    },function (error) {
        console.log("Error: " + error.code);
    });
    
    }
    setTimeout(() => {     init() }, 1500);
