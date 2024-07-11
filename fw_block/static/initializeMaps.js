const mapElements = document.querySelectorAll('.map-div');

mapElements.forEach(mapElement => {

    let zoom_level = 5
    let cords = [parseFloat(mapElement.dataset.latitude), parseFloat(mapElement.dataset.longitude)]

    const map = L.map(mapElement).setView(
        cords,
        zoom_level
    );

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    L.marker(cords).addTo(map);
})