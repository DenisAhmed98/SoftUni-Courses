function city(args){
    const keys = Object.keys(args);

    for (const key of keys) {
        console.log(`${key} -> ${args[key]}`)
    }
}