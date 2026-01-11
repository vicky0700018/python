# while loop :- 


# Python does not support increement operator or decreement operator 

# => i++ => Post increment 
# => ++i => pre increment
# => --i => pre decrement
# => i-- => post decrement


# i++ OR i = i+1 OR  i += 1 => these are same thing

# example of C language 
#include <stdio.h>

# int main() {
#     int i = 3;

#     printf("%d", i++);
#     printf("\n");
#     printf("%d", i);
#     return 0;
# }

# here we get the output = 3 
# because the priority of post increement is less than print statement.


# #include <stdio.h>

# int main() {
#     int i = 3;

#     printf("%d", ++i);
#     printf("\n");
#     printf("%d", i);
    

#     return 0;
# }