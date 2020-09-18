a = 10
b = 5
c = 2
d = 3
e = 5
f = 2
g = 5

som1 = a + c
print("Plus: ", som1)
som2 = 9
print("Toekennen: ", som2)
som3 = a - g
print("Aftrekken: ", som3)
som4 = a / f
print("Delen: ", som4)
som4 += som1
print("Optellen bij waarde: ", som4)
som2 /= som3
print("Delen door waarde:", som2)
som8 = a == c
print(som8)
print(c ** f)
print(a // b)
print(e % d)

x = 5
x += 3
print(x)

x = 5
x -= 3
print(x)

x = 5
x *= 3
print(x)

x = 5
x /= 3
print(x)

x = 5
x%=3
print(x)

x = 5
x//=3
print(x)

x = 5
x **= 3
print(x)

x = 5
print(x > 3 and x < 10)

x = 5
print(x > 3 or x < 4)

x = 5
print(not(x > 3 and x < 10))
