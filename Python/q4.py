import numpy as np

x = np.ones((20,20))
for i in range(20):
    for j in range(20):
        x[(i,j)] = np.random.normal()

y = np.ones(20)

for i in y:
    y = np.random.normal()

answer = np.linalg.inv(x.T*x)*x.T*y
print(answer)


