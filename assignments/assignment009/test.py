L = 10
n = 10
T0 = 0
T1s = 0
T2s = 100
dx = L/n
k = 52.4
p = 0.321
c = 0.12

ti = 50


t_final = 0.01675
dt = 0.000335


coeff = c*p


def calcTimes(ti, dt):
    times = []
    for i in range(ti):
        curr_time = dt*i
        times.append(curr_time)
    return times


_t = calcTimes(ti, dt)

for t in range(0, len(_t)):
    curr_time = t * dt
    time_temps = []
    print(curr_time)
    for u in range(n-1, 0, -1):
        res = (time_temps[t+1] - time_temps[t])
        res = res/dt
        res = coeff *res
        print(res)