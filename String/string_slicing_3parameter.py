# String slicing :- 

# ":"  => colon

# 0 1 2 3 4 5
# V i k r a m

# my_name = "Vikram"

# print(my_name[3 : ])  # ram 

# -------------------------------------------------------- 


# Three parameter String SLicing 

# 1. by default starting point will be 0
# 2. by default ending point will be LAST INDEX
# 3. by default GAP = 1
# 4. GAP( N - 1 )   
#  , if GAP = 4 , => 4 - 1 =>  3 => we have to skipp 3 elements
#    if GAP = 3 , => 3 - 1 => 2 => we have to skipp 2 elements


# 0 1 2 3 4 5 6 7 8 9 10
# P r o g r a m m i n g

# word = "Programming"
# print(word[0:9])   # P r o g r a m m i

# print(word[0:9:3]) # P g m

# # print(word[starting point : ending point : GAP])


# starting point => 0
# ending point => 9 (excluded)
# GAP (N-1) => 3   => 3 - 1 => 2 ( we have to skipp 2 elements ) 


# --------------------------------------------------------------


# 0 1 2 3 4 5 6 7 8 9 10
# P r o g r a m m i n g


word = "Programming"

print(word[1:7]) # r o g r a m

print(word[1: 9]) #  r o g r a m m i
print(word[1:9: 2 ])  # r g a m

# starting point => 1
# ending point => 9 (excluded )
# GAP ( N-1 ), 2 - 1 => 1 , we have to skipp 1 element.



# print(word[starting point : ending point : GAP])



# ------------------------------------------------- 
# # 0 1 2 3 4 5 6 7 8 9 10
# # P r o g r a m m i n g

# word = "Programming"

# print(word[0:5])  # Progr

# starting point => 0
# ending point => 5 ( Excluded )
