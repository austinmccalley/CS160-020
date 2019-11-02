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
    n = 9999999
    w = (b-a)/n
    print(a, b, w)

    print('--F1--')
    aq1, e1 = quad(function1, a, b)
    ar1 = rectangleApproximation('f1',n,a,b)
    ad1 = abs(aq1-ar1)
    print(aq1, ar1, ad1)

    print('--F2--')
    aq2, e2 = quad(function2, a, b)
    ar2 = rectangleApproximation('f2',n,a,b)
    ad2 = abs(aq2-ar2)
    print(aq2, ar2, ad2)

    print('--F3--')
    aq3, e3 = quad(function3, a, b)
    ar3 = rectangleApproximation('f3',n,a,b)
    ad3 = abs(aq3-ar3)
    print(aq3, ar3, ad3)

    assert ad1 < 3,'Function 1 approximation is too big'
    assert ad2 < 3,'Function 2 approximation is too big'
    assert ad3 < 3,'Function 3 approximation is too big'
    print('All passed\n')
