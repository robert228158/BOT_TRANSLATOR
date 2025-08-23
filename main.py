import time
import random
points=0
trans_dict={
    'cat':'кот',
    'dog':'собака',
    'Russia':'Россия'
}
def add(trans_dict):
    eng=input('Введите слово на английском ')
    rus=input('Введите слово на русском ')
    trans_dict[eng]=rus


def show(trans_dict):
    print('_'*33)
    for key in trans_dict.keys():
        print(f'|{key}\t\t|\t{trans_dict[key]}\t|')
    print('-'*33)

def mode_train(word,check_word,lang):
    global points
    time.sleep(2)
    print_bot('Ваше слово:')
    print(word)
    time.sleep(2)
    print_bot(f'Введите слово на {lang}!')
    word=input()
    if word==check_word:
        time.sleep(2)
        print_bot('Круто!Продолжаем тренировку?')
        points+=10
    else:
        time.sleep(2)
        print_bot('Вы ответили неверно!')
        points-=10
        time.sleep(2)
        print_bot(f'Вы набрали: {points} очков')
    print_bot('Хотите продолжить(да, нет)?')
    q=input().lower()
    if q=='да':
        time.sleep(2)
        print_bot('Продолжаем')
    else:
        return 'break'

def delete(trans_dict):
    show(trans_dict)
    key=input('Введите слово которое хотите удалить ')
    del trans_dict [key]


def print_bot(s):
    print('-'*40)
    print(f'|{s:38}|')
    print('-'*40)



def train(trans_dict):
    global points
    time.sleep(3)
    mode=input('''Выберите режим:
1.Eng-Rus
2.Rus-Eng
''')
    
    while True:
        eng_word=random.choice(list(trans_dict.keys()))
        rus_word=trans_dict[eng_word]
        if mode=='1':
            if mode_train(eng_word,rus_word,'Русском')=='break':
                break


        elif mode=='2':
            if mode_train(rus_word,eng_word,'Английском'):
                break
        else:
            print("ERROR")
            mode=input('''Выберите режим:
1.Eng-Rus
2.Rus-Eng
''')


            


print('Добро пожаловать Дорогой пользователь')
print('Вы используете программу "Переводчик"')
time.sleep(5)
while True:
    print("|"+'*'*28+'|')
    print('''|                            |
|1.Добавить слово в словарь  |
|2.Удалить слово             |
|3.Вывести словарь           |
|4.Начать треннировку        |
|                            |''')
    print("|"+'*'*28+'|')
    time.sleep(3)
    command=(input())
    if command=='1':
        time.sleep(2)
        add(trans_dict)
        time.sleep(2)
    elif command=='3':
        time.sleep(2)
        show(trans_dict)
        time.sleep(2)
    elif command=='2':
        time.sleep(2)
        delete(trans_dict)
        time.sleep(2)
    elif command=='4':
        train(trans_dict)
    else:
        print('ERROR')
