function employees(input){
    for (const employe of input){
        console.log(`Name: ${employe} -- Personal Number: ${employe.length}`)
    }
}

employees([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'
    ])