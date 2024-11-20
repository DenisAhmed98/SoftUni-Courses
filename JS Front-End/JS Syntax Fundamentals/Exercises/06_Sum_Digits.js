function solve(number){
    stringNum = number.toString();
    let sum=0;

    for (let i=0; i< stringNum.length; i++){
        sum += Number(stringNum[i])
    }

    console.log(sum)
}

solve(245678)