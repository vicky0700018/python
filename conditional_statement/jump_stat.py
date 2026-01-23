# what is jump stmt ?

# Break and Continue

# => break is a loop control statement used to immediately terminate the loop when a specific condition is met.


# => when break condition will be true , we exit from the loop.


# => when break condition will be true , it stops the execution immediately .


# for i in range(6):
#                     print(i)

# for i in range(10):
#                     if i == 6:
#                                         break
#                     print(i)


# for i in range(10):
#                     if i == 9:
#                                         break
#                     print(i)

# ------------------------------------------- 

# continue 

# for i in range(13):
#                     print(i)



for i in range(13):
                    if i == 8:
                                        break
                    print(i)



# for i in range(13):
#                     if i == 8:
#                                         continue
#                     print(i)



# for i in range(13):
#                     if i == 6:
#                                         continue
#                     print(i)

# output => 0,1,2,3,4,5,7,8,9,10,11,12