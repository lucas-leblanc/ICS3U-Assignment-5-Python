# Created by Lucas LeBlanc
# This program tells you the smallest and biggest numbers inputted

list1 = []

# asking number of integers to put in list
num = int(input("Enter number of integers in list: "))
 
# iterating till num to append integers in list
for i in range(1, num + 1):
    ele= int(input("Enter integers: "))
    list1.append(ele)
# iterating till num to append integers in list
for i in range(1, num + 1):

    list1.append(ele)
# print maximum element
print("The biggest integer is:", max(list1))
# print maximum integer
print("The smallest integer is:", min(list1))
list1 = []

print("\nDone.")
