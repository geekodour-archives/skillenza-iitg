import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

data = None

with open('dataBO.json','r',encoding='utf8') as json_data:
    data = json.load(json_data)
    print (data)

''' ---------------------------------------------------------------------------
    Cleaning the data
    ---------------------------------------------------------------------------
'''
from sklearn.ensemble import RandomForestClassifier
import json
import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import sys
import random
import string
import tflearn
import tensorflow as tf
import unicodedata

tbl = dict.fromkeys(i for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith('P'))

def remove_punctuation(text):
    return text.translate(tbl)

stemmer = LancasterStemmer()


categories = list(data.keys())
words = []
docs = []

for each_category in data.keys():
    for each_sentence in data[each_category]:
        each_sentence = remove_punctuation(each_sentence)
        w = nltk.word_tokenize(each_sentence)
        words.extend(w)
        docs.append((w, each_category))

words = [stemmer.stem(w.lower()) for w in words]
words = sorted(list(set(words)))

print (words)
print (docs)

training = []
output = []

output_empty = [0] * len(categories)

for doc in docs:
    bow = []
    token_words = doc[0]
    token_words = [stemmer.stem(word.lower()) for word in token_words]
    for w in words:
        bow.append(1) if w in token_words else bow.append(0)
    output_row = list(output_empty)
    output_row[categories.index(doc[1])] = 1
    training.append([bow, output_row])

random.shuffle(training)
training = np.array(training)

train_x = list(training[:,0])
train_y = list(training[:,1])

tf.reset_default_graph()


''' ---------------------------------------------------------------------------
            Building the Deep Neural Network
    ---------------------------------------------------------------------------
'''

net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')

''' ---------------------------------------------------------------------------
    Training the DNN
    ---------------------------------------------------------------------------
'''

model.fit(train_x, train_y, n_epoch=1000, batch_size=8, show_metric=True)
model.save('model.tflearn')

''' ---------------------------------------------------------------------------
    Testing the DNN
    ---------------------------------------------------------------------------
'''
  # let's test the mdodel for a few sentences:
  # the first two sentences are used for training, and the last two sentences are not present in the training data.
sent_1 = "I will be going for a party"                # 0
sent_2 = "Government of India is offering free Food"  # 1
sent_3 = "I am not into Politics"                     # 1
sent_4 = "I love India"                               # 1
sent_5 = "Bad Quality Products"                       # 0
sent_6 = "Lets watch the new movie"                   # 0
sent_7 = "Hindi in the National Language"             # 1
sent_8 = "nope! not going to eat fruits"              # 0
sent_9 = "Prime Minister of India"                    # 1
sent_10 = "defective products by Amazon"              # 0

  # a method that takes in a sentence and list of all words
  # and returns the data in a form the can be fed to tensorflow
def get_tf_record(sentence):
    global words
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    # bag of words
    bow = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bow[i] = 1

    return(np.array(bow))
dec = [" Not in Politics"," In politics"]
# we can start to predict the results for each of the 10 sentences
print(dec[int(categories[np.argmax(model.predict([get_tf_record(sent_1)]))])])  # Correct Output should be : 0
print(dec[int(categories[np.argmax(model.predict([get_tf_record(sent_2)]))])])  # Correct Output should be : 1
print(dec[int(categories[np.argmax(model.predict([get_tf_record(sent_3)]))])])  # Correct Output should be : 1
print(dec[int(categories[np.argmax(model.predict([get_tf_record(sent_4)]))])])  # Correct Output should be : 1
print(dec[int(categories[np.argmax(model.predict([get_tf_record(sent_5)]))])])  # Correct Output should be : 0
print(dec[int(categories[np.argmax(model.predict([get_tf_record(sent_6)]))])])  # Correct Output should be : 0
print(dec[int(categories[np.argmax(model.predict([get_tf_record(sent_7)]))])])  # Correct Output should be : 1
print(dec[int(categories[np.argmax(model.predict([get_tf_record(sent_8)]))])])  # Correct Output should be : 0
print(dec[int(categories[np.argmax(model.predict([get_tf_record(sent_9)]))])])  # Correct Output should be : 1
print(dec[int(categories[np.argmax(model.predict([get_tf_record(sent_10)]))])]) # Correct Output should be : 0

x=0
if(categories[np.argmax(model.predict([get_tf_record(sent_1)]))] == '0'):
    x+=1
if(categories[np.argmax(model.predict([get_tf_record(sent_2)]))] == '1'):
    x+=1
if(categories[np.argmax(model.predict([get_tf_record(sent_3)]))] == '1'):
    x+=1
if(categories[np.argmax(model.predict([get_tf_record(sent_4)]))] == '1'):
    x+=1
if(categories[np.argmax(model.predict([get_tf_record(sent_5)]))] == '0'):
    x+=1
if(categories[np.argmax(model.predict([get_tf_record(sent_6)]))] == '0'):
    x+=1
if(categories[np.argmax(model.predict([get_tf_record(sent_7)]))] == '1'):
    x+=1
if(categories[np.argmax(model.predict([get_tf_record(sent_8)]))] == '0'):
    x+=1
if(categories[np.argmax(model.predict([get_tf_record(sent_9)]))] == '1'):
    x+=1
if(categories[np.argmax(model.predict([get_tf_record(sent_10)]))] == '0'):
    x+=1
correctness = (x/10)*100
print(" Correct Result Percentage is : ",correctness)
