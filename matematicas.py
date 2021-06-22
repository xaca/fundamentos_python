import math
import matplotlib.pyplot as plt

x = []
y = []

for i in range(0,360,1):
    angulo = math.radians(i)
    x.append(angulo)
    y.append(math.cos(angulo))

plt.plot(x,y)
plt.ylabel('Funcion seno')
plt.show()