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


p = db.values("curso").set("horas_catedra","something")
print(p)


# print(q)
# print(q.__class__.container)
# print(Container.tools("persona").field_names())
# pprint(vars(Container.query("persona")))
# pprint(vars(Container.field("persona","nombres")))
# json_formatted_str = json.dumps(Container.entities(), indent=2)

# print(json_formatted_str)

# try:
#     Container.db_connect()
# finally:
#     Container.db_close()
