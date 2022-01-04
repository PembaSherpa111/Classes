from class_coding import Animal, Book, Vehicle

class Fish(Animal):
    """Fish Class"""

    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self,new_weight):
        self._weight = new_weight
    
    @weight.deleter
    def weight(self):
        del self._weight
    
    def move(self):
        print(f'{self._name} is swimming')

class Snake(Animal):
    """Snake Class"""

    @property
    def venoumous(self):
        return self._venoumous
    
    @venoumous.setter
    def venoumous(self,new_venoumous):
        self._venoumous = new_venoumous
    
    @venoumous.deleter
    def v(self):
        del self._venoumous
    
    def move(self):
        print(f'{self._name} is slithering')

class Person(Animal):
    """Person Class"""

    @property
    def age(self):
        return self._age
    @property
    def gender(self):
        return self._gender

    @age.setter
    def age(self,new_age):
        self._age = new_age
    @gender.setter
    def gender(self,new_gender):
        self._gender = new_gender
    
    @age.deleter
    def age(self):
        del self._age
    @gender.deleter
    def gender(self):
        del self._gender
    
    def move(self):
        print(f'{self._name} is walking')

class Textbook(Book):
    """Textbook Class"""

    @property
    def subject(self):
        return self._subject
    
    @subject.setter
    def subject(self,new_subject):
        self._subject = new_subject
    
    @subject.deleter
    def subject(self):
        del self._subject

class Addressbook(Book):
    """Textbook Class"""

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self,new_type):
        self._type = new_type
    
    @type.deleter
    def type(self):
        del self._type

class Car(Vehicle):
    """Car Class"""

    @property 
    def body_type(self):
        return self._body_type
    @property 
    def model(self):
        return self._model
    @property
    def year(self):
        return self._year
    
    @body_type.setter
    def body_type(self,new_body_type):
        self._body_type = new_body_type
    @model.setter
    def model(self,new_model):
        self._model = new_model
    @year.setter
    def year(self,new_year):
        self._year = new_year
    
    @body_type.deleter
    def body_type(self):
        del self._body_type
    @model.deleter
    def model(self):
        del self._model
    @year.deleter
    def year(self):
        del self._year

class Bicycle(Vehicle):
    """Bicycle Class"""

    @property
    def geared(self):
        return self._geared
    
    @geared.setter
    def geared(self,new_geared):
        self._geared = new_geared
    
    @geared.deleter
    def geared(self):
        del self._geared

class Boat(Vehicle):
    """Boat Class"""

    @property
    def boat_type(self):
        return self._boat_type
    
    @boat_type.setter
    def boat_type(self,new_boat_type):
        self._boat_type = new_boat_type
    
    @boat_type.deleter
    def boat_type(self):
        del self._boat_type

class Hot_Air_Balloon(Vehicle):
    """Hot Air Balloon Class"""

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self,new_capacity):
        self._capacity = new_capacity
    
    @capacity.deleter
    def capacity(self):
        del self._capacity  