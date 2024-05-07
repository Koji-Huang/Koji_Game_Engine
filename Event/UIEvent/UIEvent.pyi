from ..BasicEvent import BasicEvent as BasicEventObject, Inspector as FatherInspector
from Graphic.UI import Label


class Basic(BasicEventObject):
    skip_track: bool
    graphic_object: Label

    def __init__(self, graphic_object: any, skip_track: bool = False, *args, **kwargs):
        ...

    def track_check(self, *args, **kwargs):
        """
        do as father's do
        """
        pass

    def track_run(self, *args, **kwargs):
        """
        run track and give a new arg:
        graphic_component: self.graphic_component
        :return: None
        """
        pass

    def update_info(self, graphic_object: Label = None, **kwargs):
        """
        new info add:
        :param graphic_object: set self.graphic_object
        :return: None
        """
        pass

    def delete(self):
        """
        delete self and remove self from father if didn't
        :return: None
        """
        pass

    def __copy__(self, copied: Basic = None):
        """
        new copy info add：
        copied.graphic_object = self.graphic_object
        """
        pass



class Inspector(FatherInspector):
    target_event: Basic
    def __init__(self, *args, **kwargs):
        """
        Inspector is used to trigger event object with args. (args won't come from space)
        :param target: the target event to trigger
        """
        pass

    def check(self, **kwargs):
        """
        check if event can be trigger
        """
        return self.target_event.track_check(**kwargs, **self.spread_kwargs())

    def trigger(self, **kwargs):
        """
        trigger event.
        """
        return self.target_event.track_run(**kwargs, **self.spread_kwargs())

    def spread(self, **kwargs):
        """
        Spread event check to son graphic component.
        """

    def update_kwargs(self, component = None):
        pass