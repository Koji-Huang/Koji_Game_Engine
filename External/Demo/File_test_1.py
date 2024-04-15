
from DataType.ConfigFile.txt import Txt
from DataType.ConfigFile.json import Json
from DataType.ConfigFile.ini import Ini

A = Txt(".config")

A.write('Hello', "World")


B = Json('.json')
B.update(A)
B.save()

B.read()

C = Ini('.ini')
C['Hello']['World'] = "!"
C.save()

C.read()


pass
