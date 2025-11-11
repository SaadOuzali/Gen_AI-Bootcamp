import string,random

all_letters = string.ascii_letters
print(all_letters)
random_letters = random.choices(all_letters, k=5)
print(random_letters)
