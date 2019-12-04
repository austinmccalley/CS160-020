import random

# 10 lines
def is_int(s):
    """  
     - Take in a string
     - We are only checking for positive integers
     - Iterate over each character
     - If a character is not between the ASCII characters 0 and 9 return false
     - Return true after ALL checks
    """
    if s == '':
        return False
    negative = True if s[:1] == '-' else False
    if negative:
        return False
    else:
        for c in s:
            if not(c >= '0' and c <= '9'):
                return False
        return True

# 1 line
def withinRange(n, r):
    """  
     - See if n is less than or equal to r
    """
    return n <= r

# 7 lines
def calcPrimes(n):
    """  
     - Take in a number of primes wanted, n
     - Increase i by one while we have less than n amount of primes
     - Return all primes once we get to n primes
    """
    primes = []
    i = 0
    while len(primes) < n:
        if isPrime(i):
            primes.append(i)
        i += 1
    return primes

# 6 lines
def isPrime(n):
    """  
     - Take in a number n
     - If n is less than or equal to 1 it isn't a prime
     - Iterate over all numbers from 2 to n
        - If any number other than 1 or itself is evenly divisible with n then it isn't a prime
    - Return true if the number passes ALL checks 
    """
    if (n <= 1):
        return False
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

# 9 lines
def calcPGrid(c, r):
    """  
    - Take in the number of columns and rows, c and r
    - Calculate all the primes for a grid of c by r
    - For each row add a new column
    - For each cell add a prime at some index pn
    - Increase pn by 1
    - Return the grid of primes
    """
    grid = []
    primes = calcPrimes(c*r)
    pn = 0
    for x in range(r):
        grid.append([])
        for y in range(c):
            grid[x].append(primes[pn])
            pn += 1
    return grid

# 4 lines
def multList(l):
    """  
    - Take in a list l
    - PI the list together
    - Return the result
    """
    res = 1
    for x in l:
        res = res * x
    return res

# 14 lines
def calcWins(n, grid):
    """  
    - Create a dictionary of all winning situations
    - Calculate the diganols of the grid
    - Calculate the no win situation(a tie)
    - Get all the across situations of winning
    - Get all the down situations of winning
    """
    wins = {}
    wins['fdiag'] = multList([row[i] for i, row in enumerate(grid)])
    wins['sdiag'] = multList([row[-i-1] for i, row in enumerate(grid)])
    wins['nowin'] = multList([j for sub in grid for j in sub])
    for y in range(n):
        for x in range(n):
            if x == 0:
                name = 'across-'+str(y)
                wins[name] = multList(grid[y])
            if y == 0:
                name = 'down-'+str(x)
                wins[name] = multList([el[x] for el in grid])
    return (wins)

# 8 lines
def parseGrid(grid, pgrid):
    """  
    - Take in the prime grid and the regular grid
    - PI the prime grid of where each marker is
    - Return the x-score and the o-score
    """
    xs, os = 1, 1
    for y in range(len(pgrid)):
        for x in range(len(pgrid)):
            if grid[x][y] == 'X':
                xs *= pgrid[x][y]
            if grid[x][y] == 'O':
                os *= pgrid[x][y]
    return xs, os

# 12 lines
def checkWins(wins, n, xs, os, pgrid):
    """  
    - Take in the winning situations
    - Take in the the amount of cells in the grid
    - Take in the x-score and the o-score
    - Take in the prime grid
    - Flatted the prime grid into a 1D list
    - Iterate over all items in the winning dictionary
    - Check to see if the tie situation is the two scores multiplied together are equal
    - Calculate the quotient for the x and o scores by each value in the winning dictionary
    - Check to see if the quotient is in primes and return true for them winning
    - If the qutoeint can be evenely divided then that player one
    """
    primes = [j for sub in pgrid for j in sub]
    for k, v in wins.items():
        if k == 'nowin':
            if v == xs*os:
                return {'x': False, 'o': False, 't': True}
        xdiv = xs / v
        odiv = os / v
        if xdiv in primes or str(xdiv).split('.')[1] == '0':
            return {'x': True, 'o': False, 't': False}
        elif odiv in primes or str(odiv).split('.')[1] == '0':
            return {'x': False, 'o': True, 't': False}
    return {'x': False, 'o': False, 't': False}

