import math as m
import matplotlib.pyplot as plt

duration_sim = 50 # duration of simulation /s
timestep_sim = 0.01 # timestep of simulation timestep /s
steps_sim = duration_sim/timestep_sim # total number of steps in the simulation


time = [0] * round(steps_sim) # create arrays to be plotted on graph
Yval = [0] * round(steps_sim)

for i in range(round(steps_sim)):
    time[i] = i * timestep_sim
    Yval[i] = m.sin((i* timestep_sim)/10)*10 + m.cos(i/2)*0







plt.plot(time, Yval)
plt.show()