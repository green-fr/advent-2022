# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

with open('22.input small.txt', 'r') as file:
    counter = 0;
    lines = file.readlines()
maze2D = [lines[i].rstrip() for i in range(len(lines) - 2)]
n = 4
maze3D = []
maze3D.append([maze2D[i][n * 2 : n * 3] for i in range(n * 0, n * 1)])
maze3D.append([maze2D[i][n * 0 : n * 1] for i in range(n * 1, n * 2)])
maze3D.append([maze2D[i][n * 1 : n * 2] for i in range(n * 1, n * 2)])
maze3D.append([maze2D[i][n * 2 : n * 3] for i in range(n * 1, n * 2)])
maze3D.append([maze2D[i][n * 2 : n * 3] for i in range(n * 2, n * 3)])
maze3D.append([maze2D[i][n * 3 : n * 4] for i in range(n * 2, n * 3)])
for plan in maze3D:
    for line in plan:
        print(line)
    print()
path = lines[-1]
pathParsed = []
currentGroup = ''
currentChars = False
for char in path:
    if char.isalpha():
        if (not currentChars):
            currentChars = True
            pathParsed.append(int(currentGroup))
            currentGroup = ''
        currentGroup += char
    elif char.isdigit():
        if (currentChars):
            currentChars = False
            pathParsed.append(currentGroup)
            currentGroup = ''
        currentGroup += char
if (currentChars):
    pathParsed.append(currentGroup)
else:
    pathParsed.append(int(currentGroup))

# key = (face leaving, direction leaving)
# value = (face arriving, direction arriving)
# table made manually from the folding (different from one folding to another)
transition = {}
transition[(0, 0)] = (5, 2)
transition[(0, 1)] = (3, 1)
transition[(0, 2)] = (2, 1)
transition[(0, 3)] = (1, 1)
transition[(1, 0)] = (2, 0)
transition[(1, 1)] = (4, 3)
transition[(1, 2)] = (5, 3)
transition[(1, 3)] = (0, 1)
transition[(2, 0)] = (3, 0)
transition[(2, 1)] = (4, 0)
transition[(2, 2)] = (1, 2)
transition[(2, 3)] = (0, 0)
transition[(3, 0)] = (5, 1)
transition[(3, 1)] = (4, 1)
transition[(3, 2)] = (2, 2)
transition[(3, 3)] = (0, 3)
transition[(4, 0)] = (5, 0)
transition[(4, 1)] = (1, 3)
transition[(4, 2)] = (2, 3)
transition[(4, 3)] = (3, 3)
transition[(5, 0)] = (0, 2)
transition[(5, 1)] = (1, 0)
transition[(5, 2)] = (4, 2)
transition[(5, 3)] = (3, 2)
# key = (direction leaving, direction arriving)
# value = (newx, newy) function(x, y)
# table made manually (same for all foldings)
turn = {}
turn[(0, 0)] = lambda x, y: (0, y)
turn[(0, 1)] = lambda x, y: (n - 1 - y, 0)
turn[(0, 2)] = lambda x, y: (n - 1, n - 1 - y)
turn[(0, 3)] = lambda x, y: (y, n - 1)
turn[(1, 0)] = lambda x, y: (0, n - 1 - x)
turn[(1, 1)] = lambda x, y: (x, 0)
turn[(1, 2)] = lambda x, y: (n - 1, x)
turn[(1, 3)] = lambda x, y: (n - 1 - x, n - 1)
turn[(2, 0)] = lambda x, y: (0, n - 1 - y)
turn[(2, 1)] = lambda x, y: (y, 0)
turn[(2, 2)] = lambda x, y: (n - 1, y)
turn[(2, 3)] = lambda x, y: (n - 1 - y, n - 1)
turn[(3, 0)] = lambda x, y: (0, x)
turn[(3, 1)] = lambda x, y: (n - 1 - x, 0)
turn[(3, 2)] = lambda x, y: (n - 1, n - 1 - x)
turn[(3, 3)] = lambda x, y: (x, n - 1)

def findStartingPosition():
    for i, char in enumerate(maze3D[0][0]):
        if char not in [' ', '#']:
            return Position(0, 0, i, 0)

class Position:
    layer = None
    x = None
    y = None
    direction = None
    def __init__(self, layer, x, y, direction):
        self.layer = layer
        self.x = x
        self.y = y
        self.direction = direction
    def turnRight(self):
        self.direction = (self.direction + 1) % 4
    def turnLeft(self):
        self.direction = (self.direction - 1) % 4
    def move(self, steps):
        for i in range(steps):
            newPosition = Position(self.layer, self.x, self.y, self.direction)
            wrapping = False
            if (self.direction == 0):
                newPosition.x += 1
                if (newPosition.x == n): wrapping = True
            elif (self.direction == 1):
                newPosition.y += 1
                if (newPosition.y == n): wrapping = True
            elif (self.direction == 2):
                newPosition.x -= 1
                if (newPosition.x == -1): wrapping = True
            elif (self.direction == 3):
                newPosition.y -= 1
                if (newPosition.y == -1): wrapping = True
            if (wrapping):
                newPosition.layer, newPosition.direction = transition[(position.layer, position.direction)]
                newPosition.x, newPosition.y = turn[(position.direction, newPosition.direction)](position.x, position.y)
            if (maze3D[newPosition.layer][newPosition.y][newPosition.x] == '#'):
                break
            else:
                self.layer = newPosition.layer
                self.x = newPosition.x
                self.y = newPosition.y
                self.direction = newPosition.direction
    def __str__(self):
        return f"Position(layer={self.layer}, x={self.x}, y={self.y}, direction={self.direction})"

# function made manually, depends on folding
def unfoldPosition(position):
    if (position.layer == 0):
        return (2 * n + position.x, 0 * n + position.y)
    elif (position.layer == 1):
        return (0 * n + position.x, 1 * n + position.y)
    elif (position.layer == 2):
        return (1 * n + position.x, 1 * n + position.y)
    elif (position.layer == 3):
        return (2 * n + position.x, 1 * n + position.y)
    elif (position.layer == 4):
        return (2 * n + position.x, 2 * n + position.y)
    elif (position.layer == 5):
        return (3 * n + position.x, 2 * n + position.y)
position = findStartingPosition()
print(position)
for instruction in pathParsed:
    if (instruction == 'R'):
        position.turnRight()
    elif (instruction == 'L'):
        position.turnLeft()
    else:
        position.move(instruction)
    print(instruction, position)

(x, y) = unfoldPosition(position)
print((y + 1) * 1000 + (x + 1) * 4 + position.direction)
