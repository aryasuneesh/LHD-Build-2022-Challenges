var character = document.getElementById("character");
var block = document.getElementById("block");
var counter=0;

function jump() {
    if(character.classList != "animate"){
        character.classList.add("animate");
    }
    setTimeout(function(){
        character.classList.remove("animate");
    }, 300);
}

var checkDead = setInterval(function() {
    var characterTop = parseInt(window.getComputedStyle(character).getPropertyValue("top"));
    var blockLeft = parseInt(window.getComputedStyle(block).getPropertyValue("left"));
    if(blockLeft<20 && blockLeft>-20 && characterTop>=130){
        block.style.animation = "none";
    
        alert("You Lose. Score: "+Math.floor(counter/60));
        counter = 0;
        block.style.animation = "block 1s infinite linear";
    }
    else{
        counter++;
        document.getElementById("scoreSpan").innerHTML = Math.floor(counter/60);
    }
}, 10);

