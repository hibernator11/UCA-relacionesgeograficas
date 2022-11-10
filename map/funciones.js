function mostrarMapa(datos){                 
    document.getElementById('mapa').innerHTML = "<div id='mapid'></div>";
    var tiles = L.tileLayer('https://api.mapbox.com/styles/v1/bvmc/ckx663h9h5sr315p5o1dvpqhp/tiles/{z}/{x}/{y}?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery Â© <a href="https://www.mapbox.com/">Mapbox</a>',
            maxZoom: 18,
            tileSize: 512,
            zoomOffset: -1,
            accessToken: 'pk.eyJ1IjoiYnZtYyIsImEiOiJjanFucTh2OTQwN3UxM3hwc29tdTRlZG4xIn0.rDf0DcczLzlH7-7E35tL0Q'
        }),
        latlng = L.latLng(17.37, -95.04);

    var map = L.map('mapid', {center: latlng, zoom: 6, layers: [tiles]});

    var markers = L.markerClusterGroup();

    for (var i = 0; i < datos.length; i++) {
        var a = datos[i];
        var title = datos[i].texto;
        var marker = L.marker(new L.LatLng(a.lat, a.lon));
        marker.bindPopup(title);
        markers.addLayer(marker);
    }

    map.addLayer(markers);
    return map;
}

function refresca(datos) {

    document.getElementById('mapa').innerHTML = "<div id='mapid'></div>";
    var cont = L.DomUtil.get('mapid');
    if(cont != null){
        cont._leaflet_id = null;
    }
   
    var tiles = L.tileLayer('https://api.mapbox.com/styles/v1/bvmc/ckx663h9h5sr315p5o1dvpqhp/tiles/{z}/{x}/{y}?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery Â© <a href="https://www.mapbox.com/">Mapbox</a>',
            maxZoom: 18,
            tileSize: 512,
            zoomOffset: -1,
            accessToken: 'pk.eyJ1IjoiYnZtYyIsImEiOiJjanFucTh2OTQwN3UxM3hwc29tdTRlZG4xIn0.rDf0DcczLzlH7-7E35tL0Q'
        }),
        latlng = L.latLng(17.37, -95.04);

   var map = L.map('mapid', {center: latlng, zoom: 6, layers: [tiles]});
   var eachLayer = mapid.eachLayer(function (layer) {
        mapid.removeLayer(layer);
    });
    
   var markers = L.markerClusterGroup();

    for (var i = 0; i < datos.length; i++) {
    	
  	var mostrar = false;
        var title = datos[i].texto;
        var tipo = datos[i].tipo;

        if ($("#españa_colonias").is(":checked") && tipo.includes("España--Colonias--Historia--Fuentes")) mostrar = true;
        if ($("#guatemala_historia").is(":checked") && tipo.includes("Guatemala--Historia--Siglo XVI--Fuentes")) mostrar = true;
        if ($("#manuscritos_mexicanos").is(":checked") && tipo.includes("Manuscritos, Mexicanos")) mostrar = true;
        if ($("#mexico_historia").is(":checked") && tipo.includes("México--Historia--Siglo XVI--Fuentes")) mostrar = true;
        if ($("#nueva_españa_descripcion").is(":checked") && tipo.includes("Nueva España--Descripción y viaje")) mostrar = true;
        if ($("#nueva_españa_historia").is(":checked") && tipo.includes("Nueva España--Historia--Fuentes")) mostrar = true;
        if ($("#nueva_españa_mapas").is(":checked") && tipo.includes("Nueva España--Mapas, Manuscritos")) mostrar = true;
        if ($("#Pindigenas_guatemala_arte").is(":checked") && tipo.includes("Pueblos indígenas--Guatemala--Arte")) mostrar = true;
        if ($("#Pindigenas_guatemala_historia").is(":checked") && tipo.includes("Pueblos indígenas--Guatemala--Historia--Fuentes")) mostrar = true;
        if ($("#Pindigenas_mexico_artes").is(":checked") && tipo.includes("Pueblos indígenas--México--Artes")) mostrar = true;
        if ($("#Pindigenas_mexico_historia").is(":checked") && tipo.includes("Pueblos indígenas--México--Historia--Fuentes")) mostrar = true;
        if ($("#Arte_siglo_xvi").is(":checked") && tipo.includes("Arte--Siglo XVI--Nueva España")) mostrar = true;
        if (mostrar == true) {
            var a = datos[i];
            var marker = L.marker(new L.LatLng(a.lat, a.lon));
            marker.bindPopup(title);
            markers.addLayer(marker);
        }

    }
    map.addLayer(markers);
    return map;
}


