function loadSport(baseUrl, onSuccess) {
    fetch(baseUrl)
        .then(response => response.json())
        .then(onSuccess)
        .catch(error => console.error('Error: ', error));
}

function createSport(baseUrl, sport, onSuccess) {
    fetch(baseUrl, {
        method: 'POST',
        body: JSON.stringify(sport)
    })
        .then(response => response.json())
        .then(onSuccess)
        .catch(error => console.error('Error: ', error));
}

function updateSport(baseUrl, sport, onSuccess) {
    fetch(baseUrl + sport._id, {
        method: 'PUT',
        body: JSON.stringify(sport)
    })
        .then(response => response.json())
        .then(onSuccess)
        .catch(error => console.error('Error: ', error));
}

function deleteSport(baseUrl, sport, onSuccess) {
    console.log(baseUrl + sport._id)
    fetch(baseUrl + sport._id, {
        method: 'DELETE'
    })
        .then(response => response.json())
        .then(onSuccess)
        .catch(error => console.error('Error: ', error));
}

function createElement(tag, properties, container) {
    const element = document.createElement(tag)

    Object.keys(properties).forEach(key => {
        if ( typeof properties[key] === 'object' ) {
            element[key] ??= {};
            Object.assign(element[key], properties[key]);
        } else {
            element[key] = properties[key];
        }
    });
    
    if ( container ) container.append(element);
    
    return element;
}

function init() {

    const baseUrl = 'http://localhost:3030/jsonstore/workout/';
    const fields = [...document.querySelectorAll('#workout, #location, #date')];
    const btnAddWorkoutEl = document.querySelector('#add-workout');
    const btnEditWorkoutEl = document.querySelector('#edit-workout');

    const listEl = document.querySelector('#list');

    btnAddWorkoutEl.addEventListener('click', createHandler);
    btnEditWorkoutEl.addEventListener('click', updateHandler);

    function loadEntries() {
        listEl.innerHTML = '';
        loadSport(baseUrl, (result) => {
            Object.values(result).forEach(createEntry);
        });
    }

    function createEntry({ workout, location, date, _id }){
        const entryEl = createElement('div', { className: 'container', dataset: { workout, location, date, _id }}, listEl);
        createElement('h2', { textContent: workout }, entryEl);
        createElement('h3', { textContent: date }, entryEl);
        createElement('h3', { id: 'location', textContent: location }, entryEl);
        const btnContainerEl = createElement('div', { id: 'buttons-container'}, entryEl);
        createElement('button', { className: 'change-btn', textContent: 'Change', onclick: changeHandler }, btnContainerEl);
        createElement('button', { className: 'delete-btn', textContent: 'Done', onclick: deleteHandler }, btnContainerEl);
    }

    function deleteEntry({ workout, location, date, _id }) {
        listEl.querySelector(`div[data-_id="${_id}"]`).remove();
    }

    function createHandler(e) {
        e.preventDefault();

        const [ workout, location, date ] = fields.map(field => field.value);

        if ( ! workout || ! location || ! date ) return;

        const sport = { workout, location, date };

        createSport(baseUrl, sport, (result) => {
            createEntry(result);
        });

        fields.forEach(field => field.value = '');
    }

    function changeHandler(e) {
        const entryEl = e.target.closest('div.container');
        const values = Object.values(entryEl.dataset);

        entryEl.classList.add('active');

        fields.forEach((field, index) => field.value = values[index]);

        btnAddWorkoutEl.disabled = true;
        btnEditWorkoutEl.disabled = false;
    }

    function updateHandler(e) {
        e.preventDefault();

        const [ workout, location, date ] = fields.map(field => field.value);

        if ( ! workout || ! location || ! date ) return;

        const entryEl = listEl.querySelector('div.active');

        const sport = { workout, location, date, _id: entryEl.dataset._id };

        updateSport(baseUrl, sport, (result) => {
            loadEntries();
            fields.forEach(field => field.value = '');
            btnAddWorkoutEl.disabled = false;
            btnEditWorkoutEl.disabled = true;
        });
    }

    function deleteHandler(e) {
        const entryEl = e.target.closest('div.container');
        console.log(entryEl);

        const sport = Object.assign({}, entryEl.dataset);

        deleteSport(baseUrl, sport, (result) => {
            deleteEntry(result);
        });
    }

    loadEntries();
}

document.addEventListener('DOMContentLoaded', init);