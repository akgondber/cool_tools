import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.savefig('images/n_a_m_s_2.png')

arr1 = np.array([4, 3, 2, 11, 22, 2, 16, 7], dtype=np.float32)
tmp_arr = []
for i, v in enumerate(arr1):
    if i % 2 == 0:
        tmp_arr.append(v / 2.8)
    else:
        tmp_arr.append(v * 2.1)

plt.clf()
arr2 = np.array(tmp_arr)
line = plt.plot(arr1, arr2, 'H')
plt.setp(line, 'color', 'g', 'alpha', .62, 'ls', '-.',)
plt.ylim(np.min(arr2) - 1, np.max(arr2) + 1)
plt.xlim(np.min(arr1) - 1, np.max(arr1) + 1)
plt.savefig('images/n_a_m_s_2_1.png')