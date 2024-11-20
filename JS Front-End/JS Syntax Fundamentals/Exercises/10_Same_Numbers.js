function solve(number){
    stringNum = number.toString();
    let sum=0;
    let flag = true

    for (let i=0; i< stringNum.length; i++){
        if (i!=0 && flag == true){
            if (stringNum[i-1] != stringNum[i])
                flag = false
        }
        sum += Number(stringNum[i])
    }
    console.log(flag)
    console.log(sum)
}

solve(1234)