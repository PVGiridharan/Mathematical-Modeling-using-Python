# Calculate the simple harmonic motion of undamped and damped spring mass system
# First import plot, numpy and default math libraries
import matplotlib.pyplot as plt
import numpy as np
import math

#define variables for parameters
m = 1 # mass of the object in kg
k = 35 # stiffness of massless spring in N/m
c = 0.35 # coeffiecent of damping in Ns/m (modify the damping to evaluate the underdamping, critical and over damped systems)
p = 0 # phase angle
d = 1 # spring length in meter
do = 10 # forced initial displacement of the spring in millimeter
step_size = 0.01 # step size of calculation
 
# calculate the Angular Frequency, Frequency and Time Period
omega = math.sqrt(k/m) # Angular Frequency of the system
freq_un = math.sqrt(k/m)/(2*math.pi) # Natural frequency of system
freq_dam = freq_un*math.sqrt(1-(c/(2*math.sqrt(k*m)))) # Natural frequency of system
time_period = 1/freq_un # Time period for 1 cycle

# define function to calculate the displacement of undamped spring mass system
def f_un(t):
    return do*math.cos(omega*t)
    
# define function to calculate the displacement of damped spring mass system
def f_dam(t):
    return do*math.exp(-(c/2)*m*t)*math.cos(omega*t)
    
# define the time data as array
t=np.linspace(0,time_period*5,5*int(1/step_size))
#define y values equal to time array and as set as zero before calculation
y_un=np.zeros(len(t))
y_dam=np.zeros(len(t))
#calculate the harmonic motion of undamped spring mass system
for i in range(len(t)):
    y_un[i]=f_un(t[i])
    
#calculate the harmonic motion of damped spring mass system
for i in range(len(t)):
    y_dam[i]=f_dam(t[i])
    
# Print Output of #calculate the harmonic motion of undamped spring mass system
print("Angular Frequency of the Undamped System = " + str(round(omega,2)) + " rad/s")
print("Natural Frequency of the Undamped System = " + str(round(freq_un,2)) + " Hz")
print("Natural Frequency of the Damped System = " + str(round(freq_dam,2)) + " Hz")
print("Time Period for 1 cycle - Undamped System = " + str(round(time_period,2)) + " s")
#Plot the results for 5 cycles
plt.plot(t,y_un)
plt.plot(t,y_dam)
plt.xlabel("time")
plt.ylabel("displacement [mm]")
plt.show()
