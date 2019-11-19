import math

def floor_float(f):
    f = str(f)
    fa = f.split('.')
    return int(fa[0])

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
    if is_float(user_in) or is_int(user_in):
        return float(user_in)
    else:
        print('Please provide a proper floating point or an integer')
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

def main():

    # Thermal Conductivity k
    tc = getTC()
    # Density
    density = getDensity()
    # Specific heat
    sh = getSH()

    # Intial and Boundary Conditions
    init_t = iTemp()
    sc, ec = bConditions()

    # Material Length
    ml = mLength()
    # Divide length in x sections
    sections = mSections()

    # Number of time intervals
    ti = tIntervals()
    # Delta time
    dt = dTime()

    print(tc, density, sh)
    print(init_t, sc, ec)
    print(ml, sections)
    print(ti, dt)

    if not checkStability(tc, dt, ml, sections, sh, density):
        print('The conditions you gave are unstable!')
        sys.exit()

    times = calcTimes(ti, dt)
    ax = calcPoints(ml, sections)
    print(ax)

    for t in times:
        print(t)
        for x in ax:
            coef = density * sh
            top = (x*(t+dt)) - (x*t)
            div = top/dt
            ans = coef * div
            print(ans)
main()
