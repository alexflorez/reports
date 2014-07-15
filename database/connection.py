__author__ = 'Alex Florez'

from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker

# pyodbc para conectarse a SQL Server
engine = create_engine('mssql+pyodbc://user:password@localhost/dbname?charset=utf8')

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
for punch in allpunches:
    i += 1
    print(i, " ", punch)
    if i == 10:
        break

count = session.query(punches).count()
print(count)