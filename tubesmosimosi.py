
#%%
#init
import numpy as np
import matplotlib.pyplot as plt
import math

# init
x = 0 # initial x 
y = 0 # initial y 
v0 = 50 # initial velocity
angle = 35 # initial angle
angle_rad = math.radians(angle) # convert degree to radian
g = 9.806 # gravity acceleration
t = 0 # time
dt = 0.01 
d = 0.0013
m = 150
print(angle_rad)

#%%
#NUMERICAL
x_arr = [x]
y_arr = [y]
t_arr = [t]

vx = v0 * np.cos(angle_rad)
vy = v0 * np.sin(angle_rad)

ax = 0
ay = -g

while y >= 0:
    vy += ay*dt
    vx += ax*dt
    y += vy*dt
    x += vx*dt
    t += dt
    if y <= 0:
        break
# store
    x_arr.append(x)
    y_arr.append(y)
    t_arr.append(t)
    
t_tot_num = t_arr[-1]
# range
range_num = x_arr[-1]
# max height
h_max_num = np.max(y_arr)

print("SOLUSI NUMERIK")
print("TOTAL WAKTU ",t_tot_num)
print("JARAK YANG DITEMPUH",range_num)
print("TINGGI MAKSIMAL",h_max_num)
print("-------------------------")

#%%
#ANALYTICAL
x_ex_arr = [0]
y_ex_arr = [0]
x0 = 0
y0 = 0
vx0 = v0 * np.cos(angle_rad)
vy0 = v0 * np.sin(angle_rad)
vx = vx0
vy = -vy0
ax = 0
ay = -g
# t = 0


for t in t_arr:
    v = math.sqrt((vx * vx) + (vy * vy))
    ax = (-d/m) * v * vx
    ay = - g - ((d/m) * v * vy)
    x_ex = x0 + (vx0 * t) + ((ax/2) * t * t)
    y_ex = y0 + (vy0 * t) + ((ay/2) * t * t)
    x_ex_arr.append(x_ex)
    y_ex_arr.append(y_ex)

    # x_ex = v0 * np.cos(angle_rad) * t
    # y_ex = (0.5 * g * t**2) + (v0 * np.sin(angle_rad) * t)

# total time
t_tot_ex = (2 * v0 * np.sin(angle_rad))/g
# range
range_ex = v0 * np.cos(angle_rad) * t_tot_ex
# max height
h_max_ex = (v0**2 * np.sin(angle_rad)**2) / (2 * g)

print("SOLUSI ANALITIK")
print("TOTAL WAKTU ",t_tot_ex)
print("JARAK YANG DITEMPUH",range_ex)
print("TINGGI MAKSIMAL",h_max_ex)

plt.figure()
plt.plot(x_arr, y_arr, c='b', label='numerical')
plt.plot(x_ex_arr, y_ex_arr, c='r', label='analytical')
plt.axhline(c='black')
plt.axvline(c='black')
plt.legend()
plt.show()

# %%
