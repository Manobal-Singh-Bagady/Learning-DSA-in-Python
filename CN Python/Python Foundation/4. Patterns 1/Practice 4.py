"""
n = 4
4555 
3455 
2345 
1234
"""

n = int(input())

for i in range(1, n + 1):
    for j in range(n - i + 1, n + 1):
        print(j, end="")
    for j in range(n - i):
        print(n + 1, end="")
    print()


# Output:
# n=4
# 4555
# 3455
# 2345
# 1234