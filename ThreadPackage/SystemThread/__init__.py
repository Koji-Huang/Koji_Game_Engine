from ..SystemThread.Init import Thread as Init
from ..SystemThread.Event import Thread as Thread
from ..SystemThread.File import Thread as File
from ..SystemThread.Graphic import Thread as Graphic
from ..SystemThread.Sound import Thread as Sound

Threads: tuple = (Thread, File, Graphic, Sound)
