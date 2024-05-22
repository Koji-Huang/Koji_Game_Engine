# Asset Engine

---

## 介绍

​	Asset 引擎主要由以下几个部分组成:

> ```
> .Asset
> 	|--- Management.py
> 	|--- AssetCreator.py
> 	|--- AssetQuote.py
> 	|--- AbstractAsset.py
> 	|--- AssetRegistry.py
> 	|--- Graph, Level, Music, Script, Spirit
> 		|--- ...
> ```

1. [Management.py](.\AssetManagement.md)

   > 供系统调用的 API 接口, 提供基础的 I/O 接口

2. [AssetQuote.py](AssetQuote.md)

   > 针对 Asset 编写的值快捷方式对象

3. [AssetCreator.py](AssetCreator.md)

   > 定义并生成一个写入接口 (类似于ID的那种), 用于创建, 管理, 多态 Asset 对象

5. [AbstractAsset.py](AbstractAsset.md)

   > Asset 对象的基型

6. [AssetRegistry.py](AssetRegistry.md)

   > 保存在系统里的 Asset 管理器对象

---

## 使用方式

### 	函数

​		 Asset 包载入了 Management 里的所有函数, 在外部调用时 `Asset.Management.xxx = Asset.xxx`

​		这意味着: 几乎所有的函数都写在了 Management 里, 如有需要 请跳转至 Management 里查看具体的用法

### 	变量:

- `RegisteredAssetType`

  > 注册了的资产数据类型, 当系统调用创建资产时会从这里查找匹配的资产数据类型

- `AssetRegistry`

  > 资产的管理器, 所有标记有 path 的资产都会保存在这个对象中

