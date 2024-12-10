function deleteByEmail() {
    let tableContainer = document.querySelectorAll('#customers td:nth-child(2)');
    let inputSearch = document.querySelector('input[name="email"]').value
    let result = document.querySelector('#result')

    if (inputSearch == '') return

    for (item of tableContainer){
        if (item.textContent.includes(inputSearch)){
            item.parentElement.remove();
            result.textContent = 'Deleted.'
            break;
        }
        else{
            result.textContent = 'Not found.'
        }
    }
}
