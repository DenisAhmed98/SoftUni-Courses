function addItem() {
    let listContainer = document.querySelector('#items');
    let input = document.querySelector('#newItemText').value
    let li = document.createElement('li')
    
    li.textContent = input
    listContainer.appendChild(li);
}
