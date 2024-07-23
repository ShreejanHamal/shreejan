#declare the list
list = [1,2,"shreejan",5]
list1=[1,2,2,3,45,56,7,7,8,9,5]
print(list)
print(list[2])
print(list[0])
#here in list[0:2] 0 is index and 2 is length 
print(list[0:2])
print(list[0:2:1])

#list.append() is a function to add odj at the end of the list we can only add one data at a time
list.append("kabin")
print(list)

#list1.insert(index,value) is a function that add obj at the desire index of lsit 
list1.insert(2,45)
print(list1)

#list.extend() is a function to add odj at the end of the list we can add multiple data
list.extend([30,31,32,33])
print(list)

#this function replaces the value of  given index
list[5]=10001
print(list)

#list1.sort() is a function to sort numbers in asscending order 
list1.sort()
print(list1)

# list.remove() removes the data in list
list.remove(1)
print(list)

#list.pop() removes the last element of the list by default
list.pop()
print(list.pop()) #it print the element that is removed from the list
print(list)
# we can give index to remove to delete certain elemet in index
list1.pop(2)
print(list1.pop(2))
print(list1)

