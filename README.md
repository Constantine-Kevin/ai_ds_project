# Overview
This repository consists of our group's final project for the "Introduction to AI & Data Science" course.

Required Module:
- nltk
- re
- contractions
- sklearn

Required files (The code will download the necessary files if it does not exist):
- nltk wordnet
- nltk stopwords

Description of files:
- main.py , program to run the naive bayes to train and test the model
- Change the variable within main.py: "Lemmatize" to enable lemmatizer and "RemoveStopWord" to True to enable removing stop words
- By default both variable are False
- preprocess.py program to preprocess a text, 
- Each preprocessing will remove HTML tag, expanding contraction, and remove non-alphabetic characters

How to run:
- Put the train dataset in a folder "train" with two files "pos" ("train/pos") for positive dataset and "neg" ("train/neg") for negative dataset
- Put the test dataset in a folder "test" with two files "pos" ("test/pos") for positive dataset and "neg" ("test/neg") for negative dataset
- Run main.py
- Optional: Change the preprocessing options within main.py to suit which type of feature within preprocessing to use

Lessons Learned:
- Based on the [paper](Paper.pdf), we have found that Naïve Bayes can predict both positive and negative labels of the movie reviews with good accuracy.
- Removal of stopwords increases the accuracy of the model; however, lemmatization decreases the accuracy of the model.
- "I felt that during our time previously we did not refactor the code well and did not use a meaningful commit message. In future projects, I'll keep this in mind  apply code standards and best practices  " [Kevin Constantine](https://github.com/Constantine-Kevin)

Thanks to Andrew et al., from Stanford University for providing the dataset.<br>
The link to the dataset can be found [here](https://ai.stanford.edu/~amaas/data/sentiment/).