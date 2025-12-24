# String Methods Practice Examples

# # 1. upper() - Convert string to uppercase
# print("=== 1. upper() ===")
# name = "vicky"
# print(f"Original: {name}")
# print(f"Uppercase: {name.upper()}")
# print()

# # 2. lower() - Convert string to lowercase
# print("=== 2. lower() ===")
# text = "PYTHON PROGRAMMING"
# print(f"Original: {text}")
# print(f"Lowercase: {text.lower()}")
# print()

# # 3. capitalize() - Capitalize first character
# print("=== 3. capitalize() ===")
# sentence = "hello world"
# print(f"Original: {sentence}")
# print(f"Capitalized: {sentence.capitalize()}")
# print()

# # 4. title() - Capitalize first letter of each word
# print("=== 4. title() ===")
# text = "python is awesome"
# print(f"Original: {text}")
# print(f"Title case: {text.title()}")
# print()

# # 5. len() - Get string length
# print("=== 5. len() ===")
# word = "developer"
# print(f"String: {word}")
# print(f"Length: {len(word)}")
# print()

# # 6. count() - Count occurrences of a character/substring
# print("=== 6. count() ===")
# text = "mississippi"
# print(f"String: {text}")
# print(f"Count of 's': {text.count('s')}")
# print(f"Count of 'i': {text.count('i')}")
# print(f"Count of 'p': {text.count('p')}")

# # 7. find() - Find first occurrence of substring
# print("=== 7. find() ===")
# text = "hello world hello"
# print(f"String: {text}")
# print(f"Position of 'world': {text.find('world')}")


# # 8. index() - Similar to find but raises error if not found
# print("=== 8. index() ===")
# text = "python"
# print(f"String: {text}")
# print(f"Index of 'h': {text.index('h')}")
# print(f"Index of 'n': {text.index('n')}")
# print(f"Index of 'y': {text.index('y')}")


# # 9. replace() - Replace substring with another
# print("=== 9. replace() ===")
# text = "I love coding"
# print(f"Original: {text}")
# print(f"Replaced: {text.replace('coding', 'programming')}")
# print(f"Replaced: {text.replace('coding', 'python')}")
# print(f"Replaced: {text.replace('coding', 'devlopment')}")


# # 10. split() - Split string into list
# print("=== 10. split() ===")
# text = "apple banana orange grapes mango peach"
# print(f"Original: {text}")
# print(f"After split: {text.split()}")
# print()

# # 11. strip() - Remove whitespace from both ends
# print("=== 11. strip() ===")
# text = "   hello world   "
# print(f"Original: '{text}'")
# print(f"After strip: '{text.strip()}'")
# print()

# # 12. lstrip() - Remove whitespace from left side
# print("=== 12. lstrip() ===")
# text = "   python   "
# print(f"Original: '{text}'")
# print(f"After lstrip: '{text.lstrip()}'")
# print()

# # 13. rstrip() - Remove whitespace from right side
# print("=== 13. rstrip() ===")
# text = "   vicky kumar   "
# print(f"Original: '{text}'")
# print(f"After rstrip: '{text.rstrip()}'")


# # 14. startswith() - Check if string starts with substring
# print("=== 14. startswith() ===")
# text = "python programming"
# print(f"String: {text}")
# print(f"Starts with 'python': {text.startswith('python')}")
# print(f"Starts with 'java': {text.startswith('java')}")
# print()

# # 15. endswith() - Check if string ends with substring
# print("=== 15. endswith() ===")
# text = "learning.py"
# print(f"String: {text}")
# print(f"Ends with '.py': {text.endswith('.py')}")
# print(f"Ends with '.txt': {text.endswith('.txt')}")
# print()

# # 16. join() - Join list elements with a string
# print("=== 16. join() ===")
# words = ["python", "is", "awesome"]
# print(f"List: {words}")
# print(f"Joined with space: {' '.join(words)}")
# print(f"Joined with dash: {'-'.join(words)}")
# print(f"joined with comma: {','.join(words)}")
# print(f"joined with underscore: {'_'.join(words)}")


# # 17. swapcase() - Swap uppercase to lowercase and vice versa
# print("=== 17. swapcase() ===")
# text = "PyThOn PrOgRamMing"
# print(f"Original: {text}")
# print(f"Swapped: {text.swapcase()}")


# # 18. isdigit() - Check if string contains only digits
# print("=== 18. isdigit() ===")
# print(f"'12345'.isdigit(): {'12345'.isdigit()}")
# print(f"'123abc'.isdigit(): {'123abc'.isdigit()}")
# print(f"'00123'.isdigit(): {'00123'.isdigit()}")

# # 19. isalpha() - Check if string contains only alphabets
# print("=== 19. isalpha() ===")
# print(f"'hello'.isalpha(): {'hello'.isalpha()}")
# print(f"'hello123'.isalpha(): {'hello123'.isalpha()}")
# print(f"'hello world'.isalpha(): {'hello world'.isalpha()}")

# # 20. isalnum() - Check if string contains alphanumeric characters
# print("=== 20. isalnum() ===")
# print(f"'hello123'.isalnum(): {'hello123'.isalnum()}")
# print(f"'hello 123'.isalnum(): {'hello 123'.isalnum()}")
# print()

# # Combined Practice Examples
# print("=== COMBINED PRACTICE ===")

# # Example 1
# email = "  VICKY.KUMAR@GMAIL.COM  "
# clean_email = email.strip().lower()
# print(f"Email processing: {email} => {clean_email}")

# # Example 2
# user_input = "vicky kumar"
# formatted = user_input.title()
# print(f"Format name: {user_input} => {formatted}")

# # Example 3
# csv_data = "apple,banana,orange,grapes"
# fruits = csv_data.split(',')
# print(f"CSV to list: {fruits}")

# # Example 4
# words = ["learning","python", "is", "fun"]
# sentence = " ".join(words)
# print(f"List to sentence: {sentence}")
