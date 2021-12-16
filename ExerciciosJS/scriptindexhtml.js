let paragrafo = document.querySelector("#paragrafoum");

//adicionando evento ao paragrafo:
paragrafo.addEventListener("mouseover", mudarCorVerde);
paragrafo.addEventListener("mouseout", mudaCorVermelha);

function mudarCorVerde(){
    paragrafoum.style.background="green";
}

function mudaCorVermelha(){
    paragrafoum.style.background="red";
}