"""
n = 4
   1 
  121 
 12321 
1234321 
 12321 
  121 
   1 
"""

n = int(input())

i = 1
inc = True
while i > 0:
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

    if i == n:
        inc = False
    if inc:
        i += 1
    else:
        i -= 1


# Output:
# n = 4
#    1
#   121
#  12321
# 1234321
#  12321
#   121
#    1
