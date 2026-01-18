# my_number = int(input("enter any number:  "))

# if my_number >= 70:
#                     print("yes! you are the first one")


# if ROhit reached the clg on the time:
#                     print("ROhit can attend all classes")

# ----------------------------- 
# if ROhit reached the clg on the time:
#                     print("ROhit can attend all classes")

# else:
#                     print("ROhit can't attend all the classes")

# -------------------------------- 
# my_number = int(input("enter any number:  "))

# if my_number >= 60:
#                     print("you will be the first one")
# else:
#                     print("You will not be the first one")


# Conclusion : 

# 1. whenever we have to handle only one conditon , we should use if statement.

# 2. whenever we have to handle two condition , we should use if , else statement . 

# 3. whenever we have to handle more than 2 conditions , we should use if elif statement.

# 4. whenever we have to check any condition inside any another condition , in that case only we should prefer Nested if statement.

# ------------------------------------------- 
# if ROhit reached the clg on the time:
#                     print("ROhit can attend all classes")

# else:
#                     print("ROhit can't attend all the classes")


# ----------------------------------------- 


# if ROhit reached the clg on the time:
#                     print("ROhit can attend all classes")

# elif ROhit reached the clg after the lunch:
#                     print("rohit can attend rest of classes.")
# else:
#                     print("ROhit can't attend all the classes")

# ----------------------------------------- 

# my_number = int(input("enter any number:  "))

# if my_number >= 60:
#                     print("you will be the first one")

# elif my_number >= 50:
#                     print("YOu will be the second one")

# elif my_number >= 30:
#                     print("You will be the third one")

# else:
#                     print("You will be failed")


# ----------------------------------------------- 

# Nested if statement 

# => BOx inside another box called Nested box. 


# politics 

# apka Chhatt leke apko Kambal batna 

# write a program to check a person is eligible or not to vote in Bihar

resident = input("enter your residency:")

if resident == "Bihar":

             age = int(input("Hii! please enter your age: "))
             if age >= 18:
                    print("you are eligible to vote in Bihar")
             else:
                    print("sorry, YOu are underage")


else:
                    print("YOu are not eligible to vote in Bihar")