#
# textmodel.py
#
# TextModel project!
#
# name(s): Yongchan Hong
#

from collections import defaultdict
import re
import string
from porter import create_stem
import math

TextModel1 = [ ]  # start with the empty list

words1 = defaultdict( int )  # default dictionary for counting
TextModel1 = TextModel1 + [ words1 ]  # add that dictionary in...

wordlengths1 = defaultdict( int )  # default dictionary for counting
TextModel1 = TextModel1 + [ wordlengths1 ]  # add that dictionary in...

stems1 = defaultdict( int )  # default dictionary for counting
TextModel1 = TextModel1 + [ stems1 ]  # add that dictionary in...

sentencelengths1 = defaultdict( int )  # default dictionary for counting
TextModel1 = TextModel1 + [ sentencelengths1 ]  # add that dictionary in...

punct1=defaultdict(int) #default dictionary for punctuation
TextModel1=TextModel1 + [punct1] #add that dictionary in...

# create one of your own...
# words1 = defaultdict( int )  # default dictionary for counting
# TextModel1 = TextModel1 + [ words1 ]  # add that dictionary in...

# a function to print all of the dictionaries in a TextModel1

def printAllDictionaries( TM ):
    """ a function to print all of the dictionaries in TM
        input: TM, a text model (a list of 5 or more dictionaries)
    """
    words = TM[0]
    wordlengths = TM[1]
    stems = TM[2]
    sentencelengths = TM[3]
    punct=TM[4]

    print("\nWords:\n", words)
    print("\nWord lengths:\n", wordlengths)
    print("\nStems:\n", stems)
    print("\nSentence lengths:\n", sentencelengths)
    print("\nPunctuation:\n", punct)
    print("\n\n")


# include other functions here...
def readTextFromFile(filename):
    '''read a text from file as a one long line'''
    f2=open(filename,"r")
    inputList=f2.readlines()
    f2.close()
    cleanList = list(map(lambda x: x.strip("\n"), inputList))
    answer="".join(cleanList)
    return answer


def makeSentenceLengths(s):
    '''return each lengths of the sentence from given text s'''
    endpoint=[]
    key=[]
    dictionary={}
    change1=re.split("[!.?]",s)
    for X in range(len(change1[:-1])):
        if X!=0:
            jump=0
            for num in change1[X]:
                if num==" ":
                    jump+=1
            endpoint.append(jump)
        else:
            jumping=1
            for num in change1[X]:
                if num==" ":
                    jumping+=1
            endpoint.append(jumping)
    for value in endpoint:
        if value in key:
            dictionary[value]+=1
        else:
            key.append(value)
            dictionary[value]=1
    return (dictionary)

def cleanString(s):
    '''delete all punctuation from given text s and return'''
    s=s.lower()
    for p in string.punctuation:
        s=s.replace(p,"")
    return (s)

def makeWordLengths(s):
    '''return the length of each word and how many times it shows up from the given text s by dict form'''
    wordlength=[]
    key=[]
    dictionary={}
    s=cleanString(s)
    split=s.split(" ")
    for word in split:
        length=len(word)
        wordlength.append(length)
    for value in wordlength:
        if value in key:
            dictionary[value]+=1
        else:
            key.append(value)
            dictionary[value]=1
    return (dictionary)
        
def makeWords(s):
    '''similar with makeWordLength except that it makes a dictionary from word itself'''
    wordlength=[]
    key=[]
    dictionary={}
    s=cleanString(s)
    split=s.split(" ")
    for word in split:
        wordlength.append(word)
    for value in wordlength:
        if value in key:
            dictionary[value]+=1
        else:
            key.append(value)
            dictionary[value]=1
    return (dictionary)

def makeStems(s):
    '''use porter.py to get each stem and create a dictionary for it'''
    wordlength=[]
    key=[]
    dictionary={}
    s=cleanString(s)
    split=s.split(" ")
    for word in split:
        stem=create_stem(word)
        wordlength.append(stem)
    for value in wordlength:
        if value in key:
            dictionary[value]+=1
        else:
            key.append(value)
            dictionary[value]=1
    return (dictionary)

def makePunctuation(s):
    '''Create a similar dictionary with makeWords function, just with punctuation'''
    wordlength=[]
    key=[]
    dictionary={}
    split=s.split(" ")
    for word in s:
        if word=="!":
            if word in key:
                dictionary[word]+=1
            else:
                key.append(word)
                dictionary[word]=1
        elif word=="?":
            if word in key:
                dictionary[word]+=1
            else:
                key.append(word)
                dictionary[word]=1
        elif word==".":
            if word in key:
                dictionary[word]+=1
            else:
                key.append(word)
                dictionary[word]=1
        elif word==",":
            if word in key:
                dictionary[word]+=1
            else:
                key.append(word)
                dictionary[word]=1
        elif word=="'":
            if word in key:
                dictionary[word]+=1
            else:
                key.append(word)
                dictionary[word]=1
    return (dictionary)

