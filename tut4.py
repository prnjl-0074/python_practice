#tuples
tupl1 = ("bottle", "lunch", 45, 88, 99)
print(tupl1)
print(tupl1[-2:-1])
print(tupl1[0])

if "lunch" in tupl1:
    print("yes it does")

for x in tupl1:
    print(tupl1)

tupl2 = list(tupl1)
tupl2.append("break")
print(tupl2)

#unpack in tuple
(red, pink, yellow, *blue) = tupl1
print(red)
print(pink)
print(yellow)
print(blue)

tupl3 = ("appy", "coffee", "coffee", "coldc")
i = 0
while i < len(tupl3):
  print(tupl3[i])
  i = i + 1

tupl3.count('coffee')


#set
set1 = {"appy","coffee", "coffee", "potato"}
print(set1)

for x in set1:
    print(set1)

print("coffee" in set1)
set1.add("coffee")
print(set1)
set1.remove("appy")
print(set1)

y = set1.pop()
print(y)
print(set1)

set2 = {"a", "b" , "c"}
set3 = {1, 2, 3}

set4 = set2.union(set3)
print(set3)

#dictionary
dict1 = {
  "name": "pranjal",
  "surname": "jain",
  "year": 2000
}
print(dict1)
z = dict1["name"]
print(z)

k = dict1.keys()
print(k)

dict1["year"] = 2001
print(dict1)
dict1["name"] = "PJ"
print(dict1)

for x, y in dict1.items():
    print(x,y)

dict1.popitem()
print(dict1)

del dict1
print(dict1)