class AnagramChecker:
    def __init__(self):
        with open("week2/day5/ExerciceXP/wordsv2.txt", "r") as file_obj:
            data = file_obj.read()
        self.text = data.lower().split()

    def is_valid_word(self, word: str):
        return word.lower() in self.text

    def is_anagram(self, word1: str, word2: str):
        sorted_word1 = list(sorted(list(word1)))
        sorted_word2 = list(sorted(list(word2)))
        return sorted_word1 == sorted_word2 and word1 != word2

    def get_anagrams(self, word: str):
        anagrams_list = []

        for w in self.text:

            if self.is_anagram(word, w):
                anagrams_list.append(w)

        return anagrams_list


# ob = AnagramChecker()
# print(ob.is_anagram("ghgdghh", "ghgdhsghh"))
# # print(ob.is_valid_word("COMPACTii"))
# print(ob.get_anagrams("CALPA"))
