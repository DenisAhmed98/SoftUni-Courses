function sumTable() {
    let tableRows = document.querySelectorAll("table tr")
    let total = 0
    for (let i=1; i < tableRows.length; i++){
        let cols = tableRows[i].children;
        total += Number(cols[cols.length-1].textContent)
    }
    document.getElementById("sum").textContent = total
}