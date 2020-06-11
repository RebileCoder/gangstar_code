import pyautogui as pg
import random
import pyperclip

name = 'MOUSE'

pg.alert('Добро пожаловать в генератор надёжных паролей', name, button='Сгенерировать новый пароль')

password_name = pg.prompt('Пароль от:', name)

login = pg.prompt('Логин для пароля:')

g = open('пароли.txt', 'r')
k = g.read().split(':')
while True:
    for b in k:
        if b == password_name:
            password_name = pg.prompt('Измените название сервиса пароля. Введённый вами Пароль от... уже существует', name)
    break


o = pg.confirm('Хотите добавить заметку к паролю?', name, ('Да', 'Нет'))

if o == 'Да':
    keep = pg.prompt('Ваша заметка:', name)


l = ['A', 'S', 'q', 'R', 't', 'Y', 'o', 'W', 'e', 'T', 'i', 'p', 'a', 's', 'D']
g = ['{', '[', '(', '~', '%', '$', '^', '&', '*', '-', '=', '`']
op = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

password = ''
s = 3
pop = 0

while True:
    d = random.randint(3, 4)
    for x in range(d):
        a = random.choice(l)
        b = random.choice(g)
        c = random.choice(op)
        password += a
        password += b
        password += c

    while pop < s:
        pg.screenshot('tor' + str(pop) + '.png')
        pop += 1
    g = pg.confirm('Ваш пароль:\n' + str(password), name, ('Скопировать', 'Ещё раз', 'Отмена'))
    if g == 'Ещё раз':
        password = ''
    elif g == 'Скопировать':
        pyperclip.copy(password)
        f = open('пароли.txt', 'a')
        f.write('\n' + str(password_name) + ': ' + str(login) + ', ' + str(password))
        if o == 'Да':
            f.write('\nЗаметка: ' + str(keep))
        f.close()
        break
    else:
        break
