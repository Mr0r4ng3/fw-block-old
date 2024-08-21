const datePickerInput = document.getElementById('date-picker')

const queryString = window.location.search
const urlParams = new URLSearchParams(queryString)

const nowDate = new Date()

const defaultDateRange = [`${nowDate.getFullYear()}-${nowDate.getMonth()}-${nowDate.getDate()}`, `${nowDate.getFullYear()}-${nowDate.getMonth() + 1}-${nowDate.getDate() + 1}`]

const dateRange = urlParams.get("date-range") ? urlParams.get("date-range").split(" a ") : defaultDateRange

const options = {
    mode: "range",
    altInput: true,
    altFormat: "F j, Y",
    dateFormat: "Y-m-d",
    locale: "es",
    defaultDate: dateRange
}

const fp = flatpickr(datePickerInput, options)

if (!urlParams.get("date-range")) {
    const filterForm = document.getElementById("filters-form")

    filterForm.submit()
}