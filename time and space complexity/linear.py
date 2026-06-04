# O(n)

n = 5
for i in range(n):
    print(i)

for i in range(n+100):
    print(i)

for i in range(n-100):
    print(i)

for i in range(n//2):
    print(i)


# O(n+x)
for i in range(n):
    print(i)

for x in range(n):
    print(x)