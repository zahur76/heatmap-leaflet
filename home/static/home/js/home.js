$(document).ready(function(){
        
    const copy = "© <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
    const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
    //base layer
    const osm = L.tileLayer(url, { attribution: copy });
    
    const map = L.map("map", { layers: [osm], center: [-20.251, 57.580], zoom: 10 });

});