import numpy as np
import matplotlib.pyplot as plt

def analemma(phi = 45,time_h = 6,time_m = 0):
    #Функция, рисующая аналемму на заданную широту и время.(phi<0 - южные широты)
    E = 23.44
    dates = np.arange(1,365,10)
    B = 2 * np.pi * (dates - 81)/365.2564
    
    x0 = 7.53 * np.cos(B) + 1.5 * np.sin(B) - 9.87 * np.sin(2 * B)
    x0 = x0*360/60/24
    y0 = np.arcsin(np.sin(E*np.pi/180)*np.sin(2*np.pi*(dates-80)/365.2422)) * 180 / np.pi
    t = time_h + time_m/60
    alpha = np.cos((t-6) * 2 / 24 * np.pi )*(90-abs(phi))
    h = np.sin((t-6)*2/24*np.pi)*(90-abs(phi))
    x = x0 * np.cos(-alpha*np.pi/180) + y0 * np.sin(-alpha*np.pi/180)
    if phi >=0:
        y = y0 * np.cos(-alpha*np.pi/180) - x0 * np.sin(-alpha*np.pi/180) + h
    else:
        y = -(y0 * np.cos(-alpha*np.pi/180) - x0 * np.sin(-alpha*np.pi/180)) + h
    
    plt.axis('equal')
    plt.plot([-40,40],[0,0], '-', color = 'r')
    plt.plot(x,y,'.',color = 'b')
    
analemma(-45,18)
