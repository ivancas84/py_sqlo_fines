import pprint
import sys
sys.path.insert(0, "../")

from py_sqlo.src.container import Container


config = {
    "user":"root",
    "password":"",
    "host":"localhost",
    "database":"planfi10_20203",
    "path_model":"C:\\xampp\\htdocs\\fines2-estructura\\model\\"
}


Container.init(config)
m = Container.mapping("curso").label()
print(m)
# q = Container.query("persona").fields().sql()
# print(q)


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
