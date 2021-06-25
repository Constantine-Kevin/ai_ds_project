import nltk
import re
import contractions
from nltk.stem import WordNetLemmatizer 


#Lemmatizer
#Uncomment below if the file isn't installed in computer
#nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

#Return a preprocessed string
def preprocess_string(str_arg):
    #Clean the string from any HTML Tag
    cleanr = re.compile('<.*?>')
    cleaned_str =re.sub(cleanr, ' ',str_arg)
    #Expand Contraction
    cleaned_str= contractions.fix(cleaned_str)
    #Clean the string from any other non alphabet and multiple spaces
    cleaned_str=re.sub('[^a-z\s]+',' ',cleaned_str,flags=re.IGNORECASE) 
    cleaned_str=re.sub('(\s+)',' ',cleaned_str)
    #Put the string to lowercase
    cleaned_str=cleaned_str.lower() 
    cleaned_str_list= cleaned_str.split()
    #Lemmatize
    cleaned_str_list=[lemmatizer.lemmatize(word) for word in cleaned_str_list]
    
    return " ".join(cleaned_str_list)


def main():
    a="i just saw this movie on TV..<br /><br />i've lost my dad when i was young and this movie surely did touch me..<br /><br />i can feel the lost that the little girl Desi felt..<br /><br />the feeling of wanting to see her father again..<br /><br />wanting to talk to him..<br /><br />or at least given the chance to say goodbye..<br /><br />and i'm so touched with the letter that was wrote back to her..<br /><br />saying that her father read her letter, and sent it back to someone to reply her and buy her a present because there isn't a shop in heaven..<br /><br />it just lets me feel that miracles do exist.."
    b="balbla blasd <br> ajsd! lasdda <h1>jasd"
    c="The goose just cannot doesn't, like being looked upon by person not wearing any glasses."
    print(preprocess_string(c))

if __name__=="__main__":
    main()
