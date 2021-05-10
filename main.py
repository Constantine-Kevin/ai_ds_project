import os
from preprocess import preprocess_string
def main():
    #Initialization
    positive_text=os.listdir('train/pos')
    negative_text=os.listdir('train/neg')
    positive_library={}
    negative_library={}
    #Add to positive dictio
    for i in positive_text:
        with open("train/pos/"+i, 'r',encoding='utf8') as file:
            data = file.read().replace('\n', ' ')
            preprocess_string(data,positive_library)
    #Add to negative dictio
    for i in negative_text:
        with open("train/neg/"+i, 'r',encoding='utf8') as file:
            data = file.read().replace('\n', ' ')
            preprocess_string(data,negative_library)
    #Sort Dictio by key
    pos_dictio_item=positive_library.items()
    positive_library=sorted(pos_dictio_item)
    neg_dictio_item=negative_library.items()
    negative_library=sorted(neg_dictio_item)
    #Output 
    #print(positive_library)
    with open("positive_library.txt","w",encoding='utf8') as file:
        for tuples in positive_library:
            file.write(f"{tuples[0]} {tuples[1]}\n")
    with open("negative_library.txt","w",encoding='utf8') as file:
        for tuples in negative_library:
            file.write(f"{tuples[0]} {tuples[1]}\n")
    #print()
    #print()
    #print(negative_library)
main()