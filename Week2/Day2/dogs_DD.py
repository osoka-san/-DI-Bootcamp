from HW_EX_XP_W1_D2 import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = ", ".join([dog.name for dog in args])
        print(f"{self.name} and {dog_names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained enough to do a trick.")

dog1 = PetDog("Alpha", 5, 30)
dog2 = PetDog("Budd", 3, 20)
dog3 = PetDog("Rex", 4, 25)

dog1.train()

dog1.play(dog2, dog3)

dog1.do_a_trick()

dog2.do_a_trick()