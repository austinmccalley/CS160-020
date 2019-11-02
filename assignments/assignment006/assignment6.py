'''
Flow:
    User pics which function (1, 2, 3)
    Pick approximation method(Recatangle or Trapezoidal)
'''


def pickFunction():
    print('f1: f1(x) = 10x^2')
    print('f2: f2(x) = 2x^2 - 5')
    print('f3: f3(x) = x + 20')

    function_names = ['f1','f2','f3']
    user_in = input('Please pick a function from above to run an integration on: ')

    if user_in not in function_names:
        print('Please try again. The function you picked was not in the pre-approved list')
        return pickFunction()
    else:
        return user_in


def pickApproximation():
    print('We are going to use trapezoidal(T) or rectangle(R) method. If you wish to quit use Q')

    approximation_names = ['t','r', 'T', 'R', 'Q', 'q']

    user_in = input('Please pick which approximation you would like to use: ')

    if user_in not in approximation_names:
        print('Please try again. You did not pick a valid approximation name.')
        return pickApproximation()
    else:
        return user_in.lower()


def function1(x):
    ans = 10.0*x**2.0
    return ans

def function2(x):
    return 2.0*x**2.0 - 5.0

def function3(x):
    return x + 20.0

def rectangleApproximation(func,number_rectangles,a_point,b_point):
    try:

        diff = b_point - a_point
        interval = diff / number_rectangles

        if func == 'f1':
            # f1(x) = 10x^2

            summation = 0
            for x in range(1, number_rectangles+1):
                eval_point = a_point+(interval*x)
                summation += function1(eval_point)

            return interval  * summation

        elif func == 'f2':
            # f2(x) = 2x^2 - 5

            summation = 0
            for x in range(1, number_rectangles +1):
                eval_point = a_point+(interval*x)
                summation += function2(eval_point)

            return interval * summation

        elif func == 'f3':
            # f3(x) = x + 20

            summation = 0
            for x in range(1, number_rectangles+1):
                eval_point = a_point+(interval*x)
                summation += function3(eval_point)

            return interval * summation

        else:
            print('What did you do? We are going to try this again!')
            return rectangleApproximation(func)

    except Exception as e:
        print('We got an exception: %s! Lets try this again' % e)
        return rectangleApproximation(func)



def trapezoidalApproximation(func,number_trapezoids,a_point,b_point):
    try:

        diff = b_point - a_point

        interval = diff / number_trapezoids

        if func == 'f1':
            # f1(x) = 10x^2

            summation = 0
            for x in range(0, number_trapezoids+1):
                eval_point = a_point+(interval*x)
                if x == 0  or x == number_trapezoids:
                    summation += function1(eval_point)
                else:
                    summation += 2.0*function1(eval_point)
            return (interval/2) * summation

        elif func == 'f2':
            # f2(x) = 2x^2 - 5

            summation = 0
            for x in range(0, number_trapezoids+1):
                eval_point = a_point+(interval*x)
                if x == 0 or x == number_trapezoids:
                    summation += function2(eval_point)
                else:
                    summation += 2.0*function2(eval_point)
            return (interval/2) * summation

        elif func == 'f3':
            # f3(x) = x + 20

            summation = 0
            for x in range(0, number_trapezoids+1):
                eval_point = a_point+(interval*x)
                if x == 0 or x == number_trapezoids:
                    summation += function3(eval_point)
                else:
                    summation += 2.0*function3(eval_point)
            return (interval/2) * summation

    except Exception as e:
        print(e)
        print('We got an exception: %s! Lets try this again!' % e)
        return trapezoidalApproximation(func)


def main():
    while True:
        function = pickFunction()
        approximation = pickApproximation()

        if approximation == 'r':
            number_rectangles = int(input('How many rectangles would you like to approximate with? '))
            if number_rectangles <= 0:
                print('Make sure the number of rectangles is greater than 0')
                main()
            else:
                a_point = int(input('Which x-value do you wish to start at? '))
                b_point = int(input('Which x-value do you wish to end with? '))
                if a_point == 0 and b_point == 0:
                    print('Lets try this again and ensure you find an intergral greater difference than 0')
                    main()
                else:
                    approx = rectangleApproximation(function,number_rectangles, a_point, b_point)
                    print('We got an approximation of %s for the function you requested!' % approx )
        elif approximation == 't':
            number_trapezoids = int(input('How many trapezoids would you like to approximate with? '))
            if number_trapezoids <= 0:
                print('Make sure the number of trapezoids is greater than 0')
                main()
            else:
                a_point = int(input('Which x-value do you wish to start at? '))
                b_point = int(input('Which x-value do you wish to end with? '))
                if a_point == 0 and b_point == 0:
                    print('Lets try this again and ensure you find an intergral greater difference than 0')
                    main()
                else:
                    approx = trapezoidalApproximation(function, number_trapezoids, a_point, b_point)
                    print('We got an approximation of %s for the function you requested!' % approx )
        elif approximation == 'q':
            break


if __name__ == "__main__":
    main()
