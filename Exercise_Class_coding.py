class Animal:
    """Animal Class"""
    def __init__(self,name):
        self._name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,new_name):
        self._name = new_name
    
    @name.deleter
    def name(self):
        del self._name

    def move(self):
        print(f'{self._name} is walking')

class Book:
    """"Book Class"""
    def __init__(self,title, author, publisher, published_date):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._published_date = published_date

    def __str__(self):
        return (f"title: {self._title}, author: {self._author}, publisher: {self._publisher}, published date: {self._published_date}")

    @property
    def title(self):
        return self._title
    @property    
    def author(self):
        return self._author
    @property
    def publisher(self):
        return self._publisher
    @property
    def published_date(self):
        return self._published_date

    @title.setter
    def title(self,new_title):
        self._title = new_title
    @author.setter
    def author(self,new_author):
        self._author = new_author
    @publisher.setter
    def publisher(self,new_publisher):
        self._publisher = new_publisher
    @published_date.setter
    def published_date(self,new_published_date):
        self._published_date = new_published_date

class Vehicle:
    """Vehicle Class"""
    def __init__(self,type,brand):
        self._type = type
        self._brand = brand
    
    def __str__(self):
        return (f"type: {self._type}, brand: {self._brand}")
    
    @property
    def type(self):
        return self._type
    @property
    def brand(self):
        return self._brand
    
    @type.setter
    def type(self,new_type):
        self._type = new_type
    @brand.setter
    def brand(self,new_brand):
        self._brand = new_brand
    
    def move(self):
        print(f'{self._type} is moving')


print('\n=================\n')

Animal1 = Animal('Tiger')
print(Animal1.name)
Animal1.name = 'Lion'
print(Animal1.name)
Animal1.move()

print('\n=================\n')

Book1 = Book("Harry Potter and the Philosopher's Stone","J Rowling","Bloomsbury (UK)","26 June 1997")
print(Book1.title)
Book1.author = 'J. K. Rowling'
print(Book1.author)
print(Book1)

print('\n=================\n')

Vehicle1 = Vehicle('','')
print(Vehicle1)
Vehicle1.type = 'car'
Vehicle1.brand = 'Honda'
print(Vehicle1)
Vehicle1.move()    
