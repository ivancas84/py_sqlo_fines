import sys
sys.path.insert(0, "../")

from py_sqlo.src.container_test import ContainerTest

config = {
    "user":"root",
    "password":"",
    "host":"localhost",
    "database":"planfi10_20203",
    "path_model":"C:\\xampp\\htdocs\\fines2-estructura\\model\\"
}

print(ContainerTest.mapping("persona"))
print(ContainerTest.mapping("alumno"))


# print(Container.tools("persona").field_names())
# pprint(vars(Container.query("persona")))
# pprint(vars(Container.field("persona","nombres")))
# json_formatted_str = json.dumps(Container.entities(), indent=2)

# print(json_formatted_str)

# try:
#     Container.db_connect()
# finally:
#     Container.db_close()
