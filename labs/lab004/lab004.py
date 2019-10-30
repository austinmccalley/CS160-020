import random


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

def testMode():
    allowed_functions = ['f1','f2','f3', 'C']
    for x in range(0, len(allowed_functions)):
        func = allowed_functions[x]
        a = random.randint(0, 250)
        b = random.randint(0, 250)
        print(summation(func, a, b))
        print(list(range(a,b)))
        print(sum(list()))

        ourResult = summation(func, a, b)
        thereResult = sum(list(range(a,b)))

        assert ourResult == thereResult


def getFunctionWanted():
    print('f1: f1(x)=10x^2')
    print('f2: f2(x)=2x^2-5')
    print('f3: f3(x)=x+20')
    print('To cancel use C')
    #print('To run random tests use T')
    allowed_functions = ['f1','f2','f3', 'C', 'T']
    func = input("What function would you like to chose? ")

    if func not in allowed_functions:
        print('Please restart the program with a function that is defined above!')
        return getFunctionWanted()
    return func


while True:
    func = getFunctionWanted()
    if func == 'C':
        break
    if func == 'T':
        testMode()
    else:
        a = int(input('What starting value do you want to use? '))
        b = int(input('What ending value do you want to use? '))
        print('We got the summation %s!' % str(summation(func, a, b)))

