"""
n = 4
   * 
  *** 
 ***** 
*******
"""

n = int(input())

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print("*", end="")
    for j in range(i - 1, 0, -1):
        print("*", end="")
    print()


# Output:
# n = 4
#    *
#   ***
#  *****
# *******
