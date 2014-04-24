__author__ = 'Alex Florez'

from jinja2 import Environment, FileSystemLoader

import datetime

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('table.html')
title = ['Nro', 'Nombre', 'Ingreso', 'Entrada', 'Salida', 'Salida']
data = [[1, 'Name Surname', '08:07', '14:05', '15:09', '18:25'],
        [2, 'Name Surname', '07:59', '13:26', '14:31', '18:06'],
        [3, 'Name Surname', '08:00', '13:25', '14:32', '18:04'],
        [4, 'Name Surname', '08:02', '13:30', '14:30', '18:00'],
        [5, 'Name Surname', '08:06', '13:29', '14:27', '17:53'],
        [6, 'Name Surname', '08:03', '13:25', '14:28', '18:31'],
        [7, 'Name Surname', '08:00', '13:33', '14:29', '17:48'],
        [8, 'Name Surname', '08:02', '12:21', '12:51', '18:25'],
        [9, 'Name Surname', '07:59', '13:24', '14:13', '22:16'],
        [10, 'Name Surname', '08:08', '13:12', '14:01', '18:35'],
        [11, 'Name Surname', '08:04', '13:29', '14:27', '17:48'],
        [12, 'Name Surname', '04:51', '13:33'],
        [13, 'Name Surname', '09:34', '13:28', '14:08', '17:02'],
        [14, 'Name Surname', '08:09', '13:05', '14:20', '17:48']]

args = 3


def arrive_late(it):
    if type(it) != str or len(it) > 5:
        return False
    hh, mm = it.split(':')
    timein = datetime.timedelta(minutes=int(mm), hours=int(hh))
    late = datetime.timedelta(minutes=5, hours=8)
    if timein > late:
        return True
    return False


output = template.render(header=title, datamarks=data, islate=arrive_late)
f = open('reporte_email.html', 'w')
f.write(output)
