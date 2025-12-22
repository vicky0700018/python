# p   r   o   g   r   a   m   m   i   n   g
# -11-10 -9  -8  -7  -6  -5  -4  -3  -2  -1

# word = "programming"
# print(word[-1])  # g

# print(word[-5]) # m

# print(word[-11 : -5]) # p   r   o   g   r   a


# starting point => -11
# ending point => -5 (excluded)

# ------------------------------------------------------------




# p   r   o   g   r   a   m   m   i   n   g
# -11-10 -9  -8  -7  -6  -5  -4  -3  -2  -1

# word = "programming"


# print(word[-11 : -2 ])  # p   r   o   g   r   a   m   m   i 

# print(word[-11 : -2 : 2]) # p o r m i

# starting point => -11
# ending point =>  -2 (excluded)
# Gap (N-1) => 2 , 2 - 1 => 1 , we have to skipp 1 element .



# --------------------------------------------- 


# p   r   o   g   r   a   m   m   i   n   g
# -11-10 -9  -8  -7  -6  -5  -4  -3  -2  -1


# 0 1 2 3 4 5 6 7 8 9 10
# P r o g r a m m i n g


word = "programming"

print(word[ : : ]) # p   r   o   g   r   a   m   m   i   n   g

print(word[ : : 2]) # p o r m i g

# now, we use Negative (-ve) gap  

print(word[ : : -1])  # 



# print(word[ : : 2])  #