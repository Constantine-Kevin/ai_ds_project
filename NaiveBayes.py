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

def naivebayes(word_list,pos_dict,neg_dict):
    #Acumulator
    p_positive=0.5
    p_negative=0.5

    # Contains all the words in the dataset
    vocab_dict = {**pos_dict, **neg_dict}
    vocab_size = len(vocab_dict)

    for i in word_list:
        #P(i|positive)
        p_positive *= (pos_dict.get(i,0)+1)/(sum(pos_dict.values()) + vocab_size*(pos_zero_to_add+neg_zero_to_add) +pos_zero_to_add)
        #P(i|negative)
        p_negative *= (neg_dict.get(i,0)+1)/(sum(neg_dict.values()) + vocab_size + 1)
    
    if p_positive>p_negative:
        return "positive"
    else:
        return "negative"