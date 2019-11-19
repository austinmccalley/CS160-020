def is_int(s):
    negative = True if s[:1] == '-' else False
    if negative:
        if len(s) == 1:
            return False
        s = s[1:]
        for c in s:
            if not (c>='0' and c<='9'):
                return False
        return True
    else:
        for c in s:
            if not(c>='0' and c<='9'):
                return False
        return True

def getTC():
    user_in = input('Please enter the thermal conductivity you want to use: ')

    if is_int(user_in):
        return int(user_in)
    else:
        print('Please provide an integer')
        return getTC()


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


