# assignment operator :-


#+=  ( add and  assign )
#-=  ( subtract and assign )
# *=  ( multiply and assign )
# /=  ( divide and assign )
# %=  ( modulus and assign )
# //= ( floor divide and assign )
# **= ( exponent and assign )



# a  = 10
# b = 23

# print( a + b)



# a  = 10

# b = 23

# a = a + b     # OR a = 10 + 23  => a = 33 

# print("the value of a is : ", a)



# Time Complexity :-

# => time taken by any code to run  is called time complexity.



# Space Complexity :-
# => space taken by any code to run is called space complexity.


# +=  ( add and  assign )

# a  = 10

# b = 23

# a += b     # OR a = a + b  => a = 10 + 23  => a = 33

# print("the value of a is : ", a)

# Note : a = a + b     and     a += b    both are same thing




# a  = 33

# b = 23

# a = a - b     # OR a = a - b  => a = 33 - 23  => a = 10

# print("the value of a is : ", a)


# # -=  ( subtract and assign )

# a  = 33

# b = 23

# a -= b     # OR a = a - b  => a = 33 - 23  => a = 10

# print("the value of a is : ", a)

# Bus A => it takes 2 hours to reach the metro station.

# Bus B => it takes only 1 hour to reach the metro station.



# a = a + b   => it takes more time to run.

# a += b      => it takes less time to run.




































































































































































































































































































































































































# """
# Assignment Operators in Python
# ================================
# Assignment operators are used to assign values to variables.
# """

# # 1. Simple Assignment (=)
# print("=" * 50)
# print("1. Simple Assignment (=)")
# print("=" * 50)
# x = 10
# y = 20
# print(f"x = {x}, y = {y}")

# # 2. Add and Assign (+=)
# print("\n" + "=" * 50)
# print("2. Add and Assign (+=)")
# print("=" * 50)
# x = 10
# x += 5  # Equivalent to: x = x + 5
# print(f"x += 5 => x = {x}")

# # 3. Subtract and Assign (-=)
# print("\n" + "=" * 50)
# print("3. Subtract and Assign (-=)")
# print("=" * 50)
# x = 20
# x -= 5  # Equivalent to: x = x - 5
# print(f"x -= 5 => x = {x}")

# # 4. Multiply and Assign (*=)
# print("\n" + "=" * 50)
# print("4. Multiply and Assign (*=)")
# print("=" * 50)
# x = 10
# x *= 3  # Equivalent to: x = x * 3
# print(f"x *= 3 => x = {x}")

# # 5. Divide and Assign (/=)
# print("\n" + "=" * 50)
# print("5. Divide and Assign (/=)")
# print("=" * 50)
# x = 30
# x /= 5  # Equivalent to: x = x / 5
# print(f"x /= 5 => x = {x}")

# # 6. Floor Divide and Assign (//=)
# print("\n" + "=" * 50)
# print("6. Floor Divide and Assign (//=)")
# print("=" * 50)
# x = 30
# x //= 4  # Equivalent to: x = x // 4
# print(f"x //= 4 => x = {x}")

# # 7. Modulus and Assign (%=)
# print("\n" + "=" * 50)
# print("7. Modulus and Assign (%=)")
# print("=" * 50)
# x = 25
# x %= 7  # Equivalent to: x = x % 7
# print(f"x %= 7 => x = {x}")

# # 8. Exponentiation and Assign (**=)
# print("\n" + "=" * 50)
# print("8. Exponentiation and Assign (**=)")
# print("=" * 50)
# x = 2
# x **= 5  # Equivalent to: x = x ** 5
# print(f"x **= 5 => x = {x}")

# # # 9. Bitwise AND and Assign (&=)
# # print("\n" + "=" * 50)
# # print("9. Bitwise AND and Assign (&=)")
# # print("=" * 50)
# # x = 12  # Binary: 1100
# # x &= 10  # Binary: 1010
# # print(f"x &= 10 => x = {x}")

# # # 10. Bitwise OR and Assign (|=)
# # print("\n" + "=" * 50)
# # print("10. Bitwise OR and Assign (|=)")
# # print("=" * 50)
# # x = 12  # Binary: 1100
# # x |= 10  # Binary: 1010
# # print(f"x |= 10 => x = {x}")

# # # 11. Bitwise XOR and Assign (^=)
# # print("\n" + "=" * 50)
# # print("11. Bitwise XOR and Assign (^=)")
# # print("=" * 50)
# # x = 12  # Binary: 1100
# # x ^= 10  # Binary: 1010
# # print(f"x ^= 10 => x = {x}")

# # # 12. Bitwise Right Shift and Assign (>>=)
# # print("\n" + "=" * 50)
# # print("12. Bitwise Right Shift and Assign (>>=)")
# # print("=" * 50)
# # x = 12
# # x >>= 2
# # print(f"x >>= 2 => x = {x}")

# # # 13. Bitwise Left Shift and Assign (<<=)
# # print("\n" + "=" * 50)
# # print("13. Bitwise Left Shift and Assign (<<=)")
# # print("=" * 50)
# # x = 5
# # x <<= 2
# # print(f"x <<= 2 => x = {x}")

# # # Summary Table
# # print("\n" + "=" * 50)
# # print("SUMMARY TABLE")
# # print("=" * 50)
# # print("Operator | Description              | Example")
# # print("-" * 50)
# # print("=        | Assign                   | x = 5")
# # print("+=       | Add and assign           | x += 5 (x = x + 5)")
# # print("-=       | Subtract and assign      | x -= 5 (x = x - 5)")
# # print("*=       | Multiply and assign      | x *= 5 (x = x * 5)")
# # print("/=       | Divide and assign        | x /= 5 (x = x / 5)")
# # print("//=      | Floor divide and assign  | x //= 5 (x = x // 5)")
# # print("%=       | Modulus and assign       | x %= 5 (x = x % 5)")
# # print("**=      | Exponent and assign      | x **= 5 (x = x ** 5)")
# # print("&=       | Bitwise AND and assign   | x &= 5 (x = x & 5)")
# # print("|=       | Bitwise OR and assign    | x |= 5 (x = x | 5)")
# # print("^=       | Bitwise XOR and assign   | x ^= 5 (x = x ^ 5)")
# # print(">>=      | Right shift and assign   | x >>= 5 (x = x >> 5)")
# # print("<<=      | Left shift and assign    | x <<= 5 (x = x << 5)")