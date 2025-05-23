
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 5*np.pi, 0.1)
y = np.sin(x)


plt.plot(x, y, color='green')
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()


from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(0, 1, 1000, endpoint=True)


plt.plot(t, signal.square(2 * np.pi * 5 * t))
plt.title("Square Wave")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()