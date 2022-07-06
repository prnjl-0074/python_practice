#functions

def func1(f1):
    print(f1 + " hello")
func1("pranjal")

def funct_2(*child):
  print("The eldest child is " + child[1])

funct_2("pranjal", "kashish", "kavya")

def func3(food):
  for x in food:
    print(x)

dishes = ["chowmien", "paneer chilli", "cherry blast"]

func3(dishes)

def func3():
  pass



#lambda
x = lambda a : a + 10
print(x(5))