def normalizeDictionary(d):
    '''normalize the dictionary d by having sum of 1'''
    total=0
    for value in d.values():
        total+=value
    for key in d.keys():
        d[key]=d[key]/total
    return d

def smallestValue(nd1,nd2):
    '''return smallest among all values'''
    min1=1
    min2=1
    for value in nd1.values():
        if value<min1:
            min1=value
    for value in nd2.values():
        if value<min2:
            min2=value
    if min1>=min2:
        return min2
    else:
        return min1

def compareDictionaries(d,nd1,nd2):
    '''compare dictionaries nd1 and nd2 based on d and return in logistic value'''
    total1=0.0
    total2=0.0
    epsilon=0.5*smallestValue(nd1,nd2)
    nd1=normalizeDictionary(nd1)
    nd2=normalizeDictionary(nd2)
    for key in d.keys():
        if nd1.get(key)!=None:
            total1+=d[key]*math.log(nd1[key])
        else:
            total1+=d[key]*math.log(epsilon)
    for key in d.keys():
        if nd2.get(key)!=None:
            total2+=d[key]*math.log(nd2[key])
        else:
            total2+=d[key]*math.log(epsilon)
    return [total1,total2]
    
def createAllDictionaries(s): 
    """ should create out all five of self's 
            dictionaries in full - for testing and 
            checking how they are working...
    """
    sentencelengths = makeSentenceLengths(s)
    new_s = cleanString(s)
    words = makeWords(new_s)
    stems = makeStems(new_s)
    punct = makePunctuation(s)
    wordlengths = makeWordLengths(new_s)
    return [words, wordlengths, stems, sentencelengths, punct]

def compareTextWithTwoModels(newmodel,model1,model2):
    '''compare model1 and model2 in newmodel in 5 distinctive features and return which one is a better match'''
    win1=0
    win2=0
    wordview=compareDictionaries(newmodel[0],model1[0],model2[0])
    wordlengthview=compareDictionaries(newmodel[1],model1[1],model2[1])
    stemview=compareDictionaries(newmodel[2],model1[2],model2[2])
    sentencelengthview=compareDictionaries(newmodel[3],model1[3],model2[3])
    punctview=compareDictionaries(newmodel[4],model1[4],model2[4])
    print ("Overall Comparison:\n")
    print ("\nvsTM1 Data\n")
    print ("\nWords: ",wordview[0],"\n")
    print ("\nWord Length: ",wordlengthview[0],"\n")
    print ("\nStems: ",stemview[0],"\n")
    print ("\nSentence Length: ",sentencelengthview[0],"\n")
    print ("\nPunctuation: ",punctview[0],"\n\n")

    print ("Overall Comparison:\n")
    print ("\nvsTM2 Data\n")
    print ("\nWords: ",wordview[1],"\n")
    print ("\nWord Length: ",wordlengthview[1],"\n")
    print ("\nStems: ",stemview[1],"\n")
    print ("\nSentence Length: ",sentencelengthview[1],"\n")
    print ("\nPunctuation: ",punctview[1],"\n\n")

    if wordview[0]>wordview[1]:
        win1+=1
    else:
        win2+=1
    
    if wordlengthview[0]>wordlengthview[1]:
        win1+=1
    else:
        win2+=1
    
    if stemview[0]>stemview[1]:
        win1+=1
    else:
        win2+=1

    if sentencelengthview[0]>sentencelengthview[1]:
        win1+=1
    else:
        win2+=1

    if punctview[0]>punctview[1]:
        win1+=1
    else:
        win2+=1
    
    print ("Model 1 wins on ",win1," features.")
    print ("Model 2 wins on ",win2," features.")
    if win1>win2:
        print ("*****   Model 1 is the better match!    *****")
    else:
        print("*****     Model 2 is the better match!     *****")
    



# and, test things out here...
'''
print("TextModel1:")
printAllDictionaries( TextModel1 )
'''
test_text = '''This is a small sentence. This isn't a small sentence, because this sentence contains more than 10 words and a number! This isn't a question, is it?'''


'''
print(" +++++++++++ Model1 +++++++++++ ")
text1 = readTextFromFile( "train1.txt" )
TM1 = createAllDictionaries(text1)  # provided in hw description
printAllDictionaries(TM1)

print(" +++++++++++ Model2 +++++++++++ ")
text2 = readTextFromFile( "train2.txt" )
TM2 = createAllDictionaries(text2)  # provided in hw description
printAllDictionaries(TM2)


print(" +++++++++++ Unknown text +++++++++++ ")
text_unk = readTextFromFile( "unknown.txt" )
TM_Unk = createAllDictionaries(text_unk)  # provided in hw description
printAllDictionaries(TM_Unk)
'''