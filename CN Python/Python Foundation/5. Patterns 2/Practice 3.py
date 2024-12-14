"""
n = 4
1​     ​1 
 ​2​   ​2  
  ​3​ ​3   
   ​4   
  ​3​ ​3   
 ​2​   ​2  
1​     ​1
"""

n = int(input())

row = 1
inc = True
while row > 0:
    for col in range(1, n + 1):
        if col == row:
            print(col, end="")
        else:
            print(" ", end="")
    for col in range(n - 1, 0, -1):
        if col == row:
            print(col, end="")
        else:
            print(" ", end="")
    print()

    if row == n:
        inc = False
    if inc:
        row += 1
    else:
        row -= 1


# Output:
# n = 4
# 1     1
#  2   2
#   3 3
#    4
#   3 3
#  2   2
# 1     1
