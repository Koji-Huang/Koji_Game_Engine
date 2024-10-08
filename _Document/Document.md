# Koji_Engine_Document 

​	__Koji 引擎文档__

​	__Engine version 3.4 | Document version 1.0__

​	__Fix 2024.4.16__

---

## Introduction 介绍

​		Koji Engine 是我为了一个愚蠢而又充满理想的目标创建的项目, 从从初中写到现在, 也算是有了一定的规模. 到现在为止, 已经拥有了 图形系统, 事件系统, 线程系统 与对应的 API 接口. 接下来的开发目标将聚焦在资源管理系统与数据包的格式问题上. 再以后, 就要开发世界环境编辑器了.

​	这是我寄予厚望的项目. 无论如何我都希望它能达到新的高度, 虽然说这个引擎已经让我明白了很多的技术细节, 也了解了引擎的各个系统的运作流程与如何经行配合, 哪怕在未来这个引擎被弃用, 我也可以通过这段经历快速上手别的引擎

---

## Running Flow 关卡运行流程

1. 读取路径下的 config.txt 进行初始化引擎

> 初始化引擎配置
> 读取 save_config 修正引擎配置
> 初始化引擎 

2. 通过 config.txt 中指定的数据载入各个 config 文件

> 读取 config 中的参数锁定 asset_package
> 读取各个 asset_package 来确定资源目录结构
> 载入各个 config 的基础参数 (name, sub_path 之类的)

3. 载入并显示启动关卡

> 检索 Level 包含的 config
> 检索 config 的资源与子 config 和 关联的 config
> 读取各个 config 中的 config
> 初始化 config 的资源并加载多出来的依赖
> 进入关卡

4. 运行

> 检查 ThreadAPI
>
> > Script 更新
> > Event 更新
> > Graphic 更新
> > Music 更新

​	__需要说明的是__

1. > _Level 并不直接参与到更新中, 他只是用来存放数据而已, 不具备更新功能_

2. > _每个关卡之间切换时都会将无用的关卡数据自动排除出缓存区, 但关卡可以通过指定来需要保留的资源用到下一个关卡中.预想中, 当下一个关卡读取时, 将从储存区中查找已储存与需要储存数据的交集来达到节省资源的目的_

3. > xxx.xxx (外部文件) -> Config (配置类, 用于提供IO还有格式化输出) -> Asset (资产类, 用于管理实例化对象与加载入系统)

---

## Asset 与 Config 与 Save

​	系统读取 Config 文件时会检查是否为 Asset 对象, 如果为 Asset 对象则会转换为 Asset 对象而不是记录在 Config 中, 而 Asset 对象储存有它所属的 Config 文件中, 同时 Asset 对象应该有可以存档的机制, Config 也应该有可以存档的机制, 但是 Asset 是依托于 Config 实现的存档

​	采用和 Windows 相同的结构来管理资产

```python
AssetFolder:
	assets: dict[Asset]  # 这层所有的资产对象
	folder: dict[AssetFolder]  # 子目录
	converted: dict[any]  # 转化过的对象

    convert(name) -> any:...  # 转化一个资产对象保存并传出
    convert_new(name) -> any:...  # 转化一个资产对象直接传出
    get(name) -> any:...  # 获得转化的对象, 若未转换则立即转化
    get_asset(name) -> Asset:... # 获得资产对象
    get_converted(name) -> any:... # 获得已转化的对象, 若未转化传出 None
    disconverted(name) -> None:...  # 将一个已转换对象删去
```

​	每一次尝试获取 `get(name)` 资产的对象时, 都会优先从已转化对象中取得

---

## Module 模块

- ### 	[Global Constant 全局变量](./GlobalConstant.md)

- ### 	[Asset 资产系统](./Asset/Asset.md)

- ### 	[Event 事件系统](.\Event\Event.md)

- ### 	[Function 拓展函数](.\Function\Function.md)

- ### 	[Graphic 图像系统](.\Graphic\Graphic.md)

- ### 	[Manager API 接口](.\Manager\Manager.md)

- ### [DataType 数据类型](.\DataType\DataType.md)

---

## Usage 使用

### 	GlobalAPI

​		GlobalAPI 时一个无需实例化的 API

​		每一次使用引擎时都需要 `GlobalAPI` 对 `ID` 对象进行初始化

```python
from API import Global

GlobalAPI.register_global_environment_id()
```

​		如果需要导入外部 `Config` 文件对引擎进行参数调整, 则需要使用到 `ConfigManager` 的 `load_config_file()` 来载入数据并调用 `GlobalConstant` 的 `register_global_environment()` 函数

```Python
from API import Config

config = ConfigAPI.load_config_file('../config.ini')
ConfigAPI.register_config(config)
```

### 	GraphicAPI

​		GraphicAPI 是一个需要实例化的 API, 实例化类为 API.GraphicAPI_type

​		如果要启用图像系统, 那么你需要导入 `Graphic` 中相对应的包, 如果你希望通过系统接口来控制, 那你需要导入 `GraphicManager` 来控制

```python
from API import GraphicAPI_type

Manager = GraphicAPI_type()
```

​		如果你想要创建一个窗体, 那么你既可以通过直接创建窗体对象并传入 `GraphicManager`, 也可以通过 `GraphicManager` 来创建窗体

```python
from API import GraphicAPI_type
from Graphic import MainWindows

windows = MainWindows((600, 800))
Manager = GraphicAPI_type(windows)
# it as same as next
Manager = GraphicAPI((600, 800))
```

​	如果需要打开 `Debug` 那么你可以在任意时刻将 `GraphicManager` 通过 `set_debug()` 来设置, 但在没有 `debug` 状态下, 不能修改 debug 的属性

```python
from API import GraphicAPI_type

Manager = GraphicAPI_type()
Manager.set_debug(True)
```

### 	EventAPI

​		EventAPI 是一个需要实例化的 API	

​		如果你想启用事件系统, 那么你需要导入 `Event` 中相应的包, 同样, `Event` 也有系统接口 `EventManager` 用于控制

```python
from API import EventAPI_type

Manager = EventAPI_type()
Manager.load_default_event()
```

​	如果你希望启用图像的事件系统, 那么你需要先载入默认事件, 再通过 `EventManaer.graphic_register()`将一个 `MainWindow` 实例绑定在 `EventManager` 上

```python
from API import EventAPI_type
from Graphic import MainWindows

windows = MainWindows()
manager = EventAPI_type()

master.load_default_event()

manager.graphic_register(windows)
```

### 	ThreadAPI

​		ThreadAPI 是一个需要实例化的 API	

​		如果你希望启用线程系统, 那么你需要导入 `Thread` 中的包, 同样,  `Thread` 也有系统接口 `ThreadManager` 用于控制

```python
from API import ThreadAPI_type

Manager = ThreadAPI_type()
Manager.TRMachine.start()
```

