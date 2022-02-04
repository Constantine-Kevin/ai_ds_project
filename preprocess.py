import nltk
import re
import contractions

lemmatizer, stop_word = None, None

# Load Resources depending on which feature is enabled
def load_resources(lemmatize: bool = False, removeStopWord: bool = False):
    if lemmatize:
        try:
            nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download('wordnet')
        from nltk.stem import WordNetLemmatizer
        global lemmatizer
        lemmatizer = WordNetLemmatizer()
        print("Lemmatizer loaded")
    if removeStopWord:
        # Enable Stop Words
        from nltk.corpus import stopwords
        # List Of Stopwords
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords')
            global stop_word
        stop_word = stopwords.words('english')
        stop_word.remove('not')
        print("Stopwords loaded")


# Return a preprocessed string
def preprocess_string(str_arg: str, lemmatize: bool = False, removeStopWord: bool = False):
    # Clean the string from any HTML Tag
    cleanr = re.compile('<.*?>')
    cleaned_str = re.sub(cleanr, ' ', str_arg)
    # Expand Contraction
    cleaned_str = contractions.fix(cleaned_str)
    # Clean the string from any other non alphabet and multiple spaces
    cleaned_str = re.sub('[^a-z\s]+', ' ', cleaned_str, flags=re.IGNORECASE)
    cleaned_str = re.sub('(\s+)', ' ', cleaned_str)
    # Put the string to lowercase
    cleaned_str = cleaned_str.lower()
    cleaned_str_list = cleaned_str.split()
    # Lemmatize
    if lemmatize:
        cleaned_str_list = [lemmatizer.lemmatize(word) for word in cleaned_str_list]
    # Remove Stop Words
    if removeStopWord:
        cleaned_str_list = [word for word in cleaned_str_list if word not in stop_word]
    return " ".join(cleaned_str_list)


def main():
    a = "i just saw this movie on TV..<br /><br />i've lost my dad when i was young and this movie surely " \
        "did touch me..<br /><br />i can feel the lost that the little girl Desi felt..<br /><br />the feeling of" \
        " wanting to see her father again..<br /><br />wanting to talk to him..<br /><br />or at least given the " \
        "chance to say goodbye..<br /><br />and i'm so touched with the letter that was wrote back to her..<br />" \
        "<br />saying that her father read her letter, and sent it back to someone to reply her and buy her a present" \
        " because there isn't a shop in heaven..<br /><br />it just lets me feel that miracles do exist.."\
    b = "balbla blasd <br> ajsd! lasdda <h1>jasd"
    c = "The goose just cannot doesn't, like being looked upon by person not wearing any glasses."
    print(preprocess_string(c, True, True))


if __name__ == "__main__":
    main()
