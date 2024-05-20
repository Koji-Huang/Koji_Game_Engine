from .BasicAssetConfig import AssetConfig


class Script(AssetConfig):
    def __init__(self, father_script, script_name):
        self.bind_config_file = father_script
        self["path"] = self.bind_config_file["Script"][script_name]['path']
        self["name"] = self.bind_config_file["Script"][script_name]['name']
        self["flags"] = self.bind_config_file["Script"][script_name]['flags']
        self.script = self.bind_config_file["Script"][script_name]

    def info(self, *args):
        ret = super().info(*args)
        ret['script_name'] = self.script['name']
        ret['script_flags'] = self.script['flags']
        ret['script_file'] = self.script['file']
        return ret

    def __getattr__(self, item):
        return self.bind_config_file.__getitem__(str(item))

    def __setitem__(self, key, value):
        return self.bind_config_file.__setitem__(key, value)

    def __delitem__(self, key):
        return self.bind_config_file.__delitem__(key)

    def __getitem__(self, item):
        return self.bind_config_file.__getitem__(item)