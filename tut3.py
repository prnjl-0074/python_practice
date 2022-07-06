#boolean
print(10<9)

#operators
print(2**3)\

#lists list functions
x = ["pj, kj, hj"]
print(x)
y = ["HJ","NJ","J"]
print(y)
num1 = [2,23,11,8,10]
num1.sort()
print(num1)
num1.reverse()
print(num1)
print(max(num1))
print(min(num1))
print(len(num1))
print(num1.count(2))
num1.append(22222)
print(num1)
num1.reverse()
print(num1)

#empty list
num2 =[]
num2.append(44)
num2.append(4)
num2.append(444)
num2.append(404)
print(num2)
num2.insert(3, 440)
print(num2)
num2.remove(4)
print(num2)
num2.pop()
print(num2)
num2 [2] = 55
print(num2)

#other list functions
x = ['laptop', 'pc', 'touchpad', 59]
y = ['mouse', 'keyboard', 'cpu', 95]
x.extend(y)
print(x)
x.clear()
print(x)

#list constructor
list1 = list(("cpu", 25, 85.66, 45j))
print(list1)

if 25 in list1:
    print("yes it does")

