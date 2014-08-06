__author__ = 'Alex Florez'

from collections import OrderedDict
import re


class Employee():
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.marks = dict()

    @staticmethod
    def get_hours(rawmark):
        # rawmark = '06:54 IN, 13:30 OL, 14:38 IL, 17:54 OT'
        hours = re.findall(r'\d{2}:\d{2}', rawmark)
        return hours

    @staticmethod
    def get_date(rawmark):
        # rawmark = 'Mié 30/07/2014'
        date = re.search(r'\d{2}/\d{2}/\d{4}', rawmark)
        # date is a Match object
        if date:
            return date.group()

    def add_marks(self, rawmarks):
        # rawmarks ['Mié 30/07/2014', '06:54 IN, 13:30 OL, 14:38 IL, 17:54 OT']
        date = self.get_date(rawmarks[0])
        if date:
            hours = self.get_hours(rawmarks[1])
            for h in hours:
                if date not in self.marks:
                    self.marks[date] = [h]
                else:
                    self.marks[date].append(h)

            self.marks = OrderedDict(sorted(self.marks.items()))
