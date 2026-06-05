name = 'aditya'
room = 'A'
address = "mumbai, vikhroli, india"

intro = '''
my name is aditya
i am from pune
i live mumbai'''

print(type(name))
print(type(room))
print(type(address))
print(type(intro))

s = 'pwskill'
print(s[2])

print(list(s))

print(len(s))
print(s[-2])
print(s.upper())
print(s.lower())
print(s.capitalize())


print(s.replace("s", "y"))

print(s[2:4])
print(s[::-1])

s = "my name is aditya"
print(s.index("name"))
# print(s.index("baby"))
print(s[::-1])


s = "my name is aditya"
print(s.index("name"))
print(s.index("is ad"))

s = "Aditya"
print(s.startswith("Adi"))
print(s.endswith("tya"))

s = input()
s = s.strip()
print(s)   

s = "my name is aditya"
print(s.split())

s = "the sky is blue"
s = s.strip()
s = s.split()
s.reverse()

# convert list to string

s = " ".join(s)
print(s)