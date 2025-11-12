from ex1 import Text
import re


class TextModification(Text):
    
    def __init__(self, text):
        super().__init__(text)
        self.stop_word=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",]

    def remove_punctuation(self):
        cleaned = re.sub(r"[^\w\s]", "", self.text)
        return cleaned

    def remove_stop_words(self):
        list_text=self.text.split(" ")
        print(list_text)
        filtred_text=list(filter(lambda wo: wo not in self.stop_word,list_text ))
        print(filtred_text)
        return " ".join(filtred_text)

ob=TextModification("Hello, world! This is a test... Let's me clean it : by myself i we our")
# print(ob.most_common_word())



cleaned_text =ob.remove_punctuation()
# print(cleaned_text)
print(ob.remove_stop_words())

