#Case 1
for x in range(1,100):
    print(x)
#Case 2
for x in range(100,1,-4):
    print(x, end=" ")
#Case 3
result = 30
add = -1
for i in range(4):
    print(result, end=" ")
    result -= add
    add += 2
#Case 4
result = 1
add = 1
for i in range(8):
    print(result, end=" ")
    result += add
    add += 2
#Case 5
a,b = 1,1
for i in range(11):
    print(a, end=" ")
    a, b = b, a + b
#Case 6

