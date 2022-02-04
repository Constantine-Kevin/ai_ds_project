# Import modules Used
from preprocess import load_resources, preprocess_string
from sklearn.datasets import load_files
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
# Import which type of preprocessing do you want to use:
# Each preprocessing will remove HTML tag, expanding contraction, and remove
# non-alphabetic characters
Lemmatize = False
RemoveStopWord = False


def main():
    # Load list of stopwords and lemmatizer
    load_resources(Lemmatize, RemoveStopWord)
    print("Resources Loaded")
    # Load folder minitrain as bunch, each data will have a
    a = load_files("train")

    # Utility to print filename
    # print(a.filenames)

    print("Load done commencing preprocessing")
    print(f"Preprocessing data with settings:\n")
    print(f"Lemmatizer: {Lemmatize}")
    print(f"Stop words removal: {RemoveStopWord}")
    print()
    for i in range(len(a.data)):
        # Convert data from byte into string and preprocess
        a.data[i] = preprocess_string(a.data[i].decode("utf-8"), Lemmatize, RemoveStopWord)

    print("Preprocess done, commencing frequency count")
    # Count frequency
    vect = CountVectorizer()
    a_count = vect.fit_transform(a.data)
    print("Count done, commencing naive bayes")

    # Initiate Multinomial Naive Bayes and train using the train dataset
    clf = MultinomialNB().fit(a_count, a.target)
    print("Training done commencing test")
    # Testing for positive dataset
    docs_new = []
    testdir = os.listdir("test/pos")
    # Load all positive test dataset text and preprocess
    for i in testdir:
        with open("test/pos/"+i, 'r', encoding='utf8') as file:
            # Debug on which file it is in
            # print("test/pos/"+i)
            data = file.read().replace('\n', ' ')
            data = preprocess_string(data, Lemmatize, RemoveStopWord)
            docs_new.append(data)
    print("Done importing positive dataset, commencing test")

    x = vect.transform(docs_new)
    predicted = clf.predict(x)
    # Count the result
    true_pos = 0
    false_neg = 0
    for doc, category in zip(docs_new, predicted):
        if a.target_names[category] == "pos":
            true_pos += 1
        else:
            false_neg += 1
    # Testing for negative dataset
    docs_new2 = []
    testdir = os.listdir("test/neg")
    # Load all negative test dataset text and preprocess
    for i in testdir:
        with open("test/neg/"+i, 'r', encoding='utf8') as file:
            # Debug on which file it is in
            # print("test/neg/"+i)
            data = file.read().replace('\n', ' ')
            data = preprocess_string(data, Lemmatize, RemoveStopWord)
            docs_new2.append(data)
    print("Done importing negative dataset, commencing test")
    # print(os.listdir("test/pos")[0])
    # print(docs_new[0])
    # print(os.listdir("test/neg")[0])
    # print(docs_new2[0])
    x2 = vect.transform(docs_new2)
    predicted2 = clf.predict(x2)
    true_neg = 0
    false_pos = 0
    # Count the result
    for doc, category in zip(docs_new2, predicted2):
        if a.target_names[category] == "neg":
            true_neg += 1
        else:
            false_pos += 1
    print(f"Amount of True Positive: {true_pos}")
    print(f"Amount of False Negative:{false_neg}")
    print(f"Amount of True Negative:{true_neg}")
    print(f"Amount of False Negative:{false_pos}")


if __name__ == "__main__":
    main()
