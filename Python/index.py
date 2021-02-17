m = int(input())
a = [""] * m

for i in range(m):
    a[i] = str(input())

n = int(input())
b = [""] * n

for j in range(n):
    b[j] = str(input())

for i in range(n):
    for j in range(n):
        if a[i] in b[j]:
            print("YES")
        else:
            print("NO")