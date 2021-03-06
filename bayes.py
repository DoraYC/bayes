
# coding: utf-8

# In[37]:


from numpy import *
import re

def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problem', 'help', 'please'],
                  ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                  ['my','dalmation', 'is', 'so', 'cute', 'I', 'love', 'hime'],
                  ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                  ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                  ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec =[0, 1, 0, 1, 0, 1]
#     postingList = [[1, 1, 1, 1,1, 2,2,2,2,2,2,3,3,3,3,3],
#                   ['S','L','M','M','S', 'L','S','S','L','L','M','M','L','S','M','M']]
#     classVec = [-1,1,1,-1,-1,1,1,-1,1,-1,1,1,1,1,-1,1]
    return postingList, classVec

def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
#         print('document:')
#         print(document)
#         print("vocabSet before:")
#         print(vocabSet)
        vocabSet = vocabSet | set(document)
#         print("vocabSet after:")
#         print(vocabSet)
    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print("the word: %s is not in my vocabulary!" % word)
    return returnVec

def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec



def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = ones(numWords); p1Num = ones(numWords)
    p0Denom = 2.0; p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)
    p0Vect = log(p0Num/p0Denom)
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0
    
def testingNB():
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNB0(array(trainMat), array(listClasses))
#     testEntry = ['love', 'my', 'dalmation']
    testEntry = [2, 'S']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))
#     testEntry = ['stupid', 'garbage']
#     thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
#     print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))
  
def textParse(bigString):
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]

def spamTest():
    docList = []; classList = []; fullText = []
    for i in range(1, 26):
        wordList = textParse(open('email/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)
    trainingSet = list(range(50)); testSet = []
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat = []; trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat),array(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = setOfWords2Vec(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
    errorRate = float(errorCount)/len(testSet)
    print('the error rate is: ', errorRate)
    if errorRate > 0.0:
        print('classification error', testSet)



if __name__ == '__main__':
    spamTest()
#     listOPosts, listClasses = loadDataSet()
#     myVocabList = createVocabList(listOPosts)
#     print(myVocabList)
#     trainMat = []
#     for postinDoc in listOPosts:
#         trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
#     p0V, p1V, pAb = trainNB0(trainMat, listClasses)
#     print("-----------")
#     print(p0V)
#     print(p1V)
#     print(pAb)
#     vec = setOfWords2Vec(myVocabList, listOPosts[3])
#     print(vec)

#     testingNB()
    


# In[30]:


postingList = [['my', 'dog', 'has', 'flea', 'problem', 'help', 'please'],
                  ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid']]
type(postingList)
postingList[:]


# In[13]:


import re
regEx = re.compile('\\W*')
mySent = 'This book is the best book on Python or M.L. I have ever laid eyes upon.'
listOfTokens = regEx.split(mySent)
[tok.lower() for tok in listOfTokens if len(tok)>0]


# In[18]:


import re
regEx = re.compile('\\W*')
emailText = open('email/ham/6.txt').read()
listOfTokens = regEx.split(emailText)
listOfTokens

