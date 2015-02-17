__author__ = 'Alex Florez'

import xlrd
from Employee import Employee


class DataReader():
    def __init__(self, filename):
        self.source = filename
        self.data = []

    def connect_db(self):
        pass

    def read_data(self):
        pass

    def process_data(self):
        pass

    def __repr__(self):
        return str(self.__dict__)
