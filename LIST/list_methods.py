# List methods :- 

# 1. append() => it is used to add single element at the end of list.

# my_listt = [10,20,30,40,50,60]
# print("before applying any method: ", my_listt)

# my_listt.append(66)
# print("after applying any operation: ", my_listt)

# extend() => it is used to add multiple element at the end of list.

# my_listt = [10,20,30,40,50,60]
# print("before applying any method: ", my_listt)

# my_listt.extend([66,77])
# print("after applying any operation: ", my_listt)


# insert() => it is used to add a single ement at the specified index.


# my_listt = [10,20,30,40,50,60]
# print("before applying any method: ", my_listt)

# my_listt.insert(0,33)
# print("after applying any operation: ", my_listt)



# my_listt = [10,20,30,40,50,60]
# print("before applying any method: ", my_listt)

# my_listt.insert(0,33)
# print("after applying any operation: ", my_listt)


# remove() => it is used to remove the mentioned element .

# my_listt = [10,20,30,40,50,60]
# print("before applying any method: ", my_listt)

# my_listt.remove(30)
# print("after applying any operation: ", my_listt)


# pop() => by default it removes the last index elemnt , otherwise it removes the specified index elemt.

# my_listt = [10,20,30,40,50,60]
# print("before applying any method: ", my_listt)

# my_listt.pop()
# print("after applying any operation: ", my_listt)



# my_listt = [10,20,30,40,50,60]
# print("before applying any method: ", my_listt)

# my_listt.pop(1)
# print("after applying any operation: ", my_listt)


# index() => it returns the index of mentioned element.

# my_listt = [10,20,30,40,50,60]
# print("before applying any method: ", my_listt)
# print(my_listt.index(20))
# print("after applying any operation: ", my_listt)



# my_listt = [10,20,30,40,50,60]
# print("before applying any method: ", my_listt)
# my_listt.index(20)
# print("after applying any operation: ", my_listt)


# my_listt = [10,20,30,20,20,20,40,50,60]
# print("before applying any method: ", my_listt)
# print(my_listt.count(20))
# print("after applying any operation: ", my_listt)

# reverse()

# my_listt = [10,20,30,20,20,20,40,50,60]
# print("before applying any method: ", my_listt)
# my_listt.reverse()
# print("after applying any operation: ", my_listt)

# sorted() => by default it arranges elements in ascending ordr.

# my_listt = [10,20,30,2,20,20,4,50,6]
# print("before applying any method: ", my_listt)
# my_listt.sort()
# print("after applying any operation: ", my_listt)


# descending order 

# my_listt = [10,20,30,2,20,20,4,50,6]
# print("before applying any method: ", my_listt)
# my_listt.sort(reverse=True)
# print("after applying any operation: ", my_listt)

# copy() :-

my_listt = [10,20,30,20,20,20,40,50,60]
print("before applying any method: ", my_listt)

my_listt2 = my_listt.copy()
print("after applying any operation: ", my_listt2)