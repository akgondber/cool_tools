import numpy as np
import matplotlib.pyplot as pylt

x = np.linspace(-np.pi, np.pi, num=81)
y = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) + 0.8

p1 = pylt.plot(x, y, 'ro', label='sin(x)')
p2 = pylt.plot(x, y2, 'ro', label='cos(x)', color='g')
pylt.plot(x, y3, 'ro', label='sin(x) + 0.8', color='c')
pylt.xlabel('x')
pylt.ylabel('y')

pylt.legend(loc=2)
pylt.xlim(-np.pi - 0.2, np.pi + 0.2)
pylt.ylim((np.amin((y, y2, y3,))) - 0.6, (np.amax((y, y2, y3,))) + 0.6)
pylt.savefig('images/n_a_m_s.png')
