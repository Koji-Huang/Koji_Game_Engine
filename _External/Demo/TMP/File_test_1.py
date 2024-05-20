
from DataType.ConfigFile import Txt
from DataType.ConfigFile import Json
from DataType.ConfigFile import Ini

A = Txt(".Basel")

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
