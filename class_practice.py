class Animal(object):
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass



def domain_(url):
    if 'https://www.' in url:
        url_  = url.replace("https://www.", '')
        url_ = url_.split('.')
        return url_[0]
    elif 'http://' in url:
        url_  = url.replace("http://", '')
        url_ = url_.split('.')
        return url_[0]
        
print(domain_("https://www.github.com"))