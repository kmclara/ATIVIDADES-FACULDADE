let botão = document.querySelector("#botão");
botão.style.background="blue";

let estaQuebrado=false;

botão.addEventListener("mouseover", mudaVerde);

function mudaVerde(){
    if(estaQuebrado==false)
        botão.style.background="green";
}

botão.addEventListener("mouseout", mudaAzul);

function mudaAzul(){
    if(estaQuebrado==false)
        botão.style.background="blue"
}

botão.addEventListener("click", mudaVermelho);

function mudaVermelho(){
    botão.style.background="red";
    botão.innerHTML="Quebrei!";
    estaQuebrado=true
}