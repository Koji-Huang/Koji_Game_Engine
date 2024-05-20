from ..Basic.BasicCompositeObject import CompositeObject


class SpiritObject(CompositeObject):
    def __init__(self, pos, size, surface=None, *args, **kwargs):
        super().__init__(pos, size, surface, *args, **kwargs)
        self.config_file = ...
        self.script = ...
        self.asset = ...

    @staticmethod
    def composite_type():
        return {"Script", }.intersection(super().composite_type())
