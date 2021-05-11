# Overview
Required Module:
- nltk
- re
- contractions

Required files (Uncomment the line with the download within preprocess.py to have it installed):
- nltk wordnet
- nltk stopwords

Description of files:
- main.py , program to run preprocessing on multiple file (See how to run)
- minitest.py (See Extra)
- preprocess.py, program to preprocess the content of the file by removing html tag, contraction, non-alphabet, stopword and lemmatize afterwards 
- negative/positive_library.txt output file for negative/positive dataset respectively

How to run:
- Put the dataset in a folder "train" with two files "pos" ("train/pos") for positive dataset and "neg" ("train/neg") for negative dataset
- Run main.py
- The result is written within txt file respectively.

Extra:
- If you want to train using a smaller dataset, put the small dataset in folder "minitrain" with two files "pos" ("minitrain/pos") for positive dataset and "neg" ("minitrain/neg") for negative dataset
