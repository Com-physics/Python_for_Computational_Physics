# Importing module
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 50, 0.0001) # Declaring x as a variable and assigning the value with the help of numpy arrange function starting from 0 to ending at 50 with the step value = 0.0001 (for smoother wave plotting)
sin1 = np.sin(x) # Using numpy module assign f(x) = sin(x) as a wave 1
sin2 = np.sin(2*x) # Similiarly assign g(x) = sin(2x) as a wave 2
y= sin1 + sin2 # To visualize the convergence, h(x) = f(x) + g(x)
plt.plot(x, sin1, 'r') # To plot f(x), assign color value as red
plt.plot(x, sin2, 'g') # To plot g(x), assign color value as green
plt.plot(x, y, 'b') # To plot h(x), assign color value as blue
plt.show()