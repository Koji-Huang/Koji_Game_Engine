from ThreadPackage import *
from GraphicComponent import *
from GraphicComponent.Effect import *
from GraphicComponent.UI import *

# Thread Init
MainThreadManager = ThreadManager()

# Graphic Init
ScreenWidth, ScreenHeight = 1440, 700
ScreenArgs = []

MainScreen = MainWindows((ScreenWidth, ScreenHeight), *ScreenArgs)

BackgroundWallpaper = Label((0, 0), (ScreenWidth, ScreenHeight))
BackgroundWallpaper.tree_bind_father(MainScreen)

TrafficMap = Label((0, 0), (MainScreen.w * 0.8, MainScreen.h))
TrafficMap.set_color((10, 10, 10))
TrafficMap.tree_bind_father(BackgroundWallpaper)
drawSquareBorder(TrafficMap.graph_primer_surface, 3, 3)

InfoMap = Label((MainScreen.w * 0.8, 0), (MainScreen.w * 0.2, MainScreen.h))
InfoMap.set_color((10, 10, 10))
InfoMap.tree_bind_father(BackgroundWallpaper)
drawSquareBorder(InfoMap.graph_primer_surface, 3, 3)

MainScreen.event_tree_build()


GraphicDrawUpdateThread = FunctionThread(MainScreen.graph_update, {'name': 'draw'}, threadLevel='system')

GraphicEventUpdateThread = FunctionThread(MainScreen.event_update, {'name': 'event'}, threadLevel='system')

MainThreadManager.add_thread(GraphicDrawUpdateThread, pool='Loop')
MainThreadManager.add_thread(GraphicEventUpdateThread, pool='Loop')


MainThreadManager.TRMachine.start()
