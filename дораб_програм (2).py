# -*- coding: utf-8 -*-

from datetime import datetime
_data = str(datetime.date(datetime.now()))
_FIO = input('Здравствуйте! Введите свою фамилию и инициалы \t')
print(_data, end='\t' + ' Испытания проводит:\t ' +  _FIO)
n_Dani = open('St_saf.txt', 'a+')
n_Dani.write(f'\n{_data}\nИспытания проводил:\t{_FIO}\n')
#n_Dani.close()
import math
Lr = int(input('\n Введите длину рычага стеклоочистителя в мм - '))
Hr = int(input('Измерить и ввести расстояние между двумя крайними положениями щётки стеклоочистителя в мм -'))
Ug_St = math.degrees(math.asin( 0.5 * Hr/Lr) * 2)
ug_St = format(Ug_St,'.2f')
print(f'Угол очистки стекла =\t{ug_St} град.')
input('Для записи полученных данных в фаил St_saf.txt нажмите клавишу - Enter ')
n_Dani.write(f'\nдлина рычага стеклоочистителя в мм - {Lr}\t расстояние между двумя крайними положениями щётки -{Hr}\n')
n_Dani.write(f'Угол очистки стекла =\t{ug_St} град.')
n_Dani.close()