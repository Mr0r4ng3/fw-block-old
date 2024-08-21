const toggleSearchForm = document.getElementById("toggle-search-form");
const searchForm = document.getElementById("search-form");

toggleSearchForm.addEventListener("click", () => {
    searchForm.classList.toggle("hidden");
    toggleSearchForm.classList.toggle("rotate-180");
})