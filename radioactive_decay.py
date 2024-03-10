# Importing the module
import numpy as np
import matplotlib.pyplot as plt 
# Starting value
y = 1

# Number of iterations (not less than 200)
n = 300

# Stepsize
h = 0.01

# Collect data
t_values = [0]
y_values = [y]

# Starting a loop for a specified range of iterations i.e. from 1 to 200
for i in range(1, n+1):
    f = -y # Converting the starting value to negative and assigning it into newly decalred memory
    y = y + f * h
    t_values.append(i*h) # append the calculated data to the t_values variable i.e. empty list
    y_values.append(y) # append the calculated data to the y_values variable
    print(y) # Print the value for reference
# Plotting part
np.exp(-n*h) 
test_t = np.linspace(0, n*h, n)
test_y = 1*np.exp(-test_t)
plt.plot(test_t, test_y, 'red')

plt.xlabel('time')
plt.ylabel('Counts per minute')
plt.scatter(t_values, y_values)
plt.show()