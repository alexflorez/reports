__author__ = 'Alex Florez'

from collections import OrderedDict


class Employee():
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.marks = dict()

    @staticmethod
    def extract_hours(rawmark):
        hours = []
        marks = rawmark.split(',')

        for m in marks:
            marca = m[:-3].strip()
            hours.append(marca)
        return hours

    def add_marks(self, rawmarks):
        # rawmarks ['Mié 30/07/2014', '06:54 IN, 13:30 OL, 14:38 IL, 17:54 OT']
        list_mark = []
        dia, fecha = rawmarks[0].split(' ')
        hours = self.extract_hours(rawmarks[1])
        for hora in hours:
            marca = fecha + " " + hora
            list_mark.append(marca)

        for mk in list_mark:
            fecha, hora = mk.split(' ')
            if fecha not in self.marks:
                self.marks[fecha] = [hora]
            else:
                self.marks[fecha].append(hora)

        self.marks = OrderedDict(sorted(self.marks.items()))
