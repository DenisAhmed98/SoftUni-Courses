function adressBook(input){
    const adressBook = {}

    input.forEach(entry => {
        const [name, place] = entry.split(':');
        adressBook[name] = place;
    });

    const adressBookSorted = Object.entries(adressBook);
    
    adressBookSorted.sort( ([keyA],[keyB]) => {
        return keyA.localeCompare(keyB);
    });

    for (let [key,value] of adressBookSorted) {
        console.log(`${key} -> ${value}`)
    }
    
    
}

adressBook(['Tim:Doe Crossing','Bill:Nelson Place','Peter:Carlyle Ave','Bill:Ornery Rd'])