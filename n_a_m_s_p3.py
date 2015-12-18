import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()

plt.clf()
plt.figure(1)
plt.subplot(211)
plt.plot([1,3,8])
plt.subplot(212)
plt.plot([4,5,6])

plt.figure(1)
plt.subplot(211)
plt.title('Ease as 1, 3, 8')
plt.savefig('images/n_a_m_s_p3-2.png')

plt.figure(2)
plt.plot([4,5,6])
plt.savefig('images/n_a_m_s_p3.png')