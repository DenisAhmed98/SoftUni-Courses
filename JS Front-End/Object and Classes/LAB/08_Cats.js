function solve(input){
    let cats = [];

    class Cat {
        constructor (name, age) {
            this.name = name;
            this.age = age;
        }
    
        meow(){
            console.log(`${this.name}, age ${this.age} says Meow`);
        }
    }

    for (let i = 0; i < input.length; i++){
        let catInput = input[i].split(' ');
        cats.push(new Cat(catInput[0],catInput[1]))
    }

    for (const cat of cats){
        cat.meow()
    }
}


solve(['Mellow 2', 'Tom 5'])