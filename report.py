__author__ = 'Alex Florez'

from Styles import Styles
from Mark import Mark
from TypeReport import TypeReport
from datetime import datetime
from datetime import timedelta

import locale
locale.setlocale(locale.LC_ALL, 'esp_per')


class Report:
    def __init__(self, name, type):
        self.type = name
        self.type = type

    def header(self, ws, day):
        ws.col(0).width = 2000  # para el numero
        ws.col(1).width = 9200  # 3333 = 1" (one inch) para el nombre

        r = 0
        title = 'Registro Permanente de Control de Asistencia (Diario)'
        ws.write_merge(r, r, 0, 5, title, Styles.STYLE_TITLE)  # Merges row 0's columns 0 through 5.

        r += 2      # r = 2
        ws.write_merge(r, r, 0, 1, 'Administración', Styles.STYLE_BLACK)

        header = []
        if day.strftime("%w") == str(6):  # Día Sábado
            header = ['Nro', 'Nombre', 'Ingreso', 'Salida']
        else:
            ws.write_merge(r, r, 3, 4, 'Almuerzo', Styles.STYLE_BLACK)
            header = ['Nro', 'Nombre', 'Ingreso', 'Entrada', 'Salida', 'Salida']

        r += 1      # r = 3  # fila a escribir
        for i, label in enumerate(header):
            ws.write(r, i, label, Styles.STYLE_HEADER)

        return r + 1

    def content(self, ws, data, r):
        # data
        # 0     1       2 Ing   3 I.Alm 4 R.Alm 5 Sal
        # Cod   Name    hh:mm   hh:mm   hh:mm   hh:mm
        #r = 4   #fila inicial para escribir
        #data list of all employees
        #data[0] emp.name emp.code emp.marks

        nro = 1
        for emp in data:
            ws.write(r, 0, nro, Styles.STYLE_CENTER)
            ws.write(r, 1, emp.name, Styles.STYLE_NORMAL)
            print(emp.name)
            nro += 1
            for list_marks in emp.list_marks:
                c = 2
                late = self.arrive_late(list_marks.marks[0], "08:05")
                for mk in list_marks.marks:
                    if late:
                        ws.write(r, c, mk, Styles.STYLE_LATE)
                        late = False
                        #print(r, c, mk)
                    else:
                        ws.write(r, c, mk, Styles.STYLE_CENTER)
                        #print(r, c, mk)
                    c += 1
                r += 1
            r += 1

        return r

    def arrive_late(self, hour, hour_ref):
        timein = Mark.str2time(hour)
        late = Mark.str2time(hour_ref)
        if timein > late:
            return True
        return False

    def footer(self, ws, row):
        message = 'Considerar 10 minutos de tolerancia en retorno de almuerzo. ' \
                  'LA HORA DE SALIDA AL REFRIGERIO ES MAX. 01:30 p.m.'
        ws.write_merge(row + 1, row + 2, 0, 5, message)  # r1 r2 c1 c2

    def make_report(self, data):
        if self.type == TypeReport.XLS:
            import xlwt
            workbook = xlwt.Workbook(encoding='ascii')
            worksheet = workbook.add_sheet('Horas Administracion')
            row = self.header(worksheet, 'Semana')
            row = self.content(worksheet, data, row)
            self.footer(worksheet, row)
            workbook.save('Asistencia.xls')
            print("File written")
        else:
            print("Nothing to be done")
