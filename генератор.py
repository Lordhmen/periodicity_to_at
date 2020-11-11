import math
from random import randint

x = [0 for i in range(1, 201)]
print(x)
print(len(x))
lambdaa = 1 / 800
for i in range(0, 200):
    xx = randint(1, 999)
    x[i] = round(math.log(xx) / lambdaa)


print(sorted(x))