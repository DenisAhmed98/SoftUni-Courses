function solve() {
   let tableRows = document.querySelectorAll('.container tr');
   let searchWord = document.getElementById('searchField').value;
   if (searchWord != ''){
      for (rows of tableRows) {
         rows.classList.remove("select");
      }
   
      for (rows of tableRows) {
         tableCells = rows.querySelectorAll('td')
         for (cells of tableCells){
            if (cells.textContent.includes(searchWord)){
               rows.classList.add("select");
               break;
            }
         }
      }
   }
   
}