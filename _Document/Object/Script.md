# Script  Class Struct

​	_脚本类的类构造_

---

## 标准规范

​	脚本类是用与运行脚本来执行关卡行动的关键类, 在这里给出规范

> 1. 脚本类必须包含 `__call__` 函数
> 2. `__call__` 的调用必须传入一定的API, 比如图形类的 Script 必须传入 `GraphicAPI`, 关卡事件类的 `Script` 必须传入 `Level.API`
> 3. Script 不能直接调用系统 API( 但可以通过 Level 的构造间接调用 )
> 4. Script 最好要保证安全, 涉及系统的 Script 要谨慎关联关系

---

## Script 对象:

> ### 基础 Script 对象
>
> ```python
> from DataType.Config.Basic import Basic as Config
> 
> 
> class Script:
>     # 脚本的 ID (仅构造后赋值)
>     _script_id: str
>     # 脚本的 名称
>     _script_name: str
>     # 脚本的 临时参数
>     _script_kwargs: dict
>     # 脚本的 长期参数
>     _script_config: Config
>     # 脚本的 预读取项
>     _required: tuple[str]
>     
>     def __init__(self, config: Config = None, *args, **kwargs):
>         # 构造函数, 如果没有指定 Config 对象则创建一个 Config 对象
>         pass
>     
>     def __call__(self, *args, **kwargs):
>         # 运行 script
>         pass
> 
>     def __setitem__(self, item):
>         # 相当于 self.Basel.__setitem__
>         pass
>     
>     def __getitem__(self, item):
>         # 相当于 self.Basel.__getitem__
>         pass
>     
>     def __delitem__(self, item):
>         # 相当于 self.Basel.__delitem__
>         pass
>     
>     def save_config(self, *args, **kwargs):
>         # 将当前 Config 保存, 调用 Basel.__save__()
>         pass
>     
>     def load_config(self, config: Config):
>         # 将当前 Config 改为传入的 Config
>         pass
> ```

---

> ### 动画 Script 对象
>
> ```python
> from API import GraphicAPI 
> fron Script import Script as FatherScript
> from DataType.Config.Basic import Basic as Config
> from Graph import Animation
> 
> 
> class Script(FatherScript):
>     # 绑定的 Graphic Config
>     _graphic_config: Config
>     # 绑定的 Customized 对象
>     _Animation_object: Animation
>     pass
> 
> """
> 
> Graphic Config File Struct
> 
> config_type = "Graphic Script Config"
> sub_path = str
> name = str
> 
> kwargs = {...}
> 
> """
> ```

---

> 

