# Level Class Struct

_关卡类的构造_

---

```python
class Level:	
    # 这些 sub_path 用于在载入关卡时进行预读取与取舍
    # 关卡预读取的 Spirit 的 sub_path 集合
    required_spirit: tuple[str]
    # 关卡预读取的 Picture 的 sub_path 集合
    required_picture: tuple[str]
    # 关卡预读取的 Customized 的 sub_path 集合
    required_animation: tuple[str]
	# 关卡预读取的 Script 的 sub_path 集合
    required_script: tuple[str]
    # 关卡预读取的 Music 的 sub_path 集合
    required_music: tuple[str]
    
    start_script: str
    update_script: str
    quit_script: str
    level_config: str
    
    def __init__(self, *args, **kwargs):
        pass
    
    def save_config(self, *args, **kwargs):
        pass
    
    def save_level_state(self, *args, **kwargs):
        pass
    
    def quit(self, *args, **kwargs):
        pass
    
    def start(self, *args, **kwargs):
        pass
    
    def update(self, *args, **kwargs):
        pass
    
    def with_debug(self, *args, **kwargs
                  ):
        pass
    
    def __call__(self, *args, **kwargs):
        pass
```

