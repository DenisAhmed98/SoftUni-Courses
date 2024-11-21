function solve(text, search){
    let words = text.split(' ');
    let count = 0;

    for (let w of words){
        if (w === search){
            count++;
        }
    }

    console.log(count)
}

solve('softuni is great place for learning new programming languages',
'softuni')