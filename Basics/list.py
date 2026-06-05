name = "aditya"

names = ['aditya', 'rahul', 'jonathan']
print(names)

list1 = [100, "hello", 24.33, "aditya", True]
print(list1)
print(len(list1))
print(type(list1))

print(list1[1])

# negative indexing
print(list1[-3])

# index
list1 = [100, "hello", 24.33, "aditya", True]
print(list1.index("hello"))
print(list1.index(True))

if "hi" in list1:
    print(list1.index("hi"))
else:
    print("not present")

# copy

list1 = [1, 2, 3]
list2 = list1.copy()   # shallow copy
list1[0] = 100

print(list1)
print(list2)

list2[1] = 100

print(list1)
print(list2)

print(list(range(1, 10)))
print(list(range(15, 6, -1)))