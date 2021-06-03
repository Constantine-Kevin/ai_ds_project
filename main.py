import os
from preprocess import preprocess_string
from NaiveBayes import naivebayes
def main():
    #Initialization
    positive_text=os.listdir('train/pos')
    negative_text=os.listdir('train/neg')
    positive_library={}
    negative_library={}
    print("Start positive dictio")
    #Add to positive dictio
    for i in positive_text:
        with open("train/pos/"+i, 'r',encoding='utf8') as file:
            data = file.read().replace('\n', ' ')
            preprocess_string(data,positive_library)
    print("Start negative dictio")
    #Add to negative dictio
    for i in negative_text:
        with open("train/neg/"+i, 'r',encoding='utf8') as file:
            data = file.read().replace('\n', ' ')
            preprocess_string(data,negative_library)
    print("Finished creating dictio, starting naive bayes")
    #Sort Dictio by key
#    pos_dictio_item=positive_library.items()
#    positive_library=sorted(pos_dictio_item) # List of tuples, contains word freq per class
#    neg_dictio_item=negative_library.items()
#    negative_library=sorted(neg_dictio_item)
    positive_test=os.listdir('test/pos')
    negative_test=os.listdir('test/neg')
    confirm_positive=0
    error_positive=0
    confirm_negative=0
    error_negative=0
    print("Start the positive")
    #Add to positive dictio
    for i in positive_test:
        with open("test/pos/"+i, 'r',encoding='utf8') as file:
            print("test/pos/"+i)
            data = file.read().replace('\n', ' ')
            data=preprocess_string(data,{})
            if naivebayes(data,positive_library,negative_library)=="positive":
                confirm_positive+=1
            else:
                error_positive+=1
    print("Finished compute positive")                    
    #Add to negative dictio
    print("Start with negative")
    for i in negative_test:
        with open("test/neg/"+i, 'r',encoding='utf8') as file:
            print("test/neg/"+i)
            data = file.read().replace('\n', ' ')
            data=preprocess_string(data,{})
            if naivebayes(data,positive_library,negative_library)=="negative":
                confirm_negative+=1
            else:
                error_negative+=1
    print("Finished compute negative")
    print("Final Result")
    print(confirm_positive)
    print(error_positive)
    print(confirm_negative)
    print(error_negative)
    total=sum(confirm_positive,confirm_negative,error_positive,error_negative)
    print(f"Accuracy:{(confirm_positive+confirm_negative)/(total)}")
    

#    #Output 
#    with open("positive_library.txt","w",encoding='utf8') as file:
#        for tuples in positive_library:
#            file.write(f"{tuples[0]} {tuples[1]}\n")
#    with open("negative_library.txt","w",encoding='utf8') as file:
#        for tuples in negative_library:
#            file.write(f"{tuples[0]} {tuples[1]}\n")

if __name__ == "__main__":
	main()
