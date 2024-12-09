function solve() {
   let citiesList = document.querySelectorAll('#towns li');
   let searchWord = document.getElementById('searchText').value;
   let resultCounter = 0;

   for (citie of citiesList){
      citie.style.fontWeight = '';
      citie.style.textDecoration = '';
      resultCounter = 0;
   }

   for (citie of citiesList){
      if (searchWord == ''){
         break;
      }
      if (citie.textContent.includes(searchWord)){
         citie.style.fontWeight = 'bold';
         citie.style.textDecoration = 'underline';
         resultCounter++;
      }
   }

   document.getElementById('result').textContent = `${resultCounter} matches found`;
}