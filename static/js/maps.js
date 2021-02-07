// This function will render Google Maps and markers on all templates

function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 2,
        center: {
            lat: 46.619261,
            lng: -33.134766
        }
    });

    var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

// Here I define random locations to be marked on Google Maps

    var locations = [
        { lat: -34.6083, lng: -58.3712 },
        { lat: 53.33306, lng: -6.24889 },
        { lat: 52.531677, lng: 13.381777 },
        { lat: 40.4168, lng: -3.703790 },
        { lat: -23.5499978, lng: -46.625290 },
        { lat: 19.432608, lng: -99.133209 }
    ];

    var markers = locations.map(function (location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        });
    });

    var markerCluster = new MarkerClusterer(map, markers, {
        imagePath: "https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m"
    });

}