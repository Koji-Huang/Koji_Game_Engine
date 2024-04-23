import pygame.time
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

with PyCallGraph(output=GraphvizOutput()):
    from API import GlobalAPI
    from API import GraphicAPI_type
    from API import EventAPI_type
    from DataType.Asset.Graphic.Animation import Package

    GlobalAPI.register_global_environment()
    GraphicManager = GraphicAPI_type(size=(1600, 900))
    EventManager = EventAPI_type()
    EventManager.load_default_event()


    TXT = Package(
        "../../Graphic/EffectFunction\\TextureMapping\\Noise\\_texture_\\gradient(quadratic)(1980x1980)\\config.txt")


    Animation = TXT.convert()
    Animation.animation_frame_size = 20
    Animation.animation_frame_rate = 100


    def next_frame(cost_time):
        self = Animation
        if self.graph_kwargs.get('frame direct'):
            cost_frame = cost_time * self.animation_frame_rate * self.graph_kwargs.get('frame direct')

            if self.graph_kwargs.get('frame direct') == 1:
                if self.animation_last_update_frame + cost_frame > self.animation_frame_size:
                    self.graph_kwargs['frame direct'] = -1
                    return int(self.animation_frame_size * 2 - self.animation_last_update_frame - cost_frame)
            else:
                if self.animation_last_update_frame + cost_frame < 0:
                    self.graph_kwargs['frame direct'] = 1
                    return -int(self.animation_last_update_frame + cost_frame)
            return int(self.animation_last_update_frame + cost_frame)
        else:
            self.graph_kwargs['frame direct'] = 1
            return 0


    Animation.next_frame = next_frame

    GraphicManager.component_add(Animation)

    clock = pygame.time.Clock()
    for i in range(200):
        clock.tick_busy_loop(1000)
        print(clock.get_fps())
        Animation.graph_active = True
        GraphicManager.graphic_update()
        pygame.event.get()

pass