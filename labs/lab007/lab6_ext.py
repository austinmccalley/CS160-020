def is_integer(s):
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

def is_email(s):
    s_arr = s.split('@')
    if not len(s_arr) == 2:
        return False
    ss_arr = s_arr[1].split('.')
    if not len(ss_arr) == 2:
        return False
    else:
        return True
    print(s_arr)

def is_IP_addr(s):
    s_arr = s.split('.')
    if not len(s_arr) == 4:
        return False
    for ss in s_arr:
        if is_integer(ss):
            ss = int(ss)
            if ss < 256 and ss > 0:
                return True
            else:
                return False
    return True

def is_IPV6_addr(s):
    s_arr = s.split(':')
    hex_ls = ['A','B','C','D','E','F']
    if not len(s_arr) == 8:
        return False
    for ss in s_arr:
        if not len(ss) == 4:
            return False
        for c in ss:
            if not(c>='0' and c<='9') and c not in hex_ls:
                return False
    return True

inp = input('Please enter a string to evaluate: ')
ii = is_integer(inp)
isf = is_floating_pt(inp)
ie = is_email(inp)
isp = is_IP_addr(inp)
isp6 = is_IPV6_addr(inp)

print('Is Integer: %s' % ii)
print('Is Float: %s' % isf)
print('Is Email: %s' % ie)
print('Is IP: %s' % isp)
print('Is IPV6: %s' % isp6)
