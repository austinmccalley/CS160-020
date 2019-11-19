def is_floating_pt(s):
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


