function extract(content) {
    let text = document.getElementById(content).textContent;
    let patern = /\(([^)]+)\)/g;
    let result = []
    let matches = patern.exec(text);

    while(matches){
        result.push(matches[1]);
        matches = patern.exec(text)
    }

    return result.join('; ');
}