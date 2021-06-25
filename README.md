# Overview
Required Module:
- nltk
- re
- contractions
- sklearn

Required files (Uncomment the line with the download within preprocess.py to have it installed):
- nltk wordnet
- nltk stopwords

Description of files:
- main.py , program to run the naive bayes to train and test the model
- preprocess<**number**>.py program to preprocess tag, 
- Each preprocessing will remove HTML tag, expanding contraction, and remove non-alphabetic characters
- preprocess    = No additional feature
- preprocess2   = Lemmatize only
- preprocess3   = Remove stopwords only
- preprocess4   = Use both lemmatizer and removing stopwords

How to run:
- Put the train dataset in a folder "train" with two files "pos" ("train/pos") for positive dataset and "neg" ("train/neg") for negative dataset
- Put the test dataset in a folder "test" with two files "pos" ("test/pos") for positive dataset and "neg" ("test/neg") for negative dataset
- Run main.py
- Optional: Change the import preprocessing within main.py to suit which type of feature within preprocessing to use