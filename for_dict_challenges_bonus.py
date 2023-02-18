"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""

import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list({random.randint(1, 10000) for _ in range(random.randint(5, 20))})
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice([None, random.choice([m["id"] for m in messages]) if messages else []]),
            "seen_by": random.sample(users_ids, random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


import pprint
from collections import Counter
def task1(messages):  # 1. Вывести айди пользователя, который написал больше всех сообщений.
    sent_by = [each['sent_by'] for each in messages]
    print(f"\nMost messages from user {Counter(sent_by).most_common()[0][0]}")

def task2(messages):  # 2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
    reply_for = [str(each['reply_for']) for each in messages  # генерирую список сообщений,
                 # на которые отвечали
                 if each['reply_for'] is not None]
    most_replied_user = [each['sent_by'] for each in messages
                         if str(each['id']) == Counter(reply_for)
                         .most_common()[0][0]]
    print(f"\nThe most replyable user is {most_replied_user[0]}")

def task3(messages):  # 3. Вывести айди пользователей, сообщения которых видело больше всего
    # уникальных пользователей.
    unique_users = {}
    for every_user in [each['sent_by'] for each in messages]:
        for seen_list in [each_seen['seen_by'] for each_seen in messages
                          if each_seen['sent_by'] == every_user]:
            if every_user in unique_users:
                unique_users[every_user].update(seen_list)
            else:
                unique_users[every_user] = set(seen_list)
    print('\nThree users with most unique views')
    for counter, each in enumerate(Counter(unique_users).most_common(), start=1):
        print(f"User {each[0]} has viewrs {each[1]}")
        if counter == 3: break


def task4(messages):  # 4. Определить, когда в чате больше всего сообщений: утром (до 12 часов),
# днём (12-18 часов) или вечером (после 18 часов).
    rush_hours = {'Morning': 0, 'Daytime': 0, 'Evening': 0}
    for each in messages:
        if each['sent_at'].hour < 12:
            rush_hours['Morning'] += 1
        elif each['sent_at'].hour < 18:
            rush_hours['Daytime'] += 1
        else:
            rush_hours['Evening'] += 1
    print(f"\nThe rush hours is {Counter(rush_hours).most_common()[0][0]}")


def recursive_search(first_id):
    pass

def task5(messages):  # 5. Вывести идентификаторы сообщений, который стали началом
    # для самых длинных тредов (цепочек ответов).
    def recursive_search(first_id, depth):
        if result_dict[first_id] is None:
            max_depth[first_id] = depth
            return
        else:
            recursive_search(result_dict[first_id], depth + 1)
    result_dict = {}
    max_depth = {}
    for each in messages:  # Составляю словарь только из ID сообщений, вида {id: reply_for}
        result_dict[each['id']] = each['reply_for']
    for each in result_dict:  # Обхожу словарь рекурсивно проваливаясь по каждому ключу словаря в
        # поисках базового условия, в котором значением по ключу будет None, то есть
        # вершина цепочки сообщений
        recursive_search(each, depth=1)  # Начальная глубина всегда 1
    print(f'\nThe longest thread starts with {Counter(max_depth).most_common()[0][0]} '
          f'and counts {Counter(max_depth).most_common()[0][1]} messages in it')


if __name__ == "__main__":
    messages = generate_chat_history()
    pprint.pprint(messages)
    # print(Counter(generate_chat_history()['sent_by']))
    task1(messages)
    task2(messages)
    task3(messages)
    task4(messages)
    task5(messages)