# Config

---

## 介绍:

​	Config 这个模块是用来 载入&输出 外部数据的系统

​	主要的文件结构如下:

```
.Config
|--- Management.py
|--- ConfigRegistry.py
|--- XxxAssetConfig
|--- Basel
	|--- AbstractConfig.py
	|--- Ini.py
	|--- Txt.py
	|--- Json.py
	|--- Runtime.py
```

---

1. [Management](ConfigManagement.md)

   > 提供了对 Config 模块的基础操作

2. [XxxAssetConfig](AssetConfig.md)

   > 提供了对 `Asset` 对象的 `Config` 支持

3. [ConfigRegistry](ConfigRegistry.md)

   > 配置文件的注册表类型

4. [AbstractConfig](AbstractConfig.md)

   > Config 抽象基性对象

5. [Ini.py, Json.py, Txt.py, Runtime.py](BasicConfig.md)

   > Config 基础对象

​	另外, 对于 Config 类型的文件的数据格式定义, 我们使用另外一个文件 [ConfigFileType](ConfigFileType.md) 来储存这个内容

​	而对于 AssetConfig 类型的文件的数据格式定义, 请查看 [AssetConfigFileType](AssetConfigFileType.md).