# AbstractConfig

---

​	AbstractConfig 对象是个 Mapping 对象

## 属性:

- `config_path`: `Config`对象的注册路径
- `config_name`: `Config`对象的名称
- `config_type`: `Config`对象的类型
- `file_path`: 载入的文件路径 
- `son_config`: `Config`对象的子对象
- `_translated_data`: 将文件内容转化后的内容
- `_read_value`: 原始读取内容

## 方法:

- `__init__(self, file_path: str)`:

  > 初始函数
  >
  > > `file_path`: 文件路径

- `__translate_read__(self)`:

  > 抽象函数, 用于将原始读取数据转化并保存到 `_translated_data` 中
  >
  > 无输入与返回值

- `__translate_write__(self)`:

  > 抽象函数, 用于将`_translated_data `转化并保存到 `_read_value` 中
  >
  > 无输入与返回值

- `__setitem__(self, key: str, value: any)`:

  > 基础用法不赘述

- `__getitem__(self, item: str) -> any`:

  > 基础用法不赘述

- `__delitem__(self, key: str)`:

  > 基础用法不赘述

- `__dict__(self)`:

  > 基础用法不赘述

- `read(self)`:

  > 读入数据
  >
  > 无输入与返回值

- `write(self, key: str, value: str)`:

  > 写入数据 (立即保存到文件中)
  >
  > 无输入与返回值

- `save(self, file_path=None)`:

  > 保存文件
  >
  > 无输入与返回值

- `update(self, collection: dict)`:

  > 从另一个集合更新自己的内容
  >
  > 无输入与返回值

- `get_file_type(file_path=None) -> str`:

  > 获取`Config`文件类型
  >
  > > `file_path` 不为空时作函数, 可传入字符串和 Config 对象, 在实例化对象内做方法
  > >
  > > `return` 返回文件类型的字符串

- `convert(self) -> (str, Asset | AssetFolder, str)`:

  > 将 `Config` 转化为 `Asset` 对象
  >
  > > `return` Asset 名称, Asset 对象, Asset 路径

- `info(self, *args)`:

  > 返回这个对象的信息 (dict)

- `detail_info(self, *args)`:

  > 返回更详细的信息 (dict)

- `keys(self)`:

  > 继承至 dict

- `values(self)`:

  > 继承至 dict

- `items(self)`:

  > 继承至 dict

  