# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

from collections import Counter
# Вывести количество букв "а" в слове
word = 'Архангельск'
print(Counter(word.lower())['а'])



# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ["а", "е", "ё", "и", "о", "у", "э", "ю", "я"]
vowels_counter = 0
for each in Counter(word.lower()):
    if each in vowels:
        vowels_counter += Counter(word.lower())[each]
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