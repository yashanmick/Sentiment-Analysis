
#1 - Cleaning Text Steps
    #1 - create a text file and take test from it
    #2 - convert the letter into lowercase 
    #3 - remove punctuations like .,!? (Hi! This is mick.)

import string
from collections import Counter
import matplotlib.pyplot as plt

import GetOldTweets3 as got

def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('Donald Trump')\
                                           .setSince("2015-01-01")\
                                           .setUntil("2020-07-04")\
                                           .setMaxTweets(100)
    
    #list of objects gets stored in 'tweets' variable
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    #iterating through tweets list. Storing them temp in tweet variable
    #get text and store it as a list insde text_tweets
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets

text = ""
text_tweets = get_tweets()
length = len(text_tweets)

for i in range(0, length):
    text = text_tweets[i][0] + " " + text
    #print(text)


#read text
#text = open('read.txt', encoding='utf=8').read()
#print(text)

#convert to lovercase
    #lower() - can only works with strings, not working with lists
    #so convert the list to a string
lower_case = text.lower()
#print(string.punctuation)
#print(lower_case)

#removing punctuations
clean_text = lower_case.translate(str.maketrans('','',string.punctuation))
#clean_text = lower_case.translate(str.maketrans('l,o,i','x,y,z',string.punctuation))
    #str1 : Specifies the list of characters that need to be replaced.
    #str2 : Specifies the list of characters with which the characters need to be replaced.
    #str3 : Specifies the list of characters that needs to be deleted.
    #
    #Returns : Returns the translation table which specifies the conversions that can be used

#2 - tokenization
#how to break up the sentence to words

tokenized_words = clean_text.split()

#3 - stop words
#words that does not add any meaning to the sentence

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

#4 - getting word list which not in stop_words list
final_words = []

for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)


#5 - NPL Emotion Algorithm
    #1 - check if the word in the final word list is also present in emotion.txt
        # open the emotion file
        # loop through each line and clear it
        # extract the word and emotion using split

    #2 - if word is present -> add the emotion to emotion_list
    #3 - finally count each emotion in the emotion_list

emotion_list = []

with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n","").replace("'", "").strip()     #strip() removes the extra spaces inside the file
        word, emotion = clear_line.split(':')
        #print("Word :" + word + " " + "Emotin :" + emotion)

        if word in final_words:
            emotion_list.append(emotion)
           
print(emotion_list)
w = Counter(emotion_list)
print(w)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()