let botão = document.querySelector("#botão");
botão.style.background="blue";

botão.addEventListener("mouseover", mudaVerde);

function mudaVerde(){
    botão.style.background="green";
}