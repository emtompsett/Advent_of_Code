#advent of code day 1
import math
def getNextDir(current, next):
    if next == "L":
        current += 90
    else:
        current -= 90
    return current % 360
        
def getDirectionPosition(current):
    pos = 0
    if current == 0:
        pos = 0
    elif current == 90:
        pos = 1
    elif current == 180:
        pos = 2
    else:
        pos = 3
    return (pos)
    
def getDistance(cardinals):
    print(cardinals)
    x = cardinals[0] - cardinals[2]
    y = cardinals[1] - cardinals[3]
    print(x,y)
    return abs(x) + abs(y)

def splitDirAndDist(directions):
    tupDirs = []
    for dir in directions:
        lOrR = dir[0]
        dist = int(dir[1:])
        tupDirs.append((lOrR, dist))
    return tupDirs

def main():
    dists = [0, 0, 0, 0] #west, north, east, south
    dirs = input()
    dirs = dirs.split(", ")
    dirs = splitDirAndDist(dirs);
    currDir = 90
    for dir in dirs:
        currDir = getNextDir(currDir, dir[0])
        #print(currDir)
        position = getDirectionPosition(currDir);
        #print(add)
        dists[position] += int(dir[1])
    print(abs(getDistance(dists)))

main()
        
    
        

