const falseSubmitButton = document.getElementById("false-submit-btn")
const submitButton = document.getElementById("submit-btn")

falseSubmitButton.addEventListener("click", () => {
    submitButton.click()
})