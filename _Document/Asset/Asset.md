# Asset Engine

---

## 介绍	

​	Asset 引擎主要由以下几个部分组成:

> ```
> .API
> 	|--- Asset.py
> .Asset
> 	|--- AssetReader.py
> 	|--- AssetWritter.py
> 	|--- AssetUniversal.py
> 	|--- DataType
> 		|--- __init__.py
> 		|--- AbstractAsset.py
> 		|--- Graph, Level, Music, Script, Spirit
> 			|--- ...
> .DataType
> 	|--- SystemComponent
> 		|--- AssetRegistry
> ```

1. API/Asset.py

   > 供系统调用的 API 接口, 提供基础的 I/O 接口

2. Asset/AssetQuote.py

   > 定义并生成一个读取接口 (类似于ID的那种), 用于获取, 绑定, 实例化 Asset 对象

3. Asset/AssetCreator.py

   > 定义并生成一个写入接口 (类似于ID的那种), 用于创建, 管理, 多态 Asset 对象

5. Asset/DataType/AbstrackAsset.py

   > Asset 对象的基型

6. DataType/SystemComponent/AssetRegistry.py

   > 保存在系统里的 Asset 管理器对象