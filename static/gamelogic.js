function getCookieValue(name) {
  let result = document.cookie.match("(^|[^;]+)\\s*" + name + "\\s*=\\s*([^;]+)")
  return result ? result.pop() : ""
}


var block = document.getElementById("block");
var hole = document.getElementById("hole");
var character = document.getElementById("character");
var score = 0;
var topscore = getCookieValue("topscore");
var paused = true;



if (topscore == undefined) 
{
  topscore = 0;
}


/*var gameWidth = parseInt(window.getComputedStyle(game).getPropertyValue("width"));
character.style.left = (gameWidth/2 - 16) + "px";*/

document.getElementById("topscore").innerHTML = "tvé nejlepší skóre: " + topscore;

hole.addEventListener('animationiteration', () => {
    var random = ((Math.random()*80));
    hole.style.left = random + "%";
    score++;
    document.getElementById("state").innerHTML = "";

    /*var timer = parseFloat(window.getComputedStyle(block).getPropertyValue("animation-duration"));
    if(timer > 2){
      console.log(timer);
    block.style.animationDuration = (timer - 0.1) + "s";
    hole.style.animationDuration = (timer - 0.1) + "s";
    }*/
    
});

function keyPressed(event) {
  var key = event.key;
  if(paused == false){
  if(key == "ArrowLeft" || key == "a"){
    var characterPos = parseInt(window.getComputedStyle(character).getPropertyValue("left"));
    var gameWidth = parseInt(window.getComputedStyle(game).getPropertyValue("width"));
    if (characterPos > 0){
      character.style.left = (characterPos-((gameWidth/100)*2))+"px";
    }
  }
  if(key == "ArrowRight" || key == "d"){
    var characterPos = parseInt(window.getComputedStyle(character).getPropertyValue("left"));
    var gameWidth = parseInt(window.getComputedStyle(game).getPropertyValue("width"));
    if (characterPos < gameWidth-32){
      character.style.left = (characterPos+((gameWidth/100)*2))+"px";
    }
  }
  }
  if(key == " "){
    pause();
  }
}

setInterval(function(){

  if(paused == false){
  var characterLeft = parseInt(window.getComputedStyle(character).getPropertyValue("left"));
  var characterTop = parseInt(window.getComputedStyle(character).getPropertyValue("top"));
  var wallPos = parseInt(window.getComputedStyle(block).getPropertyValue("top"));
  var holePos = parseInt(window.getComputedStyle(hole).getPropertyValue("left"));
  //document.getElementById("log").innerHTML = "chL: "+ characterLeft +" chT: "+ characterTop +" wT: "+ wallPos +" hL: "+ holePos;

  if((300 <= wallPos+64 && 300+32 >= wallPos) && (characterLeft <= holePos || characterLeft+32 >= holePos+64)){
    gameover();
  }else{
    document.getElementById("score").innerHTML = "score: " + score;
  }
}}, 10);

function gameover(){
  document.getElementById("state").innerHTML = "GAME OVER";
  if(score > topscore){
    topscore = score;
    document.getElementById("topscore").innerHTML = "topscore: " + topscore;

     document.cookie = "topscore=" + topscore; 
  }
  score = -1;
  var gameWidth = parseInt(window.getComputedStyle(game).getPropertyValue("width"));
  character.style.left = (gameWidth/2 - 16) + "px";
}

function pause(){
  if (paused == true){
    paused = false;
    block.style.animationPlayState = "running";
    hole.style.animationPlayState = "running";
    document.getElementById("state").innerHTML = "";
  }else{
    paused = true;
    block.style.animationPlayState = "paused";
    hole.style.animationPlayState = "paused";
    document.getElementById("state").innerHTML = "Pozastaveno";
  }
}
