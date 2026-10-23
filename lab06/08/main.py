a = "Python"

b = a
c = a[:]

print(f"a = {a}, {id(a)}")
print(f"b = {b}, {id(b)}")
print(f"c = {c}, {id(c)}")

print("\nb == a:", b == a)
print("b is a:", b is a)
print("c is a:", c is a)

b = b + " 3"

print(f"a = {a}, {id(a)}")
print(f"b = {b}, {id(b)}")
print(f"c = {c}, {id(c)}")