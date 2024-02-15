var type = "line"; // line graphic by default

function graphic() { 
    var e = document.getElementById( "graphicType" ); // get the element
    type = e.options[e.selectedIndex].value; // get the value
}

function draw () {
    $("#myGraph").highcharts({
        chart: { type: type },
        title: { text: "Temperatures Average" },
        series:[
            { name: "Lisboa",
            data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]},
            { name: "Porto",
            data: [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5]},
            { name: "Aveiro",
            data: [3.9, 4.2, 6.0, 9.2, 13.5, 17.0, 19.5, 20.3, 18.5, 14.5, 9.8, 5.1]}
            ]
    });
}