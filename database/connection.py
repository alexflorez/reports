__author__ = 'Alex Florez'

from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker

import locale

locale.setlocale(locale.LC_ALL, 'esp_per')

# pyodbc para conectarse a SQL Server
engine = create_engine('mssql+pyodbc://sa:CLight01@192.168.1.217\\CNLEHF/CNLEHFDB?charset=utf8')

metadata = MetaData(bind=engine)

# Reflection, leo la estructura de la base de datos
# referencia a 2 tablas
punches = Table("detPunches", metadata, autoload=True, schema="CNLEHFDB.dbo")
employee = Table("catEmployee", metadata, autoload=True, schema="CNLEHFDB.dbo")

Session = sessionmaker(bind=engine)
session = Session()

# para acceder a una columna utilizo la tabla referenciada con .c o .columns
allpunches = session.query(punches).filter(punches.columns.Badge == '2079')

i = 0
# punch es KeyedTuple, tiene named labels que hacen referencia a la columna de la tabla
for punch in allpunches:
    i += 1
    print(i, " ", punch.BelongDate, punch.PunchTime)

# haciendo un join entre empleado y sus marcas
marks = session.query(employee, punches)\
    .filter(employee.c.Badge == punches.c.Badge)\
    .filter(employee.c.Badge == '12345678').order_by(punches.c.PunchTime)

for mk in marks:
    print(mk.Name1, mk.LastName1, mk.BelongDate, mk.PunchTime)

count = session.query(punches).count()
print(count)
