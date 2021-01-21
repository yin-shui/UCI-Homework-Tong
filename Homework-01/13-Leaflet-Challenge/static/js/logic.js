// Creating map object
var earthquake_link = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";
var tectonic_link = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json";

function markerSize(magnitude){
  return magnitude * 3;
}

var earthquakes = new L.LayerGroup();

// Traverse through USGS API locating the magnitude and depth
// Create popup to display magnitude & depth as well as set fill color to depth intensity
d3.json(earthquake_link, function(data){
  
  L.geoJson(data.features, {
    
    onEachFeature: function(feature, layer){
      layer.bindPopup("<h3>Magnitude: " + feature.properties.mag + "</h3>" + "<hr>" + "<h3> Depth: " + feature.geometry.coordinates[2] + "</h3>");
    },
    pointToLayer: function(feature, latlng) {
      return new L.circleMarker(latlng, 
        {radius: markerSize(feature.properties.mag)});
      },
        style: function(gF){
          return {
        fillColor: markerColor(gF.geometry.coordinates[2]),
        fillOpacity: .6,
        color: "white",
        stroke: true,
        weight: .8
    }}
  }).addTo(earthquakes);  
});

var tectonicPlates = new L.LayerGroup();

// Build the tectonic plate lines 
d3.json(tectonic_link, function(geoJson){
  L.geoJson(geoJson.features, {
    style: function(gF){
      return{
    color: "yellow",
    weight: 2
      }
    },
  }).addTo(tectonicPlates);
});

// Set marker colors for earthquake depth
function markerColor(depth){
  if (depth < 10){
    return "#36C600"
  }
  else if (depth < 30) {
    return "#B4CE00"
  }
  else if (depth < 50){
    return "#D2AD00"
  }
  else if (depth < 70){
    return "#D57000"
  }
  else if (depth < 90){
    return "#D93100"
  }
  else { return "#DD0010"}
};

// Set tile layers for light map, satellite map, and dark map 
function createMap(){
var light = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "light-v10",
  accessToken: API_KEY

});

var satellite = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "satellite-v9",
  accessToken: API_KEY
});

var darkMap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "dark-v10",
  accessToken: API_KEY
});

// Create baseMap and overlayMap types for user control
var baseMaps = {
  "Dark Map":darkMap,
  "Light Map": light,
  "Satellite": satellite
};

var overlayMaps = {
  "Earthquakes": earthquakes,
  "Tectonic Plates": tectonicPlates
};

// Set default map location coordinates and place map in specified html div class
var map = L.map("mapid", {
  center: [32.309491892349165, -64.76305089605304],
  zoom: 3,
  layers: [satellite, earthquakes]
});

L.control.layers(baseMaps, overlayMaps).addTo(map);

// Set legend location to bottom right
var legend = L.control({
  position: "bottomright"
});

// Create the legend div class as well as its grades
legend.onAdd = function(map){
  var div = L.DomUtil.create("div", "legend"),
  grades = [-10, 10, 30, 50, 70, 90],
  labels = [];

 div.innerHTML += "<h4 style='margin:4px'>Earthquake Depth</h4>"

// loop through our density intervals and generate a label with a colored square for each interval
  for (var i = 0; i < grades.length; i++) {
      div.innerHTML +=
          '<i style="background:' + markerColor(grades[i] + 1)   + '"></i> ' +
          grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
  }

  return div;
};

legend.addTo(map);
}

createMap();

