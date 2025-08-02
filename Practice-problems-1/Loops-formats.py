# n = int(input("Enter your input: "))

#Right angle triangle with numbers:

# for i in range(1, n+1):
#     for j in range(1, i+1): 
#         print(j, end="") 
#     print()
 
#  Output:
#  Enter your input: 5
# 1
# 12
# 123
# 1234
# 12345

#Inverted Angel with numbers

# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()

# Output:
# Enter your input: 5
# 12345
# 1234
# 123
# 12
# 1

# right angle with stars

# for i in range(1, n, 1):
#     print(i*("*"))

# output:
# Enter your input: 5
# *
# **
# ***
# ****

# inverted traingle with numbers

# for i in range(n, 0, -1):
#     print(i*("*"))

# Output:
# Enter your input: 5
# *****
# ****
# ***
# **
# *

# left angle traingle with stars

# for i in range(1, n+1):
#     print(" "*(n-i)*2, end="")
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# Output:
# Enter your input: 5
#      1
#     12
#    123
#   1234
#  12345

# Traiangle 

# for i in range(1, n+1):
#     print((" ")*((n-i)), end="")
#     for j in range(1, i+1):
#         print( j , end =" ")
#     print()
# for k in range(1, n+1):
#     print((" ")*(k-1), end = "")
#     for l in range(1, ((n+2)-k)):
#         print(l, end=" ")
#     print()




# Output:
# Enter your input: 5
#      1
#     1 2
#    1 2 3
#   1 2 3 4
#  1 2 3 4 5


# rows = 5

# # Upper half
# for i in range(1, rows + 1):
#     print(' ' * (rows - i), end='')
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()

# # Lower half
# for i in range(rows - 1, 0, -1):
#     print('-' * (rows - i), end='')
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()

# Output:
# Enter your input: 5
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#     1

# print rectangle

# for i in range(n):
#     for j in range(n):
#         print(("*"), end="")
#     print()

# output:
# Enter your input: 5
# *****
# *****
# *****
# *****
# *****
    
# Print hollow square

# n =5
# m =5
# for i in range(n):
#     for j in range(m):
#         if i == 0 or j == 0 or i == (m-1) or j == (n-1):
#             print(("*"), end="")
#         else:
#              print((" "), end="")

#     print()

# Output:
# Enter your input: 5
# *****
# *   *
# *   *
# *   *
# *****

