li = list(map(int, input().split()))

xor = 0
for i in li:
    xor^=i
print(xor)