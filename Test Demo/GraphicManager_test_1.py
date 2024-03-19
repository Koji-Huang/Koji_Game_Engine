import GraphicComponentManager
from GraphicComponent.UI import *

Manager = GraphicComponentManager.GraphicComponentManager()

Label_1 = Label((100, 100), (100, 100))
Label_1.set_color((255, 0, 0))
Label_2 = Label((250, 100), (100, 100))
Label_2.set_color((0, 255, 0))
Label_3 = Label((400, 100), (100, 100))
Label_3.set_color((0, 0, 255))

Manager.add_component(Label_1)
Manager.add_component(Label_2)
Manager.add_component(Label_3)


while True:
    Manager.graphic_update()
    Manager.event_update()

