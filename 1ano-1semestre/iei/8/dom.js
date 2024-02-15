// Getting elements from the DOM

// Get the element with id "op1"
var x = document.getElementById( "op1" );
// Get the element with id "op2"
var y = document.getElementById( "op2" );
// Get the element with id "res"
var res = document.getElementById("res");

// Get the values

// Convert the value of x to a float and store it in valorX
var valorX = parseFloat(x.value);
// Convert the value of y to a float and store it in valorY
var valorY = parseFloat(y.value);

// Log the values

// Log the value of x
console.log( valorX );
// Log the value of y
console.log( valorY );

// Add the values

// Add valorX and valorY and store the result in valorRes
var valorRes = valorX + valorY;

// Log the result

// Set the value of res to valorRes
res.value = valorRes;