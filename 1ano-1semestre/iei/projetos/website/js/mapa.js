var map = new L.Map("myMap", {center: [38.77214667390704, -9.096792855334686],zoom: 2});
var osmUrl="http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
var osmAttrib="Map data OpenStreetMap contributors";
var osm = new L.TileLayer(osmUrl, {attribution: osmAttrib});
map.addLayer(osm);
map.on("click", showCoordinates);

function showCoordinates(e){
	var s = document.getElementById("coordinates");
	s.innerHTML = "Latitude, Longitude = "+e.latlng.lat+", "+e.latlng.lng;
	}
	

var pontos=[
	L.marker([38.77214667390704, -9.096792855334686]).bindPopup("Sede IBM Lisboa")
	];
	
for(let i in pontos) {
	pontos[i].addTo(map);
	}
var grupo = new L.featureGroup(pontos);
map.fitBounds(grupo.getBounds());

var reitoria=L.polygon(
	[[38.77221542089243, -9.096955128984883],[38.772074267314665, -9.096964516716437],[38.77205596960822, -9.096608453469603],[38.772195554850214, -9.096593030767764]],
	{color:"red"});
	reitoria.addTo(map);

