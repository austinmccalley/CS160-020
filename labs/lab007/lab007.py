import random

def is_int(s):
    negative = True if s[:1] == '-' else False
    if negative:
        return False
    else:
        for c in s:
            if not(c>='0' and c<='9'):
                return False
        return True

def generateRandomNumbers(amount):
    rn = []
    for i in range(amount):
        rannum = genRanNum(1,100)
        if not checkIn(rn, rannum):
            rannum = genRanNum(1,100)
        rn.append(rannum)
    return rn

def generateRandomNumbersList(amount):
    list_100 = list(range(1,100))
    random.shuffle(list_100)
    rn = []
    erange = 100 - amount
    si = genRanNum(0, erange)
    for x in range(amount):
        num = list_100[si+x]
        rn.append(num)
    return rn


def genRanNum(a,b):
    return random.randint(a,b)

def getUserGuesses():
    u_in = input("How many guesses do you think that'll it take to guess a number out of the five random numbers? ")
    if len(u_in) == 0:
        print('You did not give a number for the amount of guesses')
        return getUserGuesses()
    if not is_int(u_in):
        print('You did not give the program a positive integer! Lets try it again')
        return getUserGuesses()
    else:
        return int(u_in)




def checkIn(arr, num):
    return num in arr

def getGuess():
    u_in = input("What number do you think will be in the list of random numbers? ")
    if not is_int(u_in):
        print('You did not give the program a positive integer! Lets try this again.')
    else:
        return int(u_in)


def main():
    rn = generateRandomNumbersList(5)
    u_guess = getUserGuesses()
    gn = False
    for i in range(u_guess):
        guess = getGuess()
        if checkIn(rn, guess):
            print('You got a number!')
            gn = True
            print('The rest of the numbers are:')
            print(rn)
            break
    if not gn:
        print('You did not guess any of the five numbers that were in the list. They are:')
        print(rn)

main()
