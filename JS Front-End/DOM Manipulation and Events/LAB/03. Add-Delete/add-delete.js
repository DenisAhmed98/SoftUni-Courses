function addItem() {

    function deleteItem(e) {
        e.currentTarget.parentElement.remove();
    }

    let listContainer = document.querySelector('#items');
    let input = document.querySelector('#newItemText').value;
    let li = document.createElement('li');

    if (input == '') return

    let deleteLink = document.createElement('a');
    deleteLink.setAttribute('href', '#');
    deleteLink.textContent = "[Delete]"

    deleteLink.addEventListener('click', deleteItem)
    
    
    li.textContent = input
    li.appendChild(deleteLink);
    listContainer.appendChild(li);
}
