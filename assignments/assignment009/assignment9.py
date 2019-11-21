import math, csv
from wire_plotter import Wire_Plotter


def is_int(s):
    negative = True if s[:1] == '-' else False
    if negative:
        return False
    else:
        for c in s:
            if not(c>='0' and c<='9'):
                return False
        return True

def is_float(s):
   negative = True if s[:1] == '-' else False
   split_s = s.split('.')
   if not len(split_s) == 2:
       return False
   if negative:
       s = s[1:]
       rd = 0
       for c in s:
           if not (c>='0' and c<= '9') or c == '.':
                if c == '.':
                   rd += 1
                else:
                    return False
       if rd > 1:
           return False
       return True
   else:
       rd = 0
       for c in s:
           if not (c>='0' and c<= '9') or c == '.':
             if c == '.':
                 rd +=1
             else:
                 return False
       if rd > 1:
           return False
       return True

def getTC():
    user_in = input('Please enter the thermal conductivity you want to use: ')
    if is_float(user_in):
        return float(user_in)
    else:
        print('Please provide a proper floating point')
        return getTC()

def getDensity():
    user_in = input('Please enter the density you want to use: ')
    if is_float(user_in):
        return float(user_in)
    else:
        print('Please provide a proper floating point')
        return getDensity()

def getSH():
    user_in = input('Please enter the specific heat you want to use: ')
    if is_float(user_in):
        return float(user_in)
    else:
        print('Please provide a proper floating point')
        return getSH()

def iTemp():
    user_in = input('Please provide the intial temp of the wire: ')
    if is_float(user_in):
        return float(user_in)
    else:
        print('Please provide a proper floating point')
        return iTemp()

def bConditions():
    user_in = input('Please provide the left and right temperature conditions seperated by a comma: ')
    ua = user_in.split(',')
    res = []
    for _e in ua:
        e = _e.strip()
        if is_float(e):
            res.append(float(e))
        else:
            print('You did not provide a float. Please provide a proper floating point')
            return bConditions()
    return res

def mLength():
    user_in = input('Please provide the length of the material: ')
    if is_float(user_in) or is_int(user_in):
        return float(user_in)
    else:
        print('Please provide a proper floating point or an integer')
        return mLength()

def mSections():
    user_in = input('Please provide the number of sections the material will be divided in: ')
    if is_int(user_in):
        return int(user_in)
    else:
        print('Please provide an integer')
        return mSections()

def tIntervals():
    user_in = input('Please provide the number of time intervals wish you want to use: ')
    if is_int(user_in):
        return int(user_in)
    else:
        print('Please provide a proper integer')
        return tIntervals()

def dTime():
    user_in = input('Please provide the change in time per interval: ')
    if is_float(user_in):
        return float(user_in)
    else:
        print('Please provide a proper floating point')
        return dTime()

def checkStability(k, dt, ml, sec, c, p):
    dt_tc = k*dt
    dx = ml / sec
    cp = c * p
    bot = dx**2 * cp
    # DEBUG
    # print(dt_tc, dx, cp, bot)

    div = dt_tc / bot
    # DEBUG
    # print(div)

    if abs(div) < 0.05:
        return False
    else:
        return True

def calcTimes(ti, dt):
    times = []
    for i in range(ti):
        curr_time = dt*i
        times.append(curr_time)
    return times

def calcPoints(ml, sec):
    points = []
    dx = ml/sec
    sec = floor_float(sec)
    for i in range(sec+1):
        points.append(dx*i)
    return points

def calcT(sec, t):
    if t == 0:
        return [0]*int(sec)
    else:
        ([1]*int(sec))*int(t)

def saveListToCSV(l, fn):
    with open(fn+".csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(l)

def visualize(fn, wl, wd, tl, tr, v):
    plotter = Wire_Plotter(wl, wd, tl, tr, v)

    f = open(fn+".csv", "r")
    lines = f.readlines()
    for l in lines:
        # Read in a line from the file and split on the comma
        wire_temps = l.split(',')

        # Convert all element of the list to be floats
        for i in range(len(wire_temps)):
            wire_temps[i] = float(wire_temps[i])
        print(wire_temps)

        # Pass in the the array of the wire temps
        plotter.add_interval(wire_temps)
    
    # Animate the plot
    plotter.animate()


def main():

    # Thermal Conductivity k
    k = getTC()
    # Density
    p = getDensity()
    # Specific heat
    c = getSH()

    # Intial and Boundary Conditions
    init_temp = iTemp()
    left_temp, right_temp = bConditions()

    # Material Length
    length = mLength()
    # Divide length in x sections
    sections = mSections()
    # delta x - Self explanitory
    deltax = length / sections

    # Number of time intervals
    time_int = tIntervals()
    # Delta time
    deltat = dTime()




    const = (k*deltat)/(deltax**2 * c *p)

    if abs(const) > 0.5:
        print('Unstable conditions! Exiting program')
        exit()

    # Hold all the arrays of all time
    u = []

    uold = [init_temp]*sections
    uold[0] = left_temp
    uold[sections-1] = right_temp

    unew = [init_temp]*sections
    unew[0] = left_temp
    unew[sections-1] = right_temp

    for i in range(time_int):
        for x in range(1, sections - 1):
            top = (uold[x+1]-2*uold[x]+uold[x-1])
            unew[x]=const*top + uold[x]
        u.append(unew)
        print(i, u[i])
        uold = u[-1]

    saveListToCSV(u, "out")
    visualize("out", length, sections, left_temp, right_temp, True)
    

main()
