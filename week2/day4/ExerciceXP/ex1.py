import os,random

path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "words.txt")
print("ttttt"+path)


def get_words_from_file(path:str)->list:
    with open(path,"r") as file_red:
        data=file_red.read()
        new_data_format=data.split("\n")    
        return new_data_format



# print(len(get_words_from_file(path)))

def get_random_sentence(sentence_length:int,path:str):
    list_of_words=get_words_from_file(path=path)
    if len(list_of_words) > 0:
       random_words = random.choices(list_of_words, k=sentence_length)
       sentence = " ".join(random_words).lower()
       return sentence
    else:
       raise ValueError("The file has no valid words.")
    

print(get_random_sentence(8,path))

