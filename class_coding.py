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
        print(f'{self._name} is moving')
    
    def eat(self):
        print(f'{self._name} is eating')

class Book:
    """"Book Class"""
    def __init__(self,title, author):
        self._title = title
        self._author = author

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