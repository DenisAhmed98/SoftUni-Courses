function solve(array){
    array.sort(function(a, b){return a-b});
    let answer = [];
    let counter = array.length;


    for (let i=0; i<counter; i++){
        if (i % 2 == 0) {
            answer.push(array[0])
            array.shift()
        }
        else{
            answer.push(array[array.length-1])
            array.pop()
        }
    }

    return answer 
}

solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56])