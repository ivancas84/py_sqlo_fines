import sys
import datetime
from dateutil.parser import parse


sys.path.insert(0, "../")

from py_sqlo.src.db import Db


config = {
    "user":"root",
    "password":"",
    "host":"localhost",
    "database":"planfi10_20203",
    "path_model":"C:\\xampp\\htdocs\\py_sqlo_fines\\model\\",
    "driver":"mysql"
}
d = parse("-")
print(type(d))
print(d)

# d = datetime.datetime.strptime("2012-04-23", '%Y-%m-%d')

db = Db(config)

# q = db.query("persona").cond((
#     ("persona-fecha_nacimiento","EQUAL","2021"),
# )).sql()
# print(q)
cursor = db.conn().cursor()

sql = "SELECT anio FROM calendario WHERE anio = %s"

cursor.execute(sql, ("2022",))
remaining_rows = cursor.fetchall()
print(remaining_rows)
print(type(remaining_rows[0][0]))

# class CursorByName():
#     def __init__(self, cursor):
#         self._cursor = cursor
    
#     def __iter__(self):
#         return self

#     def __next__(self):
#         row = self._cursor.__next__()

#         return { description[0]: row[col] for col, description in enumerate(self._cursor.description) }
    
# for row in CursorByName(cursor):
#     print(to_bool(row["tiene_constancia"]))


