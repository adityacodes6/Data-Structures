n = 5
m = 3

for i in range(n**2): # O(n^2)
    print(i, end=" ")

for i in range(n):      # O(n^3)
    for j in range(n):
        for k in range(n):
            print(i, end=" ")

for i in range(n):      # O(n^m)
    for j in range(m):
        print(i, j, end=" ")


# O(n^2 + n) = O(n^2) priority for the highest term

for i in range(n): # O(n^2)
    for j in range(n):
        print(i, end=" ")

for i in range(n):  # O(n)

    print(i, end= " ")

# O(n^2 + n) => O(n^2)
# O(n^3 + n^2 + n) => O(n^3)