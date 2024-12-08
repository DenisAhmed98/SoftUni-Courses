function meetings(input){
    let meetings = {};

    for (let line of input){
        let tokens = line.split(' ');
        if (Object.keys(meetings).includes(tokens[0])) {
            console.log(`Conflict on ${tokens[0]}!`)
        }
        else {
            meetings[tokens[0]] = tokens[1];
            console.log(`Scheduled for ${tokens[0]}`)
        } 
    }

    for (let key in meetings) {
        console.log(`${key} -> ${meetings[key]}`)
    }
}