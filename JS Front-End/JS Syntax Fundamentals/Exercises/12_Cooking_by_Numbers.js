function solve(num, par1,par2,par3,par4,par5){
    number = Number(num)
    commands = [par1,par2,par3,par4,par5]
    for (i=0; i<5; i++){
        if(commands[i] == 'chop') number /= 2;
        else if(commands[i] == 'dice') number = Math.sqrt(number);
        else if(commands[i] == 'spice') number += 1;
        else if(commands[i] == 'bake') number *= 3;
        else if(commands[i] == 'fillet') number -= (number*0.2);
        
        console.log(number)
    }   
}

solve('9', 'dice', 'spice', 'chop', 'bake', 'fillet')