
#class Person:
def opros():
    a =("Какой язык программирования знаете?")
    print(a)
    d= input('как дела? напиши здесь: ')
    print('я тебя поняла, у тебя дела ',d)
    pos = """ INSERT INTO mobile (ID, VOPROS, VARIANT)
                                           VALUES (%s,%s,%s)"""
    rec = (5, 'One Plus 6', 950)
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, "Запись успешно добавленаблицу mobile")
    con.commit()
    con.close()
def opros1():
    b=('Вопрос номер 1')
    S=('выберите варианты ответов \n a. летом не падает снег, а падает град каждый день \n b. Солнце светит в солнечную погоду \n s. неправильный ответ ')
    print(b)
    print(S)
    dd = input('напиши здесь букву правильного ответа : ')
    if dd =='b':
        K1 = True
        print('good ')
    else:
        K1 = False
        print('не :')
    print('ответ записан :')

def opros2():
    b=('Вопрос номер 2')
    S=('выберите варианты ответов \n a. какой то текст \n b. еще что нибудь \n s. правильный ответ True')
    print(b)
    print(S)
    dd = input('напиши здесь букву правильного ответа: ')
    if dd =='a':
        K2 = True
        print('good ')
    else:
        K2 = False
        print('не :')
    print('ответ записан :')

def opros3():
    b=('Вопрос номер 3')
    S=('выберите варианты ответов \n a. какой то текст \n b. еще что нибудь \n s. правильный ответ True')
    print(b)
    print(S)
    dd = input('напиши здесь букву правильного ответа : ')
    if dd =='s':
        K1 = True
        print('good ')
    else:
        K1 = False
        print('не :')
    print('ответ записан :')

def id():
    ID=input('Напишите свой id: ')
    #a= input()
    print('Ваш id ',ID)

if __name__ == '__main__':
   # opros()
    id()
    opros1()
    opros2()
    opros3()

