import sys

exit_con = False


def getMode():
    try:
        modes = [1,0,2]
        user_mode = int(input('What mode do you want to be in, Programmer = 0, Scientific = 1, Exit = 2? '))
        if user_mode in modes:
            return user_mode
        else:
            print('Please put a 0 or a 1 specifying what mode you want to be in!')
            return getMode()
    except ValueError as e:
        print('WARNING: You did not put in a number! \nGot exception %s ' % e)

def decmToBinary():
    try:

        decimal = int(input('Please enter a decimal number which you would like converted to binary: '))

        #print(decimal)

        if decimal <= 0:
            print('Please input a POSITIVE decimal number')
            return decmToBinary()
        else:
            curr_num = decimal
            bin_num = []

            while True:
                if curr_num == 0:
                    break
                quotient = curr_num // 2
                bin_num.append(curr_num % 2)
                curr_num = quotient
            #print(bin_num)
            bin_num.reverse()
            bin_num = ''.join(str(e) for e in bin_num)
            return bin_num
    except ValueError as e:
        print('WARNING: Did not get a number input! \nGot exception %s' % e)
        #sys.exit(1)

def doMath():
    try:
        num1 = float(input('Enter your first operand: '))
        num2 = float(input('Enter your second operand: '))

        operators = ['+','-','*','/','**']
        user_operator = input('What operator do you wish to use? (%s) ' % ', '.join(operators))

        if user_operator not in operators:
            print('Please specify an operator from this list %s ' % ', '.join(operators))
        else:
            if user_operator == '+':
                print(str(num1) + ' + ' + str(num2) + ' = ' + str(num1+num2))
            elif user_operator == '-':
                print(str(num1) + ' - ' + str(num2) + ' = ' + str(num1-num2))
            elif user_operator == '*':
                print(str(num1) + ' * ' + str(num2) + ' = ' + str(num1*num2))
            elif user_operator == '/':
                print(str(num1) + ' / ' + str(num2) + ' = ' + str(num1/num2))
            elif user_operator == '**':
                print(str(num1) + ' ** ' + str(num2) + ' = ' + str(num1**num2))
    except ValueError as e:
        print('WARNING: Did not get a number! \nGot an exception %s ' % e)




while not exit_con:
    curr_mode = getMode()
    if curr_mode == 2:
        break
        exit_con = True


    if(curr_mode == 0):
        # Programmer
        '''
        In programmer mode, the user can enter any unsigned decimal number to convert to binary.
        Hint: you could find the left starting bit by increasing the exponent while the number is greater than equal to 2** exponent.
        '''
        bin_num = decmToBinary()
        if bin_num is not None:
            print('The binary equivalent is %s' % str(bin_num))
        #print('The binary equivalent is %s!' % str(decmToBinary()))
    elif curr_mode == 1:
        #Scientific
        '''
        In scientific mode, the user can choose between the follow mathematical operations: +,-,*/, and **. All operators are binary so the user must be prompted for two operands following the operator. These operands can be integers or floating-point numbers. You need to print an error message for the
        selection of a bad mathematical operatiom, i.e. invalid selection.
        '''
        doMath()
