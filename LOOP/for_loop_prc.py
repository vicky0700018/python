# # ===== FOR LOOP PRACTICE =====

# # 1. Simple loop - Print numbers 1 to 5
# print("=== Example 1: Simple Loop ===")
# for i in range(0, 6):
#     print(i)
#     print("Hello,world!")

# # 2. Loop through a list
# print("\n=== Example 2: Loop through List ===")
# fruits = ["apple", "banana", "cherry", "date"]
# for fruit in fruits:
#     print(f"Fruit: {fruit}")
#     print("I love fruits!")

# # 3. Loop with index
# print("\n=== Example 3: Loop with Index ===")
# colors = ["red", "green", "blue", "yellow"]
# for index, color in enumerate(colors):
#     print(f"{index}: {color}")
#     print("Colors are beautiful!")
    

# # 4. Loop through string
# print("\n=== Example 4: Loop through String ===")
# word = "PYTHON"
# for letter in word:
#     print(letter)
#     print("Learning loops!")


# # 5. Sum of numbers
# print("\n=== Example 5: Sum of Numbers ===")
# total = 0
# for num in range(1, 11):
#     total += num
# print(f"Sum of 1 to 10: {total}")

# # 6. Multiplication table
# print("\n=== Example 6: Multiplication Table ===")
# num = 5
# for i in range(1, 11):
#     print(f"{num} × {i} = {num * i}")

# # 7. Nested loops - Pattern
# print("\n=== Example 7: Nested Loops - Pattern ===")
# for i in range(1, 4):
#     for j in range(1, 4):
#         print("*", end=" ")
#     print()

# # 8. Odd numbers from 1 to 20
# print("\n=== Example 8: Odd Numbers ===")
# for num in range(1, 21):
#     if num % 2 != 0:
#         print(num, end=" ")


# # 9. Count occurrences
# print("\n=== Example 9: Count Occurrences ===")
# numbers = [1, 2, 3, 2, 4, 2, 5, 2, 5, 3, 4, 2]
# count = 0
# for num in numbers:
#     if num == 2:
#         count += 1
# print(f"Number 2 appears {count} times")
# print(f"Number 3 appears {numbers.count(3)} times (using count method)")
# print(f"Number 4 appears {numbers.count(4)} times (using count method)")
# print(f"Number 5 appears {numbers.count(5)} times (using count method)")

# 10. Break and Continue
print("\n=== Example 10: Break and Continue ===")
for i in range(1, 11):
    if i == 5:
        continue  # Skip 5
    if i == 8:
        break  # Stop at 8
    print(i, end=" ")
print()
