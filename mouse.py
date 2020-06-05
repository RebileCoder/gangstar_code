import pyautogui as pg

scr = 4  # количество скриншотов

virus = 'MOUSE'  # название вируса

pg.alert('Приступаем к настройке вируса!', virus, button = 'Погнали!')
age = pg.prompt('Введите ваш возраст:', virus)
bop = pg.confirm('Вы уверены в своём ПК?', virus, ('ДА', 'Нет'))
if bop == 'ДА':
    name = pg.prompt('Введите ваше имя:', virus)
    l = pg.confirm(str(name) + ', я запускаю вирус?', virus, ('Давай!', 'Нет, мне страшно'))
    if l == 'Давай!':
        pg.hotkey('winleft')
        pop = 0
        while pop < scr:
            pg.screenshot('screeeeen' + str(pop) + '.png')
            pop += 1
