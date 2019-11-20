import numpy as np
import matplotlib.pyplot as plt


L = 0.1
n = 10
T0 = 0
T1s = 40
T2s = 20
dx = L/n
k = 52.4
p = 0.321
c = 0.12
alpha = 10**-6
print(alpha)
t_final = 0.01675
dt = 0.000335
ti = 50


def linSpace(s, e, n):
    res = []
    prev = 0
    for i in range(n):
        res.append(s + (e-s)/n * i)

    return res

def calcTimes(ti, dt):
    times = []
    for i in range(ti):
        curr_time = dt*i
        times.append(curr_time)
    return times


x = linSpace(dx/2, L-dx/2, n)

T = ([T0]*n)
dTdt = [0]*n

t = calcTimes(ti, dt)

def c_dtmdt(dtdt, dt):
    res = []
    for el in dtdt:
        res.append( el * dt)
    return res

def incT(tl, dtmdt):
    res = []
    for el in tl:
        io = tl.index(el)
        res.append(el + dtmdt[io])
    return res

for j in range(1, len(t)):
    for i in range(1, n-1):
        dTdt[i] = alpha * (-(T[i]-T[i-1])/dx**2 + (T[i+1]-T[i])/dx**2)
    dTdt[0] = alpha * (-(T[0]-T1s)/dx**2 + (T[0+1]-T[0])/dx**2)
    dTdt[n-1] = alpha * (-(T[n-1]-T[n-2])/dx**2 + (T2s-T[n-1])/dx**2)
    dtmdt = c_dtmdt(dTdt, dt)
    print(dtmdt)
    T = incT(T, dtmdt)
    print(T)