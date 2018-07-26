# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np

def create_plot():
    x = np.arange(-10, 10, 0.002)
    y = 1 / (1 + x*x)
    return(x, y)
    
fig = plt.figure()
x, y = create_plot()
plt.plot(x, y)
plt.grid(True)
plt.show()
