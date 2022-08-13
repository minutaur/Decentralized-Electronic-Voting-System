result = 0
def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))
for i in range(10):
    print(add(2))
