#typeasting
var1 = "53"
var2 = "33"
print(int(var1) + int(var2))
print(100 * str(int(var1) + int(var2)))
print(10 * "hellooo  ")

# string slicing
mystr = "Harry"
print(len(mystr))
print(mystr[-1])
print(mystr[:1:1])

# String Functions:

demo = "Aakash is a good boy" 
print(demo.endswith("boy"))
print(demo.count('o'))
print(demo.capitalize())
print(demo.upper())
print(demo.lower())
print(demo.find("is"))
a1=print(demo.replace("good","nice"))