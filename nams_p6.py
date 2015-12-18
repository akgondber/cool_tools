import numpy as np
import matplotlib.pyplot as plt

y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y > 1)]
y.sort()
x = np.arange(len(y))

plt.figure(1)

plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)

plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)

plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.05)
plt.title('symlog')
plt.grid(True)

plt.subplot(223)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)

plt.savefig('images/nams_p6.png')