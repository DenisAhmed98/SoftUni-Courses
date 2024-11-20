function solve(fruit, weight, price){
    let kg = weight / 1000
    money = kg * price
    console.log(`I need $${money.toFixed(2)} to buy ${kg.toFixed(2)} kilograms ${fruit}.`)
}

solve('orange', 2500, 1.80)