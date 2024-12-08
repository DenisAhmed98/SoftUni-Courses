function solve(input){
    const searchWords = input.shift().split(" ");
    const searchWordsObj = {}
    searchWords.forEach(element => {
        searchWordsObj[element] = 0;
    });

    input.forEach( word => {
        if (word in searchWordsObj){
            searchWordsObj[word] += 1 
        }
    });

    Object
        .entries(searchWordsObj)
        .sort((a, b) => b[1] - a[1])
        .forEach(([word, count]) => console.log(`${word} - ${count}`))
}

solve([
    'this sentence', 
    'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
    ])

        
solve([
    'is the', 
    'first', 'sentence', 'Here', 'is', 'another', 'the', 'And', 'finally', 'the', 'the', 'sentence'])