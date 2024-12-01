function solve(sentence){
    console.log(sentence.match(/[A-Z][a-z]*/g).join(', '))
}

solve('SplitMeIfYouCanHaHaYouCantOrYouCa')
solve('HoldTheDoor')
solve('ThisIsSoAnnoyingToDo')
