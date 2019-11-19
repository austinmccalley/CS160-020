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
    user_in = input('Please provide the left and right temperature conditions seperated by a comma')
    ua = user_in.split(',')
    res = []
    for _e in ua:
        e = _e.trim()
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

def main():

    # Thermal Conductivity k
    tc = None
    # Density
    density = None
    # Specific heat
    sh = None

    # Intial and Boundary Conditions
    init_c = None
    b_c = None

    # Material Length
    ml = None
    # Divide length in x sections
    sections = None

    # Number of time intervals
    ti = None
    # Delta time
    dt = None


