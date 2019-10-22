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
    print('Please pick either trapezoidal(T) or rectangle(R) method.')


function = pickFunction()


