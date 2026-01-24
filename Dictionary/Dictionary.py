# Dictionary 


# => it stores data in Key value pair format. 
# => it is also unordered , that means , it doest not support indexing. 
# => Key must be unique. 
# => it is Mutable . but we can change only value not Key . 



# dictionaryyy = { 
#                     "name" : "Rudra",
#                     "roll" : 121,
#                     "email" : "rudra@gmail.com"
# }

# print(dictionaryyy)

# print(dictionaryyy['name'])

# ---------------------------------------------------------------------- 

# methods 

# 1. key()
# 2. values()
# 3. items()
# 4. get()
# 5. update()
# 6. pop()
# 7. popitem()
# 8. clear()


# dictionaryyy = { 
#                     "name" : "Rudra",  # here, name is key and Rudra is Value
#                     "roll" : 121,
#                     "email" : "rudra@gmail.com"
# }

# print(dictionaryyy)

# print(dictionaryyy['name'])
# print(dictionaryyy.get('name'))




# dictionaryyy = { 
#                     "name" : "Rudra",  # here, name is key and Rudra is Value
#                     "roll" : 121,
#                     "email" : "rudra@gmail.com"
# }

# print(dictionaryyy)

# dictionaryyy.update({"city": "Pune"})

# print(dictionaryyy)







dictionaryyy = { 
                    "name" : "Rudra",  # here, name is key and Rudra is Value
                    "roll" : 121,
                    "email" : "rudra@gmail.com"
}

print(dictionaryyy)

print(dictionaryyy.keys())
print(dictionaryyy.values())

print(dictionaryyy.items())



# please explore  pop and popitem , clear 
