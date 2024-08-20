const mapElements = document.querySelectorAll('.map-div');

mapElements.forEach(mapElement => {

    let zoom_level = 5
    let latitude = mapElement.dataset.latitude
    let longitude = mapElement.dataset.longitude
    let cords = [parseFloat(latitude), parseFloat(longitude)]

    const map = L.map(mapElement).setView(
        cords,
        zoom_level
    );

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: `&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> | <a href="https://www.openstreetmap.org/?mlat=${latitude}&mlon=${longitude}#map=5/${latitude}/${longitude}">\u00A0${latitude}\u00A0\u00A0${longitude}\u00A0</a>`
    }).addTo(map);

    L.marker(cords).addTo(map);
})