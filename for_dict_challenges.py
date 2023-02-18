# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

from collections import Counter
students_counted = Counter([x['first_name'] for x in students])
for each in students_counted:
    print(f"{each}: {students_counted[each]}")
print("Конец задания 1\n")

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]


def popular_counter(students: list):
    students_counted = Counter([x['first_name'] for x in students])
    print(f"{students_counted.most_common()[0][0]} is the most repeated name "
          f"with a result {students_counted.most_common()[0][1]}")

popular_counter(students)
print("Конец задания 2\n")

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for each in range(len(school_students)):  #Не могу использовать Counter. Объект list не хэшируемый
    print(f"Class # {each+1}")
    popular_counter(school_students[each])
print("Конец задания 3\n")

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}


def class_count(school_list: list):
    mf_dict = {}
    for each in school_list:
        cur_class = each['class']
        for learner in each['students']:
            mf_dict.setdefault(cur_class, {'boys': 0, 'girls': 0})
            if learner['first_name'] in is_male:
                if is_male[learner['first_name']]:
                    mf_dict[cur_class]['boys'] += 1
                else:
                    mf_dict[cur_class]['girls'] += 1
    return mf_dict


mf_dict = class_count(school)
for each in mf_dict:
    print(f"Class {each}: "
          f"girls {mf_dict[each]['girls']}, "
          f"boys {mf_dict[each]['boys']}")
print("Конец задания 4\n")

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]}
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
max_sex = {'boys': ['', 0], 'girls': ['', 0] }  # Переделал словарь прошлого упражнения,
# который используется и в этом. Но словарь max_sex вынужден оставить без изменения,
# ведь ключевое - это количество мальчиков и девочек, и обходя весь исходный словарь,
# я определяю, где больше всего, и сохраняю.
mf_dict = class_count(school)  # Получаем словарь вида {'class': {'boys': #, 'girls': #}}
for each in mf_dict:
    if max_sex['boys'][1] < mf_dict[each]['boys']:
        max_sex['boys'] = [each, mf_dict[each]['boys']]
    if max_sex['girls'][1] < mf_dict[each]['girls']:
        max_sex['girls'] = [each, mf_dict[each]['girls']]
for each in max_sex:
    print(f"Most number of {each} is in class "
          f"{max_sex[each][0]} - {max_sex[each][1]}")
print("Конец задания 5\n")
