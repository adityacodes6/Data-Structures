# O(n)

n = 100
i = 1

while i <= n:
    print(i, end=" ")
    i += 1

print()

# O(log2n)
n = 100
i = 1

while i <= n:
    print(i, end=" ")
    i *= 2

print()

# O(log3n)
n = 100
i = 1

while i <= n:
    print(i, end=" ")
    i *= 3

print()

# O(log3n)
i = 100
while i > 0:
    print(i, end=" ")
    i //= 3