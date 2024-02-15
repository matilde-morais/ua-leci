var type = "line";
function graphic() {
	var e = document.getElementById( "selection" );
	type = e.options[e.selectedIndex].value;
	}
	






function draw() {
	$("#myGraph").highcharts({
		chart: { type: "area" },
		title: { text: "Receita do mercado de Inteligência Artificial em todo o mundo" },
		xAxis: { categories: ["2016", "2017", "2018", "2019", "2020", "2021","2022", "2023", "2024", "2025"]
			},
			
			
		series: [
			{
				name: "Receita",
				data: [1.0, 2.0, 3.0, 4.0, 5.0, 8.0, 12.5, 18.0, 24.2, 32.0]
			},
				
			]
			});
			}
