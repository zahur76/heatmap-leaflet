$(document).ready(function(){
        
    const copy = "© <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
    const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
    //base layer
    const osm = L.tileLayer(url, { attribution: copy });

    // heat map configuration
    let cfg = {
        "radius": 40,
        "useLocalExtrema": true,
        valueField: 'number'
    };
    let heatmapLayer = new HeatmapOverlay(cfg);

    let propertyHeatMap = new L.Map('map', {
        center: new L.LatLng(-20.251, 57.580),
        zoom: 11,
        layers: [osm, heatmapLayer]
    })
    // retrieve data from models
    async function load_markers() {
        const markers_url = '/markerJson'   
        const response = await fetch(markers_url)
        const data= await response.json()
        let min = Math.min(...data.map(data => data.number))
        let max = Math.max(...data.map(data => data.number))
        // set data for heatmap
        heatmapLayer.setData({
            min: min,
            max: max,
            data: data
        });
    }
    load_markers()

});