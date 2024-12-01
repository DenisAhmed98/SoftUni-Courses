function solve(array,steps){
    let answer = []
    for (let i=0; i<array.length; i+=steps){
        answer.push(array[i])
    }
    
    return answer
    
}

solve(['5','20','31','4','20'],2)

solve(['dsa', 'asd', 'test', 'tset'], 2)

solve(['1', '2', '3', '4', '5'], 6)