function solve(input){
    const dictionary = {}


    input.forEach(element => {
        const objects = JSON.parse(element)
        const key = Object.keys(objects);
        const value = Object.values(objects);
    
        dictionary[key[0]] = value[0]
        
    });
    const dictionarySorted = Object.entries(dictionary);
    
    dictionarySorted.sort( ([keyA],[keyB]) => {
        return keyA.localeCompare(keyB);
    });

    for (let [key,value] of dictionarySorted){
        
        console.log(`Term: ${key} => Definition: ${value}`)
    }
}