__author__ = 'Alex Florez'

import xlrd
from Employee import Employee


class DataReader():
    def __init__(self, filename):
        self.source = filename
        self.data = []

    def open_xls(self, sheet=0):
        """ open xls file to read data"""
        wb = xlrd.open_workbook(self.source)
        ws = wb.sheet_by_index(sheet)
        return ws

    def read_worksheet(self, ws):
        num_rows = ws.nrows - 1
        num_cells = ws.ncols - 1
        curr_row = -1
        while curr_row < num_rows:
            curr_row += 1
            #row = worksheet.row(curr_row)
            #print('Row: ', row)
            curr_cell = -1
            while curr_cell < num_cells:
                curr_cell += 1
                # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
                cell_type = ws.cell_type(curr_row, curr_cell)
                cell_value = ws.cell_value(curr_row, curr_cell)
                if cell_type == 1:  #Agregar celdas que contengan Texto
                    self.data.append(cell_value)

    def format_data(self):
        i = 0
        ni = 0
        data_employees = []

        while i is not None:
            i = self.find_code(self.data, i)  # code = data[i]
            if i is None:
                break
            ni = self.find_code(self.data, i + 1)
            if ni is None:  # llego al final
                ni = len(self.data)
                #break

            code = self.data[i]
            name = self.data[i + 1]
            emp = Employee(code, name)
            # marcas de cada día
            marks = self.data[i + 2:ni - 1]

            m = 0
            while m < len(marks):
                emp.add_marks(marks[m:m + 2])
                m += 2
            # print(code, name)
            # print(marks)
            #emp.check_marks()
            data_employees.append(emp)
            i = ni

        return data_employees

    @staticmethod
    def find_code(data, i):
        """ Return the code's position """
        while i < len(data):
            if data[i].isdigit():
                return i  # No es necesario convertirlo, sólo es para identificar donde inicia el código
            i += 1

    def read(self):
        ws = self.open_xls()
        self.read_worksheet(ws)
        return self.format_data()

    def __repr__(self):
        return str(self.__dict__)
