from ..Basic import BasicEvent as BasicEventObject, Inspector as FatherInspector
from GraphicComponent.UI import Label


class Basic(BasicEventObject):
    graphic_object: Label
    def __init__(self, graphic_object: Label, *args, **kwargs):
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
        pass

    def trigger(self, **kwargs):
        """
        trigger event.
        """
        pass

    def spread(self, **kwargs):
        """
        Spread event check to son graphic component.
        """

    def component_spread_args(self, args: dict, component: Label = None) -> dict:
        """
        When the Event spread to another new component, it will call this function.
        Main used for effect and mouse event.
        It receives args and return a fix arg for update_info()
        Notice: event always spread by father-son-level.
        :param component: if you want to specify a component to spread.
        :param args: the args to fix.
        :return: fix args.
        """
        pass