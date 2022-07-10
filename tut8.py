#Python List Exercises
#Python program to change first and last elements in a list
list1 = ["pen", "book", "pencil", "ink pen", "poster colors"]
print(list1)

list1[0] = "gel pen"
list1[1] = "water colors"
print(list1)


#Python program to interchange first and last elements in a list
list1[0],list1[4] = list1[4],list1[0]
print(list1)


#Python program to swap two elements in a list
list1[0],list1[1] = list1[1],list1[0]
print(list1)


#Python | Ways to find length of list
print(len(list1))


#Maximum of two numbers in Python
a = 0.2
b = 0.02
maximum = max(a,b)
print(maximum)


#Minimum of two numbers in Python
a = 0.2
b = 0.02
minimum = min(a,b)
print(minimum)


#Python Ways to check if element exists in list
if "poster colors" in list1:
    print("yes")

#Reversing a List
list1.reverse()
print(list1)
#Cloning or Copying a list
list2 = list1.copy()
print(list2)
#Count occurrences of an element in a list
print(list1.count("pencil"))

#Python Program to find sum and average of List
num_list = [1,2,3,4,5,6,7]
count = 0

for i in num_list:
    count+= i

avg = count/len(num_list)
print("sum = ", count)
print("average = ", avg)

#Python program to find smallest number in a list
print(min(num_list))
#Python program to find largest number in a list
print(max(num_list))

#Python program to find second largest number in a list
num_list.sort()
print(num_list[-2])

#Python program to print even numbers in a list
print("\n")
for num in num_list:

    if num % 2 == 0 :
        print(num,end=" \n")

#Python program to print odd numbers in a List
print("\n")
for num in num_list:

    if num % 2 != 0 :
        print(num,end=" \n")

#Python program to print all even numbers in a range
print("\n")
for i in range(11,21):

    if i % 2 == 0:
        print(i)

#Python program to print all odd numbers in a range
print("\n")
for i in range(11,21):

    if i % 2 != 0:
        print(i)

#Python program to count Even and Odd numbers in a List
num_list = [1,2,3,44,5,6,7]
print("\n")

even_count, odd_count = 0, 0

for nums in num_list:


    if nums % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

print("even no's are- ", even_count)
print("odd no's are- ", odd_count)

#Python program to print positive numbers in a list
print("\n")
inte_list = [55,-8,-6,74,25]

for pos in inte_list:

    if pos >= 0:
        print(pos)

#Python program to print negative numbers in a list
print("\n")
inte_list = [55,-8,-6,74,25]

for pos in inte_list:

    if pos < 0:
        print(pos)

#Python program to print all positive numbers in a range
print("these are ev\n")

for pos in range(-4,5):

    if pos >= 0:
        print(pos)

#Python program to print all negative numbers in a range
print("these are ne\n")
for pos in range(-3,5):

    if pos < 0:
        print(pos)


#Python program to count positive and negative numbers in a list
print("\n")
pos_count, neg_count = 0, 0

for k in inte_list:
    
    if k >= 0:
        pos_count += 1
    else:
        neg_count += 1

print("positive nums are = ",pos_count)
print("negative nums are = ",neg_count)


#Remove multiple elements from a list in Python
list_e = ["pen", "book",66, "pencil",55]
print("\n")
list_e.remove("pen")
list_e.remove(66)
print(list_e)

#Remove empty tuples from a list
print("\n")
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
        ('krishna', 'akbar', '45'), ('',''),()]

def Remove(tuples):
    for i in tuples:
        if(len(i)==0):
            tuples.remove(i)
    return tuples

print(Remove(tuples))


#Program to print duplicates from a list of integers
dupss = [2,3,6,6,4,7,88,55,3,88,99]
print("\n")
def duplicate(dupss):
    return list(set([y for y in dupss if dupss.count(y) > 1]))

if __name__ == '__main__':
    print(duplicate(dupss))

