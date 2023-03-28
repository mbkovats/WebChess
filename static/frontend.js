let before = "";
let beforeElem = "";
let count = 0;
let pause = 0;
function board(){
    count = 0;
    const request = new XMLHttpRequest();
    request.open("GET", 'move');
    request.send()
}
function move(square){
    if (pause == 1){
        ;
    }
    else{
        let elem = document.getElementById(square);
        const request = new XMLHttpRequest();
        if(before == square){
            ;
        }
        else if(before == ""){
            if(elem.innerHTML.includes("img")){
                before = square;
                beforeElem = elem;
                $(elem).css("border", "solid blue");
            }
        }
        else{
            request.open("POST", 'move');
            request.send(JSON.stringify(before + square));
            before = "";
            $(beforeElem).css("border", "");
        }
        request.onload = function(){
            response = JSON.parse(request.response)
            if(response == "FAIL"){
                return;
            }
            else if(response == "CAPTURED WHITE" || response == "PROMOTIONW"){
                $(elem).children(":first").detach().appendTo(document.getElementById("capturedblack"));
            }
            else if(response == "CAPTURED BLACK" || response == "PROMOTIONB"){
                $(elem).children(":first").detach().appendTo(document.getElementById("capturedwhite"));
            }
            if(square[1] == "1"){
                if(response == "SCASTLE"){
                    $(document.getElementById("H1")).children(":first").detach().appendTo(document.getElementById("F1"));
                }
                else if(response == "LCASTLE"){
                    $(document.getElementById("A1")).children(":first").detach().appendTo(document.getElementById("D1"));
                }
                else if(response == "PROMOTION"  || response == "PROMOTIONW" || response == "PROMOTIONB"){
                    $(document.getElementById("box1")).css("opacity", "1");
                    $(document.getElementById("button1")).css("opacity", "1");
                    before = elem;
                }
            }
            if(square[1] == "8"){
                if(response == "SCASTLE"){
                    $(document.getElementById("H8")).children(":first").detach().appendTo(document.getElementById("F8"));
                }
                else if(response == "LCASTLE"){
                    $(document.getElementById("A8")).children(":first").detach().appendTo(document.getElementById("D8"));
                }
                else if(response == "PROMOTION"  || response == "PROMOTIONW" || response == "PROMOTIONB"){
                    $(document.getElementById("box2")).css("opacity", "1");
                    $(document.getElementById("button2")).css("opacity", "1");
                    before = elem;
                    pause = 1;
                }
            }
            count++;
            $(beforeElem).children(":first").detach().appendTo(elem);
            document.getElementById("turncounter").innerText = "Turn " + count
            if(count % 2 == 0){
                $(document.getElementById("blackturn")).css("opacity", "0")
                $(document.getElementById("whiteturn")).css("opacity", "1")
            }
            else{
                $(document.getElementById("blackturn")).css("opacity", "1")
                $(document.getElementById("whiteturn")).css("opacity", "0")
            }
        }
    }
}
function promote(button){
    const request = new XMLHttpRequest();
    request.open("POST", 'promote');
    elem = document.getElementById("box" + button[6]);
    piece = elem.options[elem.selectedIndex].value;
    request.send(JSON.stringify(piece));
    $(before).children(":first").detach();
    if(button == "button2") {
        if(piece == "queen"){
            $("<img class = queen src=https://upload.wikimedia.org/wikipedia/commons/4/49/Chess_qlt60.png ></img>").appendTo(before);
        }
        else if(piece == "bishop"){
            $("<img class = bishop src=https://upload.wikimedia.org/wikipedia/commons/9/9b/Chess_blt60.png></img>").appendTo(before);
        }
        else if(piece == "knight"){
            $("<img class = knight src=https://upload.wikimedia.org/wikipedia/commons/2/28/Chess_nlt60.png ></img>").appendTo(before);
        }
        else if(piece == "rook"){
            $("<img class = rook src=https://upload.wikimedia.org/wikipedia/commons/5/5c/Chess_rlt60.png ></img>").appendTo(before);
        }
        $(document.getElementById("box2")).css("opacity", "0");
        $(document.getElementById("button2")).css("opacity", "0");
    }
    else {
        if(piece == "queen"){
            $("<img class = queen src=https://upload.wikimedia.org/wikipedia/commons/a/af/Chess_qdt60.png ></img>").appendTo(before);
        }
        else if(piece == "bishop"){
            $("<img class = bishop src=https://upload.wikimedia.org/wikipedia/commons/8/81/Chess_bdt60.png ></img>").appendTo(before);
        }
        else if(piece == "knight"){
            $("<img class = knight src=https://upload.wikimedia.org/wikipedia/commons/f/f1/Chess_ndt60.png ></img>").appendTo(before);
        }
        else if(piece == "rook"){
            $("<img class = rook src=https://upload.wikimedia.org/wikipedia/commons/a/a0/Chess_rdt60.png ></img>").appendTo(before);
        }
        $(document.getElementById("box1")).css("opacity", "0");
        $(document.getElementById("button1")).css("opacity", "0");
    }
    before = ""
    pause = 0;
}
document.getElementById("button1").addEventListener("click", function () { promote("button1");});
document.getElementById("button2").addEventListener("click", function () { promote("button2");});
document.getElementById("A8").addEventListener("click", function () { move("A8");}, false);
document.getElementById("B8").addEventListener("click", function () { move("B8");}, false);
document.getElementById("C8").addEventListener("click", function () { move("C8");}, false);
document.getElementById("D8").addEventListener("click", function () { move("D8");}, false);
document.getElementById("E8").addEventListener("click", function () { move("E8");}, false);
document.getElementById("F8").addEventListener("click", function () { move("F8");}, false);
document.getElementById("G8").addEventListener("click", function () { move("G8");}, false);
document.getElementById("H8").addEventListener("click", function () { move("H8");}, false);
document.getElementById("A7").addEventListener("click", function () { move("A7");}, false);
document.getElementById("B7").addEventListener("click", function () { move("B7");}, false);
document.getElementById("C7").addEventListener("click", function () { move("C7");}, false);
document.getElementById("D7").addEventListener("click", function () { move("D7");}, false);
document.getElementById("E7").addEventListener("click", function () { move("E7");}, false);
document.getElementById("F7").addEventListener("click", function () { move("F7");}, false);
document.getElementById("G7").addEventListener("click", function () { move("G7");}, false);
document.getElementById("H7").addEventListener("click", function () { move("H7");}, false);
document.getElementById("A6").addEventListener("click", function () { move("A6");}, false);
document.getElementById("B6").addEventListener("click", function () { move("B6");}, false);
document.getElementById("C6").addEventListener("click", function () { move("C6");}, false);
document.getElementById("D6").addEventListener("click", function () { move("D6");}, false);
document.getElementById("E6").addEventListener("click", function () { move("E6");}, false);
document.getElementById("F6").addEventListener("click", function () { move("F6");}, false);
document.getElementById("G6").addEventListener("click", function () { move("G6");}, false);
document.getElementById("H6").addEventListener("click", function () { move("H6");}, false);
document.getElementById("A5").addEventListener("click", function () { move("A5");}, false);
document.getElementById("B5").addEventListener("click", function () { move("B5");}, false);
document.getElementById("C5").addEventListener("click", function () { move("C5");}, false);
document.getElementById("D5").addEventListener("click", function () { move("D5");}, false);
document.getElementById("E5").addEventListener("click", function () { move("E5");}, false);
document.getElementById("F5").addEventListener("click", function () { move("F5");}, false);
document.getElementById("G5").addEventListener("click", function () { move("G5");}, false);
document.getElementById("H5").addEventListener("click", function () { move("H5");}, false);
document.getElementById("A4").addEventListener("click", function () { move("A4");}, false);
document.getElementById("B4").addEventListener("click", function () { move("B4");}, false);
document.getElementById("C4").addEventListener("click", function () { move("C4");}, false);
document.getElementById("D4").addEventListener("click", function () { move("D4");}, false);
document.getElementById("E4").addEventListener("click", function () { move("E4");}, false);
document.getElementById("F4").addEventListener("click", function () { move("F4");}, false);
document.getElementById("G4").addEventListener("click", function () { move("G4");}, false);
document.getElementById("H4").addEventListener("click", function () { move("H4");}, false);
document.getElementById("A3").addEventListener("click", function () { move("A3");}, false);
document.getElementById("B3").addEventListener("click", function () { move("B3");}, false);
document.getElementById("C3").addEventListener("click", function () { move("C3");}, false);
document.getElementById("D3").addEventListener("click", function () { move("D3");}, false);
document.getElementById("E3").addEventListener("click", function () { move("E3");}, false);
document.getElementById("F3").addEventListener("click", function () { move("F3");}, false);
document.getElementById("G3").addEventListener("click", function () { move("G3");}, false);
document.getElementById("H3").addEventListener("click", function () { move("H3");}, false);
document.getElementById("A2").addEventListener("click", function () { move("A2");}, false);
document.getElementById("B2").addEventListener("click", function () { move("B2");}, false);
document.getElementById("C2").addEventListener("click", function () { move("C2");}, false);
document.getElementById("D2").addEventListener("click", function () { move("D2");}, false);
document.getElementById("E2").addEventListener("click", function () { move("E2");}, false);
document.getElementById("F2").addEventListener("click", function () { move("F2");}, false);
document.getElementById("G2").addEventListener("click", function () { move("G2");}, false);
document.getElementById("H2").addEventListener("click", function () { move("H2");}, false);
document.getElementById("A1").addEventListener("click", function () { move("A1");}, false);
document.getElementById("B1").addEventListener("click", function () { move("B1");}, false);
document.getElementById("C1").addEventListener("click", function () { move("C1");}, false);
document.getElementById("D1").addEventListener("click", function () { move("D1");}, false);
document.getElementById("E1").addEventListener("click", function () { move("E1");}, false);
document.getElementById("F1").addEventListener("click", function () { move("F1");}, false);
document.getElementById("G1").addEventListener("click", function () { move("G1");}, false);
document.getElementById("H1").addEventListener("click", function () { move("H1");}, false);
