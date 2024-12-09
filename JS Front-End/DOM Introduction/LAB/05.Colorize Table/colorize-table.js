function colorize() {
    let tableRows = document.querySelectorAll("tbody tr")
    
    for (let i = 1; i < tableRows.length; i += 2){
        tableRows[i].style = "background: teal"
    }
}