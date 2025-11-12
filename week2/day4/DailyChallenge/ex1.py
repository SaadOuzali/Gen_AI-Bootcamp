from collections import Counter
import os

class Text:
    def __init__(self, text: str):
        self.text = text

    def word_frequency(self, word: str):
        list_of_word = self.text.split()
        occurrences = list_of_word.count(word)
        if occurrences > 0:
            return occurrences
        else:
            return None

    def most_common_word(self):
        most_common_word_dict = {}
        list_of_word = self.text.split()
        for word in list_of_word:
            most_common_word_dict[word] = list_of_word.count(word)
        sorted_dict = dict(
            sorted(
                most_common_word_dict.items(), key=lambda item: item[1], reverse=True
            )
        )
        # print(f"sorted_dict is : {sorted_dict}")

        return sorted_dict
    
    def unique_words(self):
          list_of_word = self.text.split()
          set_of_word=sorted(set(list_of_word))
          return set_of_word
    
    @classmethod
    def from_file(cls,file_path:str):
        with open(file=file_path,mode="r") as file_obj:
            data=file_obj.read()
        return Text(text=data)


file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "words.txt")
# print(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
ob = Text("ta fen a5oya saad rojola saad dir lmz1 a saad mz1 ta")
# print(ob.most_common_word())
ob2=Text.from_file(file_path=file_path)

print(type(ob.from_file(file_path=file_path)))

