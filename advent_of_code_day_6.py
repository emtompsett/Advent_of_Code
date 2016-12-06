
from sys import stdin

def getMaxLetter(countList):
    max = 0
    index = 0
    for i in range(len(countList)):
        if countList[i] > max:
            index = i
            max = countList[i]
    
    return getLetter(index);

def getLetterPos(letter):
    alpha = "abcdefghijklmnopqrstuvwxyz";    
    return alpha.find(letter)

def getLetter(pos):
    alpha = "abcdefghijklmnopqrstuvwxyz";    
    return alpha[pos];

def getLetterCounts(data, col):
    letterFreq = [0] * 26;
    for i in range(len(data)):
        row = data[i]
        pos = getLetterPos(row[col])
        letterFreq[pos] += 1
    return letterFreq

def main():
    l = ""
    data = [];

    for line in stdin:
        l = list(line)
        l.remove('\n');
        data.append(l);

    print(data);
    str = ""
    for i in range(len(data[0])):
        str += getMaxLetter(getLetterCounts(data, i));
    print(str);

main()
