function solve(speed, area){
    const limit_M = 130
    const limit_I = 90
    const limit_C = 50
    const limit_R = 20

    switch(area){
        case "motorway":
            if (speed <= limit_M){
                console.log(`Driving ${speed} km/h in a ${limit_M} zone`)
            }
            else {
                let over_limit = speed - limit_M
                let status
                if (over_limit <= 20) status = 'speeding'
                else if (over_limit <= 40) status = 'excessive speeding'
                else status = 'reckless driving'

                console.log(`The speed is ${over_limit} km/h faster than the allowed speed of ${limit_M} - ${status}`)

            }
            break;

        case "interstate":
            if (speed <= limit_I){
                console.log(`Driving ${speed} km/h in a ${limit_I} zone`)
            }
            else {
                let over_limit = speed - limit_I
                let status
                if (over_limit <= 20) status = 'speeding'
                else if (over_limit <= 40) status = 'excessive speeding'
                else status = 'reckless driving'
    
                console.log(`The speed is ${over_limit} km/h faster than the allowed speed of ${limit_I} - ${status}`)
    
            }
            break;
            
        case "city":
            if (speed <= limit_C){
            console.log(`Driving ${speed} km/h in a ${limit_C} zone`)
            }
            else {
                let over_limit = speed - limit_C
                let status
                if (over_limit <= 20) status = 'speeding'
                else if (over_limit <= 40) status = 'excessive speeding'
                else status = 'reckless driving'
                console.log(`The speed is ${over_limit} km/h faster than the allowed speed of ${limit_C} - ${status}`)    
                }
            break;

        case "residential":
            if (speed <= limit_R){
                console.log(`Driving ${speed} km/h in a ${limit_R} zone`)
            }
            else {
                let over_limit = speed - limit_R
                let status
                if (over_limit <= 20) status = 'speeding'
                else if (over_limit <= 40) status = 'excessive speeding'
                else status = 'reckless driving'
    
                console.log(`The speed is ${over_limit} km/h faster than the allowed speed of ${limit_R} - ${status}`)
    
            }
            break;
    }
}

solve(21, 'residential')