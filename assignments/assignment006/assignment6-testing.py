from scipy.integrate import quad
import numpy as np
import random
from assignment6 import rectangleApproximation, trapezoidalApproximation

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '%.12f' % f
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def function1(x):
    ans = 10.0*x**2.0
    return ans

def function2(x):
    return 2.0*x**2.0 - 5.0

def function3(x):
    return x + 20.0

def getRandomAB():
    a = random.randint(0, 99)
    b = random.randint(a+1, 99)
    return a,b

for x in range(0, 5):
    a,b = getRandomAB()
    n = random.randint(1,25)
    w = (b-a)/n
    print('a=%s b=%s n=%s w=%s' % (a,b,n,w))

    print('--F1 Error Approximation--')
    aq1, e1 = quad(function1, a, b)
    ar1 = rectangleApproximation('f1',n,a,b)
    at1 = trapezoidalApproximation('f1',n,a,b)
    per1 = abs(ar1-aq1)/aq1
    pet1 = abs(at1-aq1)/aq1
    print('Rectangle Error: ' + str(per1 * 100) + '%')
    print('Trapezoid Error: ' + str(pet1 * 100) + '%')

    print('--F2 Error Approximation--')
    aq2, e2 = quad(function2, a, b)
    ar2 = rectangleApproximation('f2',n,a,b)
    at2 = trapezoidalApproximation('f2',n,a,b)
    per2 = abs(ar2-aq2)/aq2
    pet2 = abs(at2-aq2)/aq1
    print('Rectangle Error: ' + str(per2 * 100) + '%')
    print('Trapezoid Error: ' + str(pet2 * 100) + '%')

    print('--F3 Error Approximation--')
    aq3, e3 = quad(function3, a, b)
    ar3 = rectangleApproximation('f3',n,a,b)
    at3 = trapezoidalApproximation('f3',n,a,b)
    per3 = abs(ar3-aq3)/aq3
    pet3 = abs(at3-aq3)/aq3
    print('Rectangle Error: ' + str(per3 * 100) + '%')
    print('Trapezoid Error: ' + str(pet3 * 100) + '%')

    assert per1 < 0.1,'Function 1 rectangle approximation is not accurate enough'
    assert per2 < 0.1,'Function 2 rectangle approximation is not accurate enough'
    assert per3 < 0.1,'Function 3 rectangle approximation is not accurate enough'
    assert pet1 < 0.1,'Function 1 trapezoid approximation is not accurate enough'
    assert pet2 < 0.1,'Function 2 trapezoid approximation is not accurate enough'
    assert pet3 < 0.1,'Function 3 trapezoid approximation is not accurate enough'
    print('\n')
