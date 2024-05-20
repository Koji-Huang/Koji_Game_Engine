from Graphic.Basic.Graph import Graph


class CompositeObject(Graph):
    def __init__(self, pos, size, surface=None, *args, **kwargs):
        super().__init__(self, pos, size, surface, *args, **kwargs)

    @staticmethod
    def composite_type():
        return {Graph, }
