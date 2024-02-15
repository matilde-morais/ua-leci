function calculate(){

    // get the elements

    var x = document.getElementById( "op1" );
    var y = document.getElementById( "op2" );
    var res = document.getElementById( "res" );
                
    // get the values and transform them to float

    var valorX = parseFloat(x.value);
    var valorY = parseFloat(y.value);

    // show the values

    console.log( valorX ); // mostra o primeiro operador na consola
    console.log( valorY ); // mostra o segundo operador na consola
                
    // calculate the sum
    resValor = valorX + valorY;

    // show the result

    res.value = resValor;
    console.log(res.value); // mostra o resultado da soma na consola
    
}   