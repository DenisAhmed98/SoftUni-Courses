function store(stockInput, orderInput){
    let products = {}
    for (let i=0; i < stockInput.length; i+=2){
        if (stockInput[i] in products){
            products[stockInput[i]] += Number(stockInput[i+1])
        }
        else {
            products[stockInput[i]] = Number(stockInput[i+1])
        }
    }
    
    for (let i=0; i < orderInput.length; i+=2){
        if (orderInput[i] in products){
            products[orderInput[i]] += Number(orderInput[i+1])
        }
        else {
            products[orderInput[i]] = Number(orderInput[i+1])
        }
    }

    for (let key in products) {
        console.log(`${key} -> ${products[key]}`)
    } 
}

store([
    'Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'
    ],
    [
    'Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30'
    ])