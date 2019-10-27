import random

def rNum():
    a = random.randint(0,999999)
    b = random.randint(0,999999)
    if a > b:
        return rNum()
    return [a,b]

def function1(num):
    return 10*num**2

def function2(num):
    return 2*num**2 -5

def function3(num):
    return num + 20

def summation(function, a, b):
    if a == 0 and b == 0:
        return 0

    elif function == 'f1':
        summation = 0
        for x in range(a,b+1):
            summation += function1(x)
        return summation
    elif function == 'f2':
        summation = 0
        for x in range(a,b+1):
            summation += function2(x)
        return summation
    elif function == 'f3':
        summation = 0
        for x in range(a, b+1):
            summation += function3(x)
        return summation
    else:
        return -1

def pySum(function, a, b):
    ls = []
    if a == 0 and b == 0:
        return 0
    elif function == 'f1':
        for x in range(a, b+1):
            ls.append(function1(x))
    elif function == 'f2':
        for x in range(a, b+1):
            ls.append(function2(x))
    elif function == 'f3':
        for x in range(a, b+1):
            ls.append(function3(x))
    return sum(ls)

def testRNums(n):
    for x in range(0, n):
        allowed_functions = ['f1','f2','f3']
        for x in range(0, len(allowed_functions)):
            func = allowed_functions[x]
            a,b = rNum()

            print('a: %s' % a)
            print('b: %s' % b)
            print('func: %s' % func)
            print('pySum: %s' % pySum(func, a, b))
            print('summation: %s' % summation(func, a, b))
            print('\n')
            assert pySum(func,a,b) == summation(func,a,b)


num_tests = int(input('How many different tests do you want to run? '))
testRNums(num_tests)

