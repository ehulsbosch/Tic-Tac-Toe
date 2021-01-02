# Get the user input and convert it to a nest list
grid = []
grid[:0] = ' ' * 9
lines = [grid[0:3], grid[3:6], grid[6:9]]
horizontalruler = '---------'
move = 0


def getplayer():
    global move
    move = move + 1
    if move % 2 == 0:
        return 'O'
    else:
        return 'X'


# Check if the user input is correct and usable
def checkifcoordiscorrect(x, y):
    try:
        x = int(x)
        y = int(y)
    except:
        print('You should enter numbers!')
        return None, None, False
    if isinstance(x, int) and isinstance(y, int):
        if (x > 0 and x < 4) and (y > 0 and y < 4):
            return x, y, True
        else:
            print('Coordinates should be from 1 to 3!')
            return None, None, False


# Update the grid using the user's input
def updategrid(x, y):
    if not lines[x-1][y-1] in ('X', 'O'):
        lines[x - 1][y - 1] = getplayer()
        printgrid(lines)
        return True
    else:
        print('This cell is occupied! Choose another one!')
        return False


# Print the grid
def printgrid(line):
    print(horizontalruler)
    for i in line:
        print('{} {} {} {} {}'.format('|', i[0], i[1], i[2], '|'))
    print(horizontalruler)


# Defines which player's turn it is
def checkifcorrectplayer(element):
    if element == 'X' or element == 'O':
        return True
    else:
        return False


# Checking if there is a horizontal match on any of the lines
def checkhorizontal(lines):
    winners = []
    for index, line in enumerate(lines):
        if line.count(line[0]) == len(line) and checkifcorrectplayer(line[0]):
            winners.extend([[line[0], 'horizontal', index]])
    return winners


# Checking if there is a vertical match on any of the columns
def checkvertical(lines):
    winners = []
    for index, value in enumerate(lines[0]):
        if value == lines[1][index] == lines[2][index] and checkifcorrectplayer(value):
            winners.extend([[value, 'vertical', index]])
    return winners


# Checking if there is a diagonal match on the first row / first column and first row / last column
def checkdiagonal(lines):
    winners = []
    if lines[0][0] == lines[1][1] == lines[2][2] and checkifcorrectplayer(lines[0][0]):
        winners.extend([[lines[0][0], 'diagonal', '0']])
    if lines[0][2] == lines[1][1] == lines[2][0] and checkifcorrectplayer(lines[0][2]):
        winners.extend([[lines[2][0], 'diagonal', '2']])

    return winners


# Checking if the number of hits for X and O are possible as well as checking if the game is finished
def checkifpossible(lines):
    xes = 0
    os = 0
    others = 0
    for index, line in enumerate(lines):
        for i, value in enumerate(line):
            if value == 'X':
                xes = xes + 1
            elif value == 'O':
                os = os + 1
            else:
                others = others + 1

    valid = False
    finished = False
    if xes - os in (-1, 0, 1):
        valid = True
    if others == 0:
        finished = True

    return valid, finished


# The main function that checks if there is a winner
def checkwinner(lines):
    global hasmoved
    matches = []
    matches.extend(checkhorizontal(lines))
    matches.extend(checkvertical(lines))
    matches.extend(checkdiagonal(lines))
    valid, finished = checkifpossible(lines)

    if not valid:
        print('Impossible: invalid')
    elif len(matches) == 1:
        print('{} wins'.format(matches[0][0]))
    elif len(matches) > 1:
        print('Impossible: too many matches')
    elif not finished:
        # print('Game not finished')
        askforcoords()
    else:
        print('Draw')
    # elif len(matches) == 0:


def askforcoords():
    xinput, yinput = [x for x in input("Enter the coordinates: ").split()]
    xcord, ycord, correct = checkifcoordiscorrect(xinput, yinput)
    if correct:
        moved = updategrid(xcord, ycord)
        if moved:
            checkwinner(lines)
        else:
            askforcoords()
    else:
        askforcoords()


printgrid(lines)
askforcoords()



