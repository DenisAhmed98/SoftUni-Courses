function convertToObject(input){
    input.forEach(entry => {
        let [town, latitude, longitude] = entry.split(' | ');
        latitude = Number(latitude).toFixed(2)
        longitude  = Number(longitude).toFixed(2)
        let entryObject = {town, latitude, longitude} 
        console.log(entryObject)
    });
}

convertToObject(['Sofia | 42.696552 | 23.32601',
    'Beijing | 39.913818 | 116.363625'])