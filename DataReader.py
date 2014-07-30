__author__ = 'Alex Florez'

import xlrd
from Employee import Employee


class DataReader():
    def read_xls(self, filename, sheet=0):
        """ read data from a xls file """
        wb = xlrd.open_workbook(filename)
        ws = wb.sheet_by_index(sheet)
        return self.prepare_data(ws)

    def prepare_data(self, ws):
        data = []
        #num_rows = ws.nrows - 1
        num_cells = ws.ncols - 1
        curr_row = -1
        curr_cell = -1
        while curr_cell < num_cells:
            curr_cell += 1
            cell_type = ws.cell_type(curr_row, curr_cell)
            cell_value = ws.cell_value(curr_row, curr_cell)
            # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
            if cell_type == 1:
                data.append(cell_value)

        return self.format_data(data)

    def format_data(self, data):
        i = 0
        ni = 0
        data_employees = []

        while i is not None:
            i = self.find_code(self, data, i)  # code = data[i]
            if i is None:
                break
            ni = self.find_code(self, data, i + 1)
            if ni is None:  # llego al final
                ni = len(data)
                #break

            code = data[i]
            name = data[i + 1]
            emp = Employee(code, name)
            # marcas de cada día
            marks = data[i + 2:ni - 1]

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
    def find_code(self, data, i):
        """ Return the code's position """
        while i < len(data):
            if data[i].isdigit():
                return i  # No es necesario convertirlo, sólo es para identificar donde inicia el código
            i += 1
