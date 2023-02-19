# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))



# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ["а", "е", "ё", "и", "о", "у", "э", "ю", "я"]
vowels_counter = 0
for each in word.lower():
    if each in vowels:
        vowels_counter += 1
print(vowels_counter)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for each in sentence.split():
    print(each[0:1])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.replace(' ', '')) / len(sentence.split()))

# Посчитать число буквв слове и вывести начиная с самой часто встречающейся и дльше по убыванию.
# Если несколько букв встречаются в слове одинаковое число раз,
# то вывести вперед ту что раньше в алфавите.
# Написать три решения - использую просто словарь, defaultdict и Counter.


import random, string
import time
WORD = ''.join([random.choice(string.ascii_letters) for x in range(1000000)])
#WORD = 'Литература'
# Dict
def simple_dict():
    word = {}
    for letter in WORD.lower():
        if letter in word:
            word[letter] += 1
        else:
            word[letter] = 1

    sorted_dict = {}
    for i in sorted(word.values(), reverse=True):
        if i not in sorted_dict.values():
            sorted_dict.update(dict.fromkeys(sorted([x for x in list(word.keys())
                                                     if word[x] == i]),
                                             i))
    return sorted_dict

start = time.process_time()
my_dict = simple_dict()
end = time.process_time()
print(f"Sort made with using simple dictionary\n "
      f"{my_dict}\n"
      f"In {end-start} seconds")

# defaultdict
from collections import defaultdict

def default_dict():
    word = defaultdict(int)
    for letter in WORD.lower():
        word[letter] += 1

    sorted_dict = {}
    for i in sorted(word.values(), reverse=True):
        if i not in sorted_dict.values():
            sorted_dict.update(dict.fromkeys(sorted([x for x in list(word.keys())
                                                     if word[x] == i]),
                                             i))
    return sorted_dict

start = time.process_time()
my_dict = default_dict()
end = time.process_time()
print(f"Sort made with using defaultdict dictionary\n "
      f"{my_dict}\n"
      f"In {end-start} seconds")

# Counter
from collections import Counter

def counter_dict():
    word = Counter(WORD)

    sorted_dict = {}
    for i in sorted(word.values(), reverse=True):
        if i not in sorted_dict.values():
            sorted_dict.update(dict.fromkeys(sorted([x for x in list(word.keys())
                                                     if word[x] == i]),
                                             i))
    return sorted_dict

start = time.process_time()
my_dict = counter_dict()
end = time.process_time()
print(f"Sort made with using Counter dictionary\n "
      f"{my_dict}\n"
      f"In {end-start} seconds")
# simple_dict() - 0.26, default_dict() - 0.25, counter_dict() - 0.10