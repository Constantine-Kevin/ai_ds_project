#Import modules Used
from sklearn.datasets import load_files

import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Import which type of preprocessing do you want to use:
# Each preprocessing will remove HTML tag, expanding contraction, and remove
# non-alphabetic characters
# preprocess    = No additional feature
# preprocess2   = Lemmatize only
# preprocess3   = Remove stopwords only
# preprocess4   = Use both lemmatizer and removing stopwords
from preprocess3 import preprocess_string

#Load folder minitrain as bunch, each data will have a
a=load_files("train")

#Utility to print filename
#print(a.filenames)

print("Load done commencing preprocessing")
for i in range(len(a.data)):
    #Convert data from byte into string and preprocess
    a.data[i]=preprocess_string(a.data[i].decode("utf-8"))


print("Preprocess done, commencing frequency count")
#Count frequency
vect= CountVectorizer()
a_count= vect.fit_transform(a.data)
#print(vect.get_feature_names())
#print(a_count.shape)
#print(a_count.toarray())
print("Count done, commencing naive bayes")

#Initiate Multinomial Naive Bayes and train using the train dataset
clf = MultinomialNB().fit(a_count, a.target)
print("Training done commencing test")
#Testing for positive dataset
docs_new=[]
testdir=os.listdir("test/pos")
#Load all positive test dataset text and preprocess
for i in testdir:
        with open("test/pos/"+i, 'r',encoding='utf8') as file:
            #Debug on which file it is in
            #print("test/pos/"+i)
            data = file.read().replace('\n', ' ')
            data=preprocess_string(data)
            docs_new.append(data)
print("Done importing positive dataset, commencing test")
x=vect.transform(docs_new)
predicted = clf.predict(x)
#Count the result
true_pos=0
false_neg=0
for doc, category in zip(docs_new, predicted):
    if a.target_names[category]=="pos":
        true_pos+=1
    else:
        false_neg+=1
#Testing for negative dataset
docs_new2=[]
testdir=os.listdir("test/neg")
#Load all negative test dataset text and preprocess
for i in testdir:
        with open("test/neg/"+i, 'r',encoding='utf8') as file:
            #Debug on which file it is in
            #print("test/neg/"+i)
            data = file.read().replace('\n', ' ')
            data=preprocess_string(data)
            docs_new2.append(data)
print("Done importing negative dataset, commencing test")
x2=vect.transform(docs_new2)
predicted2 = clf.predict(x2)
true_neg=0
false_pos=0
#Count the result
for doc, category in zip(docs_new2, predicted2):
    if a.target_names[category]=="neg":
        true_neg+=1
    else:
        false_pos+=1
print(f"Amount of True Positive: {true_pos}")
print(f"Amount of False Negative:{false_neg}")
print(f"Amount of True Negative:{true_neg}")
print(f"Amount of False Negative:{false_pos}")