import nltk
import re
import contractions
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 

#Lemmatizer
#nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
#List Of Stopwords
stop_word=stopwords.words('english')
stop_word.remove('not')

#Uncomment below ONCE if the file isn't installed in computer
nltk.download('stopwords')

def preprocess_string(str_arg,dictio):
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
    #Remove stopwords and lemmatize
    #without_sw = [lemmatizer.lemmatize(word) for word in cleaned_str_list if not word in stop_word]
    #without_sw = [word for word in cleaned_str_list if not word in stop_word]
    #without_sw.sort()
    #Put result in a dictio
    for i in cleaned_str_list:
        dictio[i]=dictio.get(i,0)+1
    #for i in without_sw:
    #    dictio[i]=dictio.get(i,0)+1
    #print(dictio)
    return cleaned_str_list
    #return without_sw

def main():
    a="i just saw this movie on TV..<br /><br />i've lost my dad when i was young and this movie surely did touch me..<br /><br />i can feel the lost that the little girl Desi felt..<br /><br />the feeling of wanting to see her father again..<br /><br />wanting to talk to him..<br /><br />or at least given the chance to say goodbye..<br /><br />and i'm so touched with the letter that was wrote back to her..<br /><br />saying that her father read her letter, and sent it back to someone to reply her and buy her a present because there isn't a shop in heaven..<br /><br />it just lets me feel that miracles do exist.."
    b="balbla blasd <br> ajsd! lasdda <h1>jasd"
    c="The goose just cannot doesn't, like being looked upon by person not wearing any glasses."
    print(preprocess_string(c,{}))

if __name__=="__main__":
    main()
