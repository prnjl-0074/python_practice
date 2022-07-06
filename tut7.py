#array
cars = ["Ford", "Volvo", "BMW"]
print(cars)

#class
#init
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("PJ", 22)

print(p1.name)
print(p1.age)

#objects
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def func1(self):
    print("Hello, your name is? " + self.name)

p1 = Person("pranjal", 22)
p1.func1()
