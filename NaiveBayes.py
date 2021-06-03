from math import sqrt

def __init__(self, classes):
    self.classes = classes

def getMean(numList):
    return sum(numList) / float(len(numList))

def getStdev(numList):
    mean = getMean(numList)
    variance = sum([(x-mean)**2 for x in numList]) / float(len(numList)-1)
    return sqrt(variance)

# Find probability class per term
def findValueOfTerm(term, oppositeClassList):
    termInOppositeClass = findTermInLibrary(oppositeClassList);
    return (term[1] + 1) / (term[1]+1 + termInOppositeClass[1]+1)

# Find term's tuple in a given library
def findTermInLibrary(term, library):
    for pair in library:
        if term == pair[0]:
            return pair
    return ("a", 0)

def findProbabilityOfTermInClass():
    

def train(self, dataset, labels):
    return