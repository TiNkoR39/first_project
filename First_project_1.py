import numpy as np
import matplotlib.pyplot as plt

E = 23.44
dates = np.arange(1,365,10)
B = 2 * np.pi * (dates - 81)/365.2564

x = 7.53 * np.cos(B) + 1.5 * np.sin(B) - 9.87 * np.sin(2 * B)
x = x*360/60/24
y = np.arcsin(np.sin(E*np.pi/180)*np.sin(2*np.pi*(dates-80)/365.2422)) * 180 / np.pi

plt.axis('equal')
plt.plot([-30,30],[0,0], '-', color = 'r')
plt.plot(x,y,'.',color='b')
