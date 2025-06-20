# All Types of Operators in Python - Demonstration

a = 10
b = 3

# 1. Arithmetic Operators
print("Arithmetic Operators:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print()

# 2. Comparison Operators
print("Comparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
print()

# 3. Logical Operators
x = True
y = False
print("Logical Operators:")
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)
print()

# 4. Assignment Operators
print("Assignment Operators:")
c = a  # assign value of a
print("c =", c)
c += 5
print("c += 5 ->", c)
c -= 3
print("c -= 3 ->", c)
c *= 2
print("c *= 2 ->", c)
c /= 4
print("c /= 4 ->", c)
c %= 3
print("c %= 3 ->", c)
c **= 2
print("c **= 2 ->", c)
print()

# 5. Bitwise Operators
print("Bitwise Operators:")
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a =", ~a)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1)
print()

# 6. Identity Operators
print("Identity Operators:")
print("a is b:", a is b)
print("a is not b:", a is not b)
print()

# 7. Membership Operators
print("Membership Operators:")
lst = [1, 2, 3, 10]
print("10 in lst:", 10 in lst)
print("5 not in lst:", 5 not in lst)
print()

# 8. Walrus Operator (Python 3.8+)
print("Walrus Operator:")
if (n := len(lst)) > 3:
    print("Length is greater than 3:", n)
