# Logical Operators :-

# => it is used to combile two or more conditions.
# => it always returns boolean value ( True / False ).

# types of logical operators :-
# 1. and operator :--
# 2. or operator :--
# 3. not operator :--


# a = True
# b = False

# print( a and b )  
# print( a or b )




# in c language , we use symbol for logical operators
# && operator :-  and operator :-
# || operator :-  or operator :-
# ! operator :-  not operator :-



# a = 10 
# b = 20 

# print("first condition:", a > b and b > a )
# print("second condition:", a == b and a < b)
# print( "third condition:", a < b or  b < a)





# a = True 
# b = False
# print(not a)  # false 
# print(not b)  # true



x = 22
y = 11

print("condition check: ", x < y)  # false
print("after not operator: ", not (x < y))  # True

print("after check multiple condition: ",x < y and x > y)  ## False 

print(not(x < y and x > y)) ## True