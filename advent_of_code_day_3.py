#advent of code
#day 3
from sys import stdin

def isTriangle(tup):
    if tup[0] + tup[1] > tup[2]:
        return True
    return False

def sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst

def getTuple(line):
    return [int(line[2:5]), int(line[7:10]), int(line[12:])]
    

def main():
    count = 0
    for line in stdin:
        tri = sort(getTuple(line))
        print(tri)
        if isTriangle(tri):
            count += 1
    print(count)        

main()
    
    
