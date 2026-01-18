# BREAK Example
break_num = int(input("Enter a number for break: "))

for i in range(6):
    if i == break_num:
        break
    print("Break loop:", i)



# CONTINUE Example

my_num = int(input("Enter a number for continue: "))

for i in range(6):
    if i == my_num:
        continue
    print("Continue loop:", i)



# IF Example
age = int(input("Enter your age (if example): "))

if age >= 18:
    print("You are eligible to vote")



# IF ELSE Example
age = int(input("Enter your age (if-else example): "))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")



# IF ELIF ELSE Example

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("First division")
elif marks >= 60:
    print("Second division")
else:
    print("Third division")


# NESTED IF Example
age = int(input("Enter your age (nested if): "))
citizen = input("Enter your citizenship: ")

if age >= 18:
    if citizen == "Indian":
        print("You are eligible to vote")
    else:
        print("Only Indian citizens can vote")
else:
    print("You are underage")
