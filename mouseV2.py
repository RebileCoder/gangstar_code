import pyautogui as pg
import random
import pyperclip

name = 'GENERATOR'

pg.alert('Добро пожаловать в генератор надёжных паролей', name, button='Сгенерировать пароль')

l = ['A', 'S', 'q', 'R', 't', 'Y', 'o', 'W', 'e', 'T', 'i', 'p', 'a', 's', 'D']
g = ['{', '[', '(', '~', '%', '$', '^', '&', '*', '-', '=', '`']
op = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

password = ''
s = 0
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
        break
    else:
        break
