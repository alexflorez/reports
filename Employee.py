__author__ = 'Alex Florez'


class Employee():
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.marks = []

    @staticmethod
    def extract_hours(rawmark):
        hours = []
        marks = rawmark.split(',')

        for m in marks:
            marca = m[:-3].strip()
            hours.append(marca)
        return hours

    # Cada empleado debería tener 4 marcas como max Entrada, Almuerzo, Regreso, Salida
    # Agregar una hora de almuerzo para los que no regitraron marcacion
    def add_mark(self, rawmarks):
        # rawmarks : ['Mar 01/04/2014', '08:07 IN, 13:52 OL, 15:00 IL']
        try:
            dia, fecha = rawmarks[0].split(' ')
            hours = self.extract_hours(rawmarks[1])
            for hora in hours:
                marca = fecha + " " + hora
                self.marks.append(marca)
        except:
            return
