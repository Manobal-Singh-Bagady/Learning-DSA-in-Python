"""
n = 3
* * * 
* * 
* 
"""

n = int(input())

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# Output:
# n = 4
# * * * *
# * * *
# * *
# *
