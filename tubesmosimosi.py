import numpy as np
import matplotlib.pyplot as plt
import math

x = 0 
y = 0 
t = 0
v0 = 50 # inisialisasi velocity
angle = 35 # inisialisasi sudut
angle_rad = math.radians(angle) # convert dari sudut ke radian
g = 9.806 # gravitasi
dt = 0.01 # delta t
d = 0.0013
m = 0.15 
print(angle_rad)

#numerik tanpa hambatan
x_array = [x]
y_array = [y]
t_array = [t]

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
    x_array.append(x)
    y_array.append(y)
    t_array.append(t)
    
t_tot_numtanpa = t_array[-1]
# jarak
range_numtanpa = x_array[-1]
# tinggi maks
h_max_numtanpa = np.max(y_array)

print("TOTAL WAKTU =",t_tot_numtanpa)
print("JARAK YANG DITEMPUH =",range_numtanpa)
print("TINGGI MAKSIMAL =",h_max_numtanpa)
print("-------------------------")

#numerik dengan hambatan
vxhambatan = v0*np.cos(angle_rad)
vyhambatan = v0*np.sin(angle_rad)

xhambatan = 0
yhambatan = 0
thambatan = 0
array_xhambatan,array_yhambatan,array_thambatan = [xhambatan],[yhambatan],[thambatan]

while yhambatan>=0:
    vhambatan = math.sqrt((vxhambatan*vxhambatan)+(vyhambatan*vyhambatan))
    axhambatan = -(d/m)*vhambatan*vxhambatan
    ayhambatan = -g-(d/m)*vhambatan*vyhambatan
    vxhambatan += axhambatan*dt
    vyhambatan += ayhambatan*dt
    xhambatan += vxhambatan*dt
    yhambatan += vyhambatan*dt
    thambatan += dt
    if yhambatan <= 0 :
        break
    array_xhambatan.append(xhambatan)
    array_yhambatan.append(yhambatan)
    array_thambatan.append(thambatan)

t_tothambatan = array_thambatan[-1]
h_maxhambatan = np.max(array_yhambatan)
r_maxhambatan = array_xhambatan[-1]


print("TOTAL WAKTU =",t_tothambatan)
print("JARAK YANG DITEMPUH =",r_maxhambatan)
print("TINGGI MAKSIMAL =",h_maxhambatan)
print("-------------------------")


#ANALYTICAL
x_an_array = [0]
y_an_array = [0]
x0 = 0
y0 = 0
vx0 = v0 * np.cos(angle_rad)
vy0 = v0 * np.sin(angle_rad)
vx_an = vx0
vy_an = vy0
ax = 0
ay = -g

v = math.sqrt((vx * vx) + (vy * vy))
for t in t_array:

    x_an = x0 + (vx0 * t) + ((ax/2) * t * t)
    y_an = y0 + (vy0 * t) + ((ay/2) * t * t)
    x_an_array.append(x_an)
    y_an_array.append(y_an)


# total waktu
t_tot_an = (2 * v0 * np.sin(angle_rad))/g
# jarak
range_an = v0 * np.cos(angle_rad) * t_tot_an
# tinggi maks
h_max_an = (v0**2 * np.sin(angle_rad)**2) / (2 * g)

print("TOTAL WAKTU =",t_tot_an)
print("JARAK YANG DITEMPUH =",range_an)
print("TINGGI MAKSIMAL =",h_max_an)

# jawaban no 1
plt.figure()
plt.title("NUMERIK")
plt.title("Hambatan dibandingkan dengan Tanpa Hambatan")
plt.plot(x_array, y_array, c='r', label='Tanpa Hambatan')
plt.plot(array_xhambatan, array_yhambatan, c='y', label='Hambatan')
plt.axhline(c='black')
plt.axvline(c='black')
plt.legend()
plt.show()


# jawaban no 2
plt.figure()
plt.title("Analitik dibandingkan dengan Numerik")
plt.plot(x_array, y_array, c='r', label='NUMERIK')
plt.plot(x_an_array, y_an_array, c='y', label='ANALITIK')
plt.axhline(c='black')
plt.axvline(c='black')
plt.legend()
plt.show()