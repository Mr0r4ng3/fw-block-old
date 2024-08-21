const selects = document.querySelectorAll('select')

const options = {
    searchable: true,
    selectedtext: "firewalls seleccionados"
}

selects.forEach(select => {
    NiceSelect.bind(select, options)
})