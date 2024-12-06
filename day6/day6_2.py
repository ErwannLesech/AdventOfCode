import sys

file = open('data.txt')
gridContent = []
while True:
    line = file.readline()
    if not line:
        break
    gridContent.append(line)
    
grid = [['' for j in range (len(gridContent[i]))] for i in range (len(gridContent))]

for i in range (len(gridContent)):
    for j in range (len(gridContent[i])):
        grid[i][j] = gridContent[i][j]

def colorPatrol(grid, i, j, direction): 
    while True:
        if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i])):
            return

        grid[i][j] = 'X'

        if (direction == 'UP'):
            if (i - 1 >= 0 and grid[i-1][j] == '#'):
                return colorPatrol(grid, i, j+1, 'RIGHT')
            else:
                i -= 1 

        elif (direction == 'RIGHT'):
            if (j + 1 < len(grid[i]) and grid[i][j+1] == '#'):
                return colorPatrol(grid, i+1, j, 'DOWN')
            else:
                j += 1
        
        elif (direction == 'DOWN'):
            if (i + 1 < len(grid) and grid[i+1][j] == '#'):
                return colorPatrol(grid, i, j-1, 'LEFT')
            else:
                i += 1

        elif (direction == 'LEFT'):
            if (j - 1 >= 0 and grid[i][j-1] == '#'):
                return colorPatrol(grid, i-1, j, 'UP')
            else:
                j -= 1

def countPatrol(grid):
    distinctCount = 0
    for line in grid:
        # print(line, file=sys.stderr)
        for cell in line:
            if cell == 'X':
                distinctCount += 1

    return distinctCount

for i in range (len(grid)):
    for j in range (len(grid[i])):
        if(grid[i][j] == '^'):
            grid[i][j] = 'X'
            colorPatrol(grid, i, j, 'UP')
            print(countPatrol(grid))
            