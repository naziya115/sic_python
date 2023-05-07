import math

x = 10100
count = 0

while len(str(x)) <= 100:
    if x % 2020 == 0:
        print(x)
        count += 1
    x = int(x) * 10
print(count)