/*

function refresca(datos) {

    document.getElementById('mapa').innerHTML = "<div id='mapid'></div>";
    var cont = L.DomUtil.get('mapid');
    if(cont != null){
        cont._leaflet_id = null;
    }
    var tiles = L.tileLayer('https://api.mapbox.com/styles/v1/bvmc/ckx663h9h5sr315p5o1dvpqhp/tiles/{z}/{x}/{y}?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery Â© <a href="https://www.mapbox.com/">Mapbox</a>',
            maxZoom: 18,
            tileSize: 512,
            zoomOffset: -1,
            accessToken: 'pk.eyJ1IjoiYnZtYyIsImEiOiJjanFucTh2OTQwN3UxM3hwc29tdTRlZG4xIn0.rDf0DcczLzlH7-7E35tL0Q'
        }),
        latlng = L.latLng(40.19, -3.82);

    var map = L.map('mapid', {center: latlng, zoom: 6, layers: [tiles]});
    var eachLayer = mapid.eachLayer(function (layer) {
        mapid.removeLayer(layer);
    });
    var markers = L.markerClusterGroup();

    for (var i = 0; i < datos.length; i++) {
        var mostrar = false;
        var title = datos[i].texto;

        if ($("#Edificios").is(":checked") && title.includes("Edificios y monumentos")) mostrar = true;
        if ($("#Personajes").is(":checked") && title.includes("Personajes cÃ©lebres")) mostrar = true;
        if ($("#Religiosas").is(":checked") && title.includes("Religiosas")) mostrar = true;
        if ($("#Magia").is(":checked") && title.includes("Magia y Fantasia")) mostrar = true;
        if ($("#Tradiciones_locales").is(":checked") && title.includes("Tradiciones locales")) mostrar = true;
        if ($("#Tradiciones_historicas").is(":checked") && title.includes("Tradiciones histÃ³ricas")) mostrar = true;
        if ($("#Tradiciones_costumbres").is(":checked") && title.includes("Tradiciones y costumbres")) mostrar = true;
        if ($("#Tragicas").is(":checked") && title.includes("TrÃ¡gicas")) mostrar = true;
        if ($("#Hitos").is(":checked") && title.includes("Hitos geogrÃ¡ficos y urbanos")) mostrar = true;
        if (mostrar == true) {
            var a = datos[i];
            var marker = L.marker(new L.LatLng(a.lat, a.lon));
            marker.bindPopup(title);
            markers.addLayer(marker);
        }
    }
    map.addLayer(markers);
    return map;
}












function refresca(mapid, datos) {

	document.getElementById('mapid').innerHTML = "";
	
	var cont = L.DomUtil.get('mapid');
      	if(cont != null){
        	cont._leaflet_id = null;
      	}
      	var eachLayer = mapid.eachLayer(function (layer) {
         mapid.removeLayer(layer);
       });
var tiles = L.tileLayer('https://api.mapbox.com/styles/v1/bvmc/ckx663h9h5sr315p5o1dvpqhp/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'pk.eyJ1IjoiYnZtYyIsImEiOiJjanFucTh2OTQwN3UxM3hwc29tdTRlZG4xIn0.rDf0DcczLzlH7-7E35tL0Q'
        }),
	latlng = L.latLng(40.19, -3.82);

		
	
       
       var map = L.map('mapid', {center: latlng, zoom: 6, layers: [tiles]});
         var markers = L.markerClusterGroup();
            
         for (var i = 0; i < datos.length; i++) {
            var mostrar = false;
            var title = datos[i].texto;
           	
            if ($("#Edificios").is(":checked") && title.includes("Edificios y monumentos")) mostrar = true;
            if ($("#Personajes").is(":checked") && title.includes("Personajes célebres")) mostrar = true;
            if ($("#Religiosas").is(":checked") && title.includes("Religiosas")) mostrar = true;
            if ($("#Magia").is(":checked") && title.includes("Magia y Fantasia")) mostrar = true;
            if ($("#Tradiciones_locales").is(":checked") && title.includes("Tradiciones locales")) mostrar = true;
            if ($("#Tradiciones_historicas").is(":checked") && title.includes("Tradiciones históricas")) mostrar = true;
            if ($("#Tradiciones_costumbres").is(":checked") && title.includes("Tradiciones y costumbres")) mostrar = true;
            if ($("#Tragicas").is(":checked") && title.includes("Trágicas")) mostrar = true;
            if ($("#Hitos").is(":checked") && title.includes("Hitos geográficos y urbanos")) mostrar = true;
            if (mostrar == true) {           
            	var a = datos[i];
		var marker = L.marker(new L.LatLng(a.lat, a.lon));
		marker.bindPopup(title);
		markers.addLayer(marker);            	
            }
      	}
		map.addLayer(markers);
		return map;
}*/


/*function refrescaOLD(mymap) {

    var eachLayer = mymap.eachLayer(function (layer) {
        let icon;


        if (layer._url == undefined && layer._popup != undefined) { // Si es layer de marker
            var mostrar = false;
            var auxContent = layer._popup._content;
            icon = layer.options.icon;

            if ($("#Edificios").is(":checked") && auxContent.includes("Edificios y monumentos")) mostrar = true;
            if ($("#Personajes").is(":checked") && auxContent.includes("Personajes célebres")) mostrar = true;
            if ($("#Religiosas").is(":checked") && auxContent.includes("Religiosas")) mostrar = true;
            if ($("#Magia").is(":checked") && auxContent.includes("Magia y Fantasia")) mostrar = true;
            if ($("#Tradiciones_locales").is(":checked") && auxContent.includes("Tradiciones locales")) mostrar = true;
            if ($("#Tradiciones_historicas").is(":checked") && auxContent.includes("Tradiciones históricas")) mostrar = true;
            if ($("#Tradiciones_costumbres").is(":checked") && auxContent.includes("Tradiciones y costumbres")) mostrar = true;
            if ($("#Tragicas").is(":checked") && auxContent.includes("Trágicas")) mostrar = true;
            if ($("#Hitos").is(":checked") && auxContent.includes("Hitos geográficos y urbanos")) mostrar = true;
            if (mostrar) {
                icon.options.iconSize = [25, 41];
                icon.options.shadowSize = [41,41];
            } else {
                icon.options.iconSize = [0, 0];
                icon.options.shadowSize = [0,0];
            }
            layer.setIcon(icon);

        }
    });

    // for (var indice in datos) {
    //     var marker = L.marker([datos[indice].lat, datos[indice].lon]); //.addTo(mymap);
    //     // mymap.addLayer(marker);
    //
    //     marker.addTo(mymap);
    //     marker.bindPopup(datos[indice].texto);
    // }
}*/
