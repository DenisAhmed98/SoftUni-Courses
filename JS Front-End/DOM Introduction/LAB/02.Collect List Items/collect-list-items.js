function extractText() {
    let items = document.querySelectorAll("#items li")
    let textContainer = document.querySelector("#result")

    for (i of items){
        textContainer.value = textContainer.value + i.textContent + '\n' 
    }

}