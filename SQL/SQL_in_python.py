import sqlalchemy

server = 'localhost,1433'
database = 'Northwind'
user = 'SA'
password = 'Passw0rd2018'
# '0DBC+Driver+17+for+SQL+Server' was the original driver
driver = 'SQL+Server'
# pip install pyodbc in the terminal
engine = sqlalchemy.create_engine(f"mssql+pyodbc://{user}:{password}@{server}/{database}?driver={driver}")

connection = engine.connect()

# This is creating an object which needs to be accessed
# result = engine.execute('SELECT * FROM Products;')
# print(result)
# Acquiring the results tables.

# Getting first row
# first_row = result.fetchone()
# print(first_row)
#
# Getting all rows
# all_rows = result.fetchall()
# print(all_rows)
#
# # Fetching many rows
# many_rows = result.fetchmany(10)
# print(many_rows)

# Fetching column names
# column_names = result.keys()
# print(column_names)
# for i in all_rows:
#     print(i)

# printing a certain column

# unit_price = engine.execute('SELECT UnitPrice FROM Products;')
# unit_price_column_values = unit_price.fetchall()
# for i in unit_price_column_values:
#     print(i)

