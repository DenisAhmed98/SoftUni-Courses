function solve(sentence){
    sentence = sentence.split(" ");

    for ( let w of sentence ){
        if (w.startsWith("#") && w.length > 1){
            const asciiCode = w.charCodeAt(1);

            if ((asciiCode >= 65 && asciiCode <= 90) || (asciiCode >= 97 && asciiCode <= 122) ){
                console.log(w.substring(1));
            }
        } 
    }
}

solve('Nowadays everyone uses # to tag a #special word in #socialMedia')
solve('The symbol # is known #variously in English-speaking #regions as the #number sign')
