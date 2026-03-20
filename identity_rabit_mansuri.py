# Integer
a = 21
print("Before change (int):", id(a))
a = a + 7
print("After change (int):", id(a))

# String
s = "hello"
print("\nBefore change (string):", id(s))
s = s + " world"
print("After change (string):", id(s))

# List
lst = [5, 6, 7]
print("\nBefore change (list):", id(lst))
lst.append(4)
print("After change (list):", id(lst))

# Tuple
t = (2, 3, 4)
print("\nBefore change (tuple):", id(t))
t = t + (4,)
print("After change (tuple):", id(t))