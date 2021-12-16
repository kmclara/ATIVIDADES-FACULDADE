let botão = document.querySelector("#botão");
botão.style.background="blue";

botão.addEventListener("mouseover", mudaVerde);

function mudaVerde(){
    botão.style.background="green";
}

botão.addEventListener("mouseout", mudaAzul);

function mudaAzul(){
    botão.style.background="blue"
}