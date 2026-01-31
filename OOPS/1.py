# oops => object oriented programming language.

# NOte: C language does not support oops.
# but C++, Python, Java, Javascript, Php and all support oops programming.

# there are 4 pillors of oops concept. 

# 1. inheritence
# 2. Polymorphism
# 3. Encapsulation
# 4. Abstraction



# class Room:
#                     num_of_students = 80 
#                     num_of_teachers = 2
#                     no_of_desks = 50
#                     blackboard = 2


# --------------------------------------------- 
# num_of_students = 80 
# print(num_of_students)

# ------------------------------------------------- 


# Local variable => it can be accessed inside only function or class, not outside. 


# global variable => it can be accessed anywhere , inside or outside.

num_of_students = 80  # Global variable 

print(num_of_students) # 80

def my_function():
                    my_name = "Sourabh" # local variable 
                    print(my_name)
                    print("end of function")
my_function()
print(num_of_students)
print(my_name) # it gives error