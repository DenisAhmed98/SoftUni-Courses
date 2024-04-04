from unittest import TestCase, main
#from UnitTestintg.Exercise.mammal.project.mammal import Mammal
# for Judge
from project.mammal import Mammal

class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Tiger", "Land mammal", "Roar")

    def test_initialization_of_mammal(self):
        self.assertEqual("Tiger", self.mammal.name)
        self.assertEqual("Land mammal",self.mammal.type)
        self.assertEqual("Roar",self.mammal.sound)
        self.assertEqual("animals",self.mammal.get_kingdom())

    def test_make_sound(self):
        self.assertEqual("Tiger makes Roar", self.mammal.make_sound())

    def test_information_of_mammal(self):
        self.assertEqual("Tiger is of type Land mammal", self.mammal.info())

if __name__ == "__main__":
    main()