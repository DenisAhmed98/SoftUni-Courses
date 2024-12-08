function convertToObject(input){
    const objects = JSON.parse(input)
    const keys = Object.keys(objects);

    for (const key of keys) {
        console.log(`${key}: ${objects[key]}`)
    }
}