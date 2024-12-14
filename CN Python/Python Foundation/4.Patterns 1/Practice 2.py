"""
n = 4

12344321 
123​**​321 
12​****​21 
1​******​1
"""

n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 2 - i):
        print(j, end="")
    print("*" * ((i - 1) * 2), end="")
    for j in range(n - i + 1, 0, -1):
        print(j, end="")
    print()


# Output:
# n=4
# 12344321
# 123**321
# 12****21
# 1******1
