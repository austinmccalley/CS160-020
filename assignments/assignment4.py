def getMode():
    modes = [1,0]
    user_mode = int(input('What mode do you want to be in, Programmer = 0, Scientific = 1? '))
    if user_mode in modes:
        return user_mode
    else:
        print('Please put a 0 or a 1 specifying what mode you want to be in!')
        return getMode()

    #return int(input('What mode you want to be in(Programmer 0, Scientific 1)? '))


def decmToBinary():
    decimal = int(input('Please enter a decimal number which you would like converted to binary: '))
    if decimal < 0:
        decmToBinary()
    else:
        curr_num = decimal
        bin_num = []

        while True:
            if curr_num == 0:
                break
            quotient = curr_num // 2
            bin_num.append(curr_num % 2)
            curr_num = quotient
        bin_num.reverse()
        bin_num = ''.join(str(e) for e in bin_num)
        return bin_num


curr_mode = getMode()

# Programmer
'''
In programmer mode, the user can enter any unsigned decimal number to convert to binary.
Hint: you could find the left starting bit by increasing the exponent while the number is greater than equal to 2** exponent.
'''
if(curr_mode == 0):
    print('The binary equivalent is %s!' % str(decmToBinary()))
elif curr_mode == 1:
    #Scientific
    '''
    In scientific mode, the user can choose between the follow mathematical operations: +,-,*/, and **. All operators are binary so the user must be prompted for two operands following the operator. These operands can be integers or floating-point numbers. You need to print an error message for the
    selection of a bad mathematical operatiom, i.e. invalid selection.
    '''
    operators = ['+','-','*','/','**']

    #TODO: Get
