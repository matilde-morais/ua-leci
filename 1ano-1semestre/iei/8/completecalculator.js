var op = "+"; // variável global que representa a operação a realizar (adição por defeito)

function operation() {
    var e = document.getElementById( "operation" ); // obtem a operação selecionada
    op = e.options[e.selectedIndex].value;
    // .options é um array com as opções do elemento <select>
    console.log( "Operation: "+op ); // mostra a operação na consola
}