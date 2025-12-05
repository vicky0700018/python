# Membership operator :-
# => it is used to check the presence of value in a sequence like  list, tuple, string, set, dictionary etc.

Rahul_family = [ 'ravi', 'rahul', 'rohan']

print('rahul'  in Rahul_family)  ##   True

print('Rudra' in Rahul_family)  ## False

# in => it returns true if value is present .

# not in => it returns true if value is not present .




Rahul_family = [ 'ravi', 'rahul', 'rohan']  # list

print('rahul'  in Rahul_family)  ##   True

print('Rudra' in Rahul_family)  ## False 

print('SHivam' not in Rahul_family)  # true

print('ravi' not in Rahul_family)  # False




















































































































































































































































































































































































































































































































































# """
# Membership Operators in Python
# ================================
# Membership operators are used to test if a value exists in a sequence.
# The membership operators are: 'in' and 'not in'
# """

# # 1. Using 'in' with Lists
# print("=" * 50)
# print("1. Using 'in' with Lists")
# print("=" * 50)
# fruits = ["apple", "banana", "orange", "mango"]
# print(f"List: {fruits}")
# print(f"'banana' in fruits: {'banana' in fruits}")
# print(f"'grape' in fruits: {'grape' in fruits}")

# # # 2. Using 'not in' with Lists
# # print("\n" + "=" * 50)
# # print("2. Using 'not in' with Lists")
# # print("=" * 50)
# # fruits = ["apple", "banana", "orange", "mango"]
# # print(f"List: {fruits}")
# # print(f"'grape' not in fruits: {'grape' not in fruits}")
# # print(f"'apple' not in fruits: {'apple' not in fruits}")

# # # 3. Using 'in' with Strings
# # print("\n" + "=" * 50)
# # print("3. Using 'in' with Strings")
# # print("=" * 50)
# # text = "Hello World"
# # print(f"String: '{text}'")
# # print(f"'H' in text: {'H' in text}")
# # print(f"'World' in text: {'World' in text}")
# # print(f"'xyz' in text: {'xyz' in text}")

# # # 4. Using 'not in' with Strings
# # print("\n" + "=" * 50)
# # print("4. Using 'not in' with Strings")
# # print("=" * 50)
# # text = "Hello World"
# # print(f"String: '{text}'")
# # print(f"'xyz' not in text: {'xyz' not in text}")
# # print(f"'Hello' not in text: {'Hello' not in text}")

# # # 5. Using 'in' with Tuples
# # print("\n" + "=" * 50)
# # print("5. Using 'in' with Tuples")
# # print("=" * 50)
# # numbers = (10, 20, 30, 40, 50)
# # print(f"Tuple: {numbers}")
# # print(f"30 in numbers: {30 in numbers}")
# # print(f"100 in numbers: {100 in numbers}")

# # # 6. Using 'in' with Sets
# # print("\n" + "=" * 50)
# # print("6. Using 'in' with Sets")
# # print("=" * 50)
# # colors = {"red", "green", "blue", "yellow"}
# # print(f"Set: {colors}")
# # print(f"'red' in colors: {'red' in colors}")
# # print(f"'purple' in colors: {'purple' in colors}")

# # # 7. Using 'in' with Dictionaries
# # print("\n" + "=" * 50)
# # print("7. Using 'in' with Dictionaries (checks keys)")
# # print("=" * 50)
# # person = {"name": "John", "age": 30, "city": "New York"}
# # print(f"Dictionary: {person}")
# # print(f"'name' in person: {'name' in person}")
# # print(f"'John' in person: {'John' in person}")  # Checks keys, not values
# # print(f"'age' in person: {'age' in person}")

# # # 8. Using 'in' with Dictionary Values
# # print("\n" + "=" * 50)
# # print("8. Using 'in' with Dictionary Values")
# # print("=" * 50)
# # person = {"name": "John", "age": 30, "city": "New York"}
# # print(f"Dictionary: {person}")
# # print(f"'John' in person.values(): {'John' in person.values()}")
# # print(f"30 in person.values(): {30 in person.values()}")
# # print(f"'xyz' in person.values(): {'xyz' in person.values()}")

# # # 9. Using 'in' with Dictionary Keys (explicit)
# # print("\n" + "=" * 50)
# # print("9. Using 'in' with Dictionary Keys (explicit)")
# # print("=" * 50)
# # person = {"name": "John", "age": 30, "city": "New York"}
# # print(f"Dictionary: {person}")
# # print(f"'name' in person.keys(): {'name' in person.keys()}")
# # print(f"'country' in person.keys(): {'country' in person.keys()}")

# # # 10. Practical Example: User Validation
# # print("\n" + "=" * 50)
# # print("10. Practical Example: User Validation")
# # print("=" * 50)
# # registered_users = ["alice", "bob", "charlie", "david"]
# # username = "alice"
# # if username in registered_users:
# #     print(f"✓ '{username}' is a registered user")
# # else:
# #     print(f"✗ '{username}' is not a registered user")

# # username = "eve"
# # if username not in registered_users:
# #     print(f"✗ '{username}' is not a registered user")
# # else:
# #     print(f"✓ '{username}' is a registered user")

# # # 11. Practical Example: Vowel Checker
# # print("\n" + "=" * 50)
# # print("11. Practical Example: Vowel Checker")
# # print("=" * 50)
# # vowels = "aeiouAEIOU"
# # word = "Python"
# # for char in word:
# #     if char in vowels:
# #         print(f"'{char}' is a vowel")
# #     else:
# #         print(f"'{char}' is not a vowel")

# # # 12. Practical Example: Email Domain Check
# # print("\n" + "=" * 50)
# # print("12. Practical Example: Email Domain Check")
# # print("=" * 50)
# # allowed_domains = ["gmail.com", "yahoo.com", "outlook.com"]
# # email = "user@gmail.com"
# # domain = email.split("@")[1]
# # if domain in allowed_domains:
# #     print(f"✓ Email domain '{domain}' is allowed")
# # else:
# #     print(f"✗ Email domain '{domain}' is not allowed")

# # # Summary Table
# # print("\n" + "=" * 50)
# # print("SUMMARY TABLE")
# # print("=" * 50)
# # print("Operator | Description                        | Example")
# # print("-" * 60)
# # print("in       | Returns True if value exists       | 'a' in 'abc'")
# # print("not in   | Returns True if value doesn't exist| 'd' not in 'abc'")
# # print()
# # print("Works with: Lists, Tuples, Sets, Strings, Dictionaries")
