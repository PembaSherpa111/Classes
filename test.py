from class_coding import Animal, Book, Vehicle
from class_and_inheritance import Fish, Snake, Person, Car

print('\n=================\n')

Animal1 = Animal('Tiger')
print(Animal1.name)
Animal1.name = 'Lion'
print(Animal1.name)
Animal1.move()
Animal1.eat()

print('\n=================\n')

Book1 = Book("Harry Potter and the Philosopher's Stone","J Rowling")
print(Book1.title)
Book1.author = 'J. K. Rowling'
print(Book1.author)
Book1.publisher = "Bloomsbury (UK)"
Book1.published_date = "26 June 1997"
print(Book1)

print('\n=================\n')

Vehicle1 = Vehicle('','')
print(Vehicle1)
Vehicle1.type = 'car'
Vehicle1.brand = 'Honda'
print(Vehicle1)
Vehicle1.move()    

print('\n=================\n')

Fish1 = Fish('Tuna')
Fish1.move()

print('\n=================\n')

Snake1 = Snake('Cobra')
Snake1.move()

print('\n=================\n')
Person1 = Person('Jerry')
Person1.move()

print('\n=================\n')
Car1 = Car('sedan', 'Honda')
print(Car1.type)

