#advent of code
#day 2
from sys import *


def getNextPos(currPos, directions):
   # print(currPos)
    for d in directions:
        #x values aka left right
        if d == "L" and currPos[1] != 0:
            #print(currPos[1])
            currPos[1] -= 1
        elif d == "R" and currPos[1] != 2:
            currPos[1] += 1        
        #y values aka up and down
        elif d == "U" and currPos[0] != 0:
            currPos[0] -= 1
        elif d == "D" and currPos[0] != 2:
            currPos[0] += 1
        #print(currPos)
    return currPos

def getNum(pos):
    #print(pos)
    keypad = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    
    return keypad[pos[0]][pos[1]]

def main():
    instructions = []
    for line in stdin:
        instructions.append(line)
    
    print(instructions)
    code = ""
    currPos = [1,1]
    for num in instructions:
        code += str(getNum(getNextPos(currPos, num)))
    print(code)
main()
    
    
    
