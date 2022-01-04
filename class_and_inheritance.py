from class_coding import Animal, Book, Vehicle

class Fish(Animal):
    @property
    def size(self):
        return self._size 

Fish1 = Fish('Whale')
Fish1.eat()