# 6 lines
def initBGrid(r, c):
    """  
    - Create a blank grid of r by c
    - For each row add c columns
    - For each cell add a _ as a palceholder
    """
    grid = []
    for x in range(r):
        grid.append([])
        for y in range(c):
            grid[x].append("_")
    return grid

# 4 lines
def compPlay(grid, m):
    """  
    - Take in the grid and the player marker
    - Randomly generate two numbers that are between 0 and the max spot in the grid
    - If we aren't able to place a marker
    """
    r = random.randint(0, len(grid)-1)
    c = random.randint(0, len(grid[r])-1)

    if placeMarker(grid, m, c, r):
        compPlay(grid, m)

# 5 lines
def placeMarker(grid, m, c ,r):
    if not grid[r][c] == "_":
        return True
    else:
        grid[r][c] = m
        return False

# 8 lines
def playMarker(grid, play, c, r):
    if play == 0:
        if placeMarker(grid, 'X',c, r):
            print('Theres already a play there! Try that again!')
            makePlay(play, grid)
    else:
        if placeMarker(grid, 'O',c, r):
            print('Theres already a play there! Try that again!')
            makePlay(play, grid)



# 14 lines
def makePlay(play, grid):
    """ 
     - Get User input
     - Pass in whos play it is
     - Set play grid at cords to play
     - Return play grid
    """
    gl = str(len(grid[0])-1)

    cin = input('Player #%s) What column do you want to play in? (0-%s) ' % (play, gl))
    rin = input('Player #%s) What row do you want to play in? (0-%s) ' % (play, gl))

    if(not is_int(cin) or (not is_int(rin))):
        print('Please check to ensure that your column and row are integers')
        makePlay(play, grid)
    else:
        cin = int(cin)
        rin = int(rin)
        if not withinRange(cin, len(grid[0])-1) and withinRange(rin, len(grid[0])-1):
            print('Your coloumns or rows is not within the range of 0 to %s' % gl)
            makePlay(play, grid)
        else:
            playMarker(grid, play, cin, rin)

# 2 lines
def printGrid(grid):
    """
     - Get grid size
     - For each col in a row
     - Seperate and print each elm with a space
    """
    for r in grid:
        print(' | '.join(str(e) for e in r))

# 15 lines
def parseWinning(w):
    """
     - Get the winning object
     - Check to see who won
     - Check to see if theres a tie
     - Return winner and if there was a win
    """
    win = False
    winner = -1
    if w['x']:
        win = True
        winner = 0
        print('Player 0 has won!')
    if w['o']:
        win = True
        winner = 1
        print('Player 1 has won!')
    if w['t']:
        win = True
        winner = 2
        print('There is a tie!')
    return win, winner

# 5 lines
def getCIN():
    cin = input('What size grid do you want to play with? ')
    if not is_int(cin):
        print('You did enter an integer of how big you want the grid to be')
        return main()
    return int(cin)

# 5 Lines
def getPIN():
    pin = input('Do you want to play with two players or one player? ')
    if not is_int(pin) or (pin not in ['1', '2']):
        print('Please specify 1 for one player or 2 for two players')
        return main()
    return int(pin)

# 1 line
def winInt(win, winner):
    return win

# 14 lines
def onePlayer(cin, pin, grid, pgrid, win, windict):
    play = 0
    while not win:
        if play == 0:
            printGrid(grid)
            makePlay(play, grid)
        if play == 1:
            compPlay(grid, 'O')
        xs, os = parseGrid(grid, pgrid)
        w = checkWins(windict, cin**2, xs, os, pgrid)
        win, winner = parseWinning(w)
        if winInt(win,winner):
            printGrid(grid)
            break
        play = 1 if (play==0) else 0

# 11 lines
def twoPlayer(cin, pin, grid, pgrid, win, windict):
    play = 0
    while not win:
        printGrid(grid)
        makePlay(play, grid)
        xs, os = parseGrid(grid, pgrid)
        w = checkWins(windict, cin**2, xs, os, pgrid)
        win, winner = parseWinning(w)
        if winInt(win,winner):
            printGrid(grid)
            break
        play = 1 if (play==0) else 0

# 7 lines
def main():
    cin, pin = getCIN(), getPIN()
    grid, pgrid = initBGrid(cin, cin), calcPGrid(cin, cin)
    win, windict = False, calcWins(cin, pgrid)

    if pin == 1:
        onePlayer(cin, pin, grid, pgrid, win, windict)
    else:
        twoPlayer(cin, pin, grid, pgrid, win, windict)

main()
