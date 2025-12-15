# 1. upper() => it is used to convert each and every character in uppercase of any string .

# language = "python"

# print(language.upper())

# 2. lower() => it is used to convert each and every character in lower case of any string.

# language = "PyTHon"

# print(language.lower())

# 3. capitalize() => it converts in upper case (the first character of first word in a sentence .)

# my_sentence = "python is high level programming language"
# print(my_sentence.capitalize())

# 4. len() => it returns the numbers of character in a string.

# name = "Rudra"
# print(len(name))


# 5. index() => it returns the index of any character of any string.
# => make sure it returns the first occurence .

# my_name = "Rudra"
# print(my_name.index("u"))

# 0 1 2 3 4
# R o n n y

# my_name = "Ronny"
# print(my_name.index("n"))

# 6. count() => it returns the count of mentioned character of any string.

# word = "Programming"
# print(word.count("m"))


# 7. find() => it return the index of first occurence of mentioned character of any string.

# my_string = "language"
# print(my_string.find("g"))


# 8. split() => it returns a list with comma seperated. 

# my_sentence = "Tridev is a good guy"
# print(my_sentence.split())

# 9. strip() => it is used to remove the whitespace from any string.

# lstrip(), rstrip()

# my_sentence = "            Tridev is a good guy"
# print(my_sentence)

# print(my_sentence.strip())



# 10. replace() => it is used to replace any specific string. 


# my_sentence = "Tridev is a good guy"
# print(my_sentence.replace("Tridev", "SHivam"))

# 11. startswith() => it returns any boolean , according to the given condition.

# my_name = "Shivam"
# print(my_name.startswith("Sh"))
# print(my_name.startswith("SH"))

# 12. endswith() => it returns any boolean, accordting to the given condition.

# my_name = "Shivam"
# print(my_name.endswith("m"))
# print(my_name.endswith("am"))


# my_name = "Tridev"
# my_name = "Rohit"
# print(my_name)


# beacue string is immutable , it CAN  change entirely only but not specifically .

# my_name = "Tridev"
# print(my_name[2])  # i
# my_name[2]  = "e"
# print(my_name)