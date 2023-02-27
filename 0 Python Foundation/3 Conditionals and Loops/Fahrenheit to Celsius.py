S = int(input())
E = int(input())
W = int(input())

for i in range(S, E+1, W):
    print(i, int((i-32)*5/9))