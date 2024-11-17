function solve(a, b, c){
    let result

    if (a > b && a > c) {
        result = a
    }
    else if (b > a && b > c) {
        result = b
    }
    else if (c > a && c > b) {
        result = c
    }

    console.log(`The largest number is ${result}.`)
}

solve(5,2,1)