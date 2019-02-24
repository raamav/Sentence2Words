"""
Created on Sat Feb  13 12:53:18 2019

@author: ramavishwanathan
"""



""" Approach:
    step 1: parse words from a given sentence and store them in a list
    step 2: frequency count of the words and store them in a different list
    step 3: store both these things in a dictionary
"""



def parseSentence(sen):
    """
    sen: a sentence
    returns: a list that comprises all the words in the sentence
    Nb: this can be done much easily using the str.split() operation, I just wanted to explore an alternate way
    """
    
    sen+=" "
    sen = sen.lower()
    L_words = []
    word=""
    for i in sen:
        if (i !=" "):
            word = word + i
        else:
            L_words.append(word)
            word = ""
    return (L_words)
        
def wordFreqCount(L_words):
    """
    L_words: a list of words that are a part of the input sentence
    returns: a dictionary, that has words and their frequencies
    """
    
    #L_words.remove(" ")
    L_words.sort()
    L_freq = []
    freq=1
    for i in range(len(L_words)-1):
        if L_words[i]== "." or L_words[i]== ",":
            L_words.remove[i]
    
    for i in range(len(L_words)-1):
        if L_words[i+1]== L_words[i]:
            freq+=1
        else:
            L_freq.append(freq)
            freq=1
    L_freq.append(freq)
    L_words= list(set(L_words))
    L_words.sort()
    freq_dict = dict(zip(L_words, L_freq))
    #print (L_freq)
    return (freq_dict)        
       


# The lyrics can alternately be imported from a file 
sen = "Love, love me do You know I love you I'll always be true So please, love me do Whoa, love me do Love, love me do"

L_words = parseSentence(sen)
freq_dict = wordFreqCount(L_words)
print (L_words)
print (freq_dict)
