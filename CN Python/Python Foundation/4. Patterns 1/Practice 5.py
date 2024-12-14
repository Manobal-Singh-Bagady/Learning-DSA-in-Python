"""
n = 4
1 
11 
202 
3003
"""

n = int(input())

for row in range(1, n+1):
    for col in range(1, row+1):
        if row == 1:
            print(1, end="")
        elif col ==1 or col == row:
            print(row-1, end="")
        else:
            print(0, end="")
    print()