import pprint
from pydoc import resolve
import sys
sys.path.insert(0, "../")

from py_sqlo.src.db import Db
from py_sqlo.src.config import APPROX, EQUAL, NONEQUAL


config = {
    "user":"root",
    "password":"",
    "host":"localhost",
    "database":"planfi10_20203",
    "path_model":"C:\\xampp\\htdocs\\fines2-estructura\\model\\"
}

db = Db(config)
q = db.query("persona").cond(["nombres",APPROX,"Ivan"]).sql()
print(q)
# mycursor = db.conn().cursor()

# sql = "SELECT * FROM persona WHERE nombres LIKE %s"

# mycursor.execute(sql, ("%"+"Juan"+"%", ))

# print(mycursor.statement)


