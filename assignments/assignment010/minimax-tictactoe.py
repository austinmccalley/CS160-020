from math import inf as infinity

def is_int(s):
    negative = True if s[:1] == '-' else False
    if negative:
        return False
    else:
        for c in s:
            if not(c >= '0' and c <= '9'):
                return False
        return True


def withinRange(n, r):
    return n <= r


def calcPrimes(n):
    primes = []
    i = 0
    while len(primes) < n:
        if isPrime(i):
            primes.append(i)
        i += 1
    return primes


def isPrime(n):
    if (n <= 1):
        return False
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True


def calcPGrid(c, r):
    grid = []
    primes = calcPrimes(c*r)
    pn = 0
    for x in range(r):
        grid.append([])
        for y in range(c):
            grid[x].append(primes[pn])
            pn += 1
    return grid


def multList(l):
    res = 1
    for x in l:
        res = res * x
    return res


def calcWins(n, grid):
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


def parseGrid(grid, plays):
    xs, os, pn = 1, 1, 0
    for y in range(len(grid)):
        for x in range(len(grid)):
            if plays[x][y] == 'X':
                xs *= grid[x][y]
            if plays[x][y] == 'O':
                os *= grid[x][y]
    return xs, os


def checkWins(wins, n, xs, os):
    primes = calcPrimes(n)
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


def initBGrid(r, c):
    grid = []
    for x in range(r):
        grid.append([])
        for y in range(c):
            grid[x].append("_")
    return grid


def makePlay(play, grid):
    """ 
     - Get User input
     - Pass in whos play it is
     - Set play grid at cords to play
     - Return play grid
    """
    print('Player numer %s, ' % play)

    gl = str(len(grid[0])-1)

    cin = input('What column do you want to play in? (0-%s) ' % gl)
    rin = input('What row do you want to play in? (0-%s) ' % gl)

    if(not is_int(cin)):
        print('Please check to ensure that your column is an integer')
        makePlay(play, grid)
    elif(not is_int(rin)):
        print('Please make sure your row is an integer')
        makePlay(play, grid)
    else:
        cin = int(cin)
        rin = int(rin)
        if not withinRange(cin, len(grid[0])-1) and withinRange(rin, len(grid[0])-1):
            print('Your coloumns or rows is not within the range of 0 to %s' % gl)
            makePlay(play, grid)
        else:
            if play == 0:
                if grid[rin][cin] == '_':
                    grid[rin][cin] = 'X'
                else:
                    print('Theres already a play there! Try that again!')
                    makePlay(play, grid)
            else:
                if grid[rin][cin] == '_':
                    grid[rin][cin] = 'O'
                else:
                    print('Theres already a play there! Try that again!')
                    makePlay(play, grid)


def copy_grid(grid):
    return grid[:]


def printGrid(grid):
    """
     - Get grid size
     - For each col in a row
     - Seperate and print each elm with a space
    """
    for r in grid:
        print(' | '.join(str(e) for e in r))


def play_move(state, player, block_num):
    if state[int((block_num-1)/3)][(block_num-1) % 3] is '_':
        state[int((block_num-1)/3)][(block_num-1) % 3] = player
    else:
        print(state[int((block_num-1)/3)][(block_num-1) % 3])
        block_num = int(
            input("Cell is filled try again!"))
        play_move(state, player, block_num)


def getBestMove(grid, pgrid, player, windict):
    """  
    Minimax Algorithm

    AI is O
    """
    n = len(grid[0])
    xs, os = parseGrid(grid, pgrid)
    w = checkWins(windict, n**2, xs, os)

    if w['x']:
        return -1
    if w['o']:
        return 1
    if w['t']:
        return 0

    moves = []
    empty_cells = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '_':
                indx = i*(n) + (j+1)
                empty_cells.append(indx)
    
    for empty_cell in empty_cells:
        move = {}
        move['index'] = empty_cell
        new_state = copy_grid(grid)
        play_move(new_state, player, empty_cell)
        
        if player == 0: # If human
            result = getBestMove(new_state, pgrid, player, windict)
            move['score'] = result
        else: # Else AI
            result = getBestMove(new_state, pgrid, player, windict)
            move['score'] = result
        
        moves.append(move)
    
    # Find best move
    best_move = None
    if player == 1:   # If AI player
        best = -infinity
        for move in moves:
            if move['score'] > best:
                best = move['score']
                best_move = move['index']
    else:
        best = infinity
        for move in moves:
            if move['score'] < best:
                best = move['score']
                best_move = move['index']
    
    return best_move


def main():

    cin = input('What size grid do you want to play with? ')

    if not is_int(cin):
        print('You did enter an integer of how big you want the grid to be')
        main()
    else:
        cin = int(cin)

        pin = input('Do you want to play with two players or one player? ')
        if not is_int(pin) or (pin not in ['1', '2']):
            print('Please specify 1 for one player or 2 for two players')
            return main()
        pin = int(pin)

        pgrid = initBGrid(cin, cin)
        grid = calcPGrid(cin, cin)

        win = False
        windict = calcWins(cin, grid)

        printGrid(pgrid)

        # NOTE: pin is how many players
        if pin == 1:
            play = 0
            while not win:
                if play == 0:
                    makePlay(play, grid)
                    printGrid(pgrid)
                    xs, os = parseGrid(grid, pgrid)
                    w = checkWins(windict, cin**2, xs, os)
                    getBestMove(pgrid, grid, play, windict)
                
                if play == 1:
                    choice = getBestMove(pgrid, grid, play, windict)
                    play_move(grid, play, choice)
                    
                xs, os = parseGrid(grid, pgrid)
                w = checkWins(windict, cin**2, xs, os)
                getBestMove(pgrid, grid, play, windict)

                if w['x']:
                    win = True
                    print('Player 0 has won!')
                    break
                if w['o']:
                    win = True
                    print('Player 1 has won!')
                    break
                if w['t']:
                    win = True
                    print('There is a tie!')
                    break
                if play == 0:
                    play = 1
                else:
                    play = 0
                    
        else:
            play = 0
            while not win:
                makePlay(play, pgrid)
                printGrid(pgrid)
                xs, os = parseGrid(grid, pgrid)
                w = checkWins(windict, cin**2, xs, os)
                getBestMove(pgrid, grid, play, windict)

                if w['x']:
                    win = True
                    print('Player 0 has won!')
                    break
                if w['o']:
                    win = True
                    print('Player 1 has won!')
                    break
                if w['t']:
                    win = True
                    print('There is a tie!')
                    break
                if play == 0:
                    play = 1
                else:
                    play = 0


main()
