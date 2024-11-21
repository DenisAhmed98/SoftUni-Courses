function solve(array){
    let even = 0;
    let odd = 0;
    for(let i=0; i<array.length; i++){
        if (array[i] % 2 == 0) even += array[i];
        else odd += array[i];
    }
    console.log(even-odd);
}

solve([1,2,3,4,5,6])

solve([3,5,7,9])

solve([2,4,6,8,10])