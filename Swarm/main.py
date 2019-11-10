import random
import numpy as np
import copy
from matplotlib import pyplot as plt

Table = [
    (902000, 115800),
    (462000, 96000),
    (465000, 790000),
    (545000, 908000),
    (311000, 396000),
    (675000, 984000),
    (128000, 189000),
    (105000, 103000),
    (215000, 285000),
    (31000, 70000),
    (42000, 90000),
    (78000, 73000),
    (21000, 50000),

    (50000, 84000),
    (786000, 987000),
    (97000, 156000),
    (125000, 239000),
    (1008000, 1383000),
]
print("Table: ", Table)
# Удалить повторяющиеся элементы
#Table = list(set(Table))
# Граница 75/25
border = int(len(Table) * 0.75)
test = Table[border:]
train = Table[:border]
print("test: ", test)
print("train: ", train)

# Евклидово расстояние
def ED(x, t=train):
    s = 0.0
    for el in t:
        s += (x[0] * el[0] ** x[1] - el[1])**2
        # print(x[0], x[1],el[0] ** x[1] - el[1], s)
    return np.sqrt(s)

def generate(n, lb=0.0, rb=10.0):
    r = []
    for i in range(n):
        r.append((random.uniform(lb, rb), random.uniform(lb, rb)))
    return r

# n - кол-во особей
# t - кол-во поколений
# c1,c2 - ветер
def ra(n=100, t=500, c1=2, c2=1):
    Y = np.array(generate(n))
    X = Y.copy()
    # X = Y
    ymax = copy.copy(Y[0])
    v = [0] * n
    x0 = []
    x1 = []

    for i in range(t):
        x0.append(i)
        x1.append(ED(ymax))
        for j in range(n):
            if ED(X[j]) < ED(Y[j]):
                Y[j] = X[j]

            if ED(Y[j]) < ED(ymax):
                ymax = Y[j]
                # ymax = copy.copy(Y[j])
                # print(ED(ymax))

        for j in range(n):
            v[j] = v[j] + c1 * random.uniform(0.0, 1.0) * (Y[j] - X[j]) + c2 * random.uniform(0.0, 1.0) * (ymax - X[j])
            X[j] = X[j] + v[j]

    x0.append(t + 1)
    x1.append(ED(ymax))
    return [ymax, x0, x1]

maximum, x0, x1 = ra(100, 500, 2, 1)
print(maximum, ED(maximum, test))
plt.plot(x0, x1)
plt.show()
