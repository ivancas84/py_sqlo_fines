import sys

sys.path.insert(0, "../")

from py_sqlo.src.db import Db


config = {
    "user":"root",
    "password":"",
    "host":"localhost",
    "database":"planfi10_20203",
    "path_model":"C:\\xampp\\htdocs\\fines2-estructura\\model\\",
    "driver":"mysql"
}

db = Db(config)
q = db.query("persona").cond((
    ("domicilio-calle","EQUAL",True),
    ("domicilio-numero","EQUAL",94)
)).sql()
# print(q)
# cursor = db.conn().cursor()

# sql = "SELECT tiene_constancia FROM alumno WHERE tiene_constancia = true LIMIT 1 "

# cursor.execute(sql)
# # remaining_rows = cursor.fetchall()
# # print(remaining_rows)


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


