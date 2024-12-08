function phoneBook(string){
    let phoneBook = {};

    for (let line of string){
        let tokens = line.split(' ');
        phoneBook[tokens[0]] = tokens[1];
    }

    const keys = Object.keys(phoneBook);

    for (const key of keys) {
        console.log(`${key} -> ${phoneBook[key]}`)
    }

}