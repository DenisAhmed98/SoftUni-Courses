function solve(a, b, c) {
    let negativeCount = 0;

    if (a < 0) negativeCount++;
    if (b < 0) negativeCount++;
    if (c < 0) negativeCount++;

    if (negativeCount % 2 === 0) {
        console.log("Positive");
    } else {
        console.log("Negative");
    }
}

solve(5,12,-15)
solve(-6,-12,14)
solve(-1,-2,-3)
solve(-5,1,1)