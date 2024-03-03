from animal import Animal
from reptile import Reptile
from mammal import Mammal
from lizard import Lizard
from snake import Snake
from gorilla import Gorilla
from bear import Bear

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
