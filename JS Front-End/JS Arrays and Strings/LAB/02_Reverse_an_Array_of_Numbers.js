function solve(n, array){
    let new_array = []

    for (let i=0; i<n; i++){
        new_array.push(array[i])
    }
    new_array = new_array.reverse()
    console.log(new_array.join(" "))
}

solve(3, [10, 20, 30, 40, 50])