# Koji_Engine_Document 

​	__Koji 引擎文档__

​	__Engine version 3.4 | Document version 1.0__

​	__Fix 2024.4.16__

---

## Introduction 介绍

​		Koji Engine 是我为了一个愚蠢而又充满理想的目标创建的项目, 从从初中写到现在, 也算是有了一定的规模. 到现在为止, 已经拥有了 图形系统, 事件系统, 线程系统 与对应的 API 接口. 接下来的开发目标将聚焦在资源管理系统与数据包的格式问题上. 再以后, 就要开发世界环境编辑器了.

​	这是我寄予厚望的项目. 无论如何我都希望它能达到新的高度, 虽然说这个引擎已经让我明白了很多的技术细节, 也了解了引擎的各个系统的运作流程与如何经行配合, 哪怕在未来这个引擎被弃用, 我也可以通过这段经历快速上手别的引擎

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
from API import GlobalAPI

GlobalAPI.register_global_environment_id()
```

​		如果需要导入外部 `Config` 文件对引擎进行参数调整, 则需要使用到 `ConfigManager` 的 `load_config_file()` 来载入数据并调用 `GlobalConstant` 的 `register_global_environment()` 函数

```Python
from API import ConfigAPI

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

