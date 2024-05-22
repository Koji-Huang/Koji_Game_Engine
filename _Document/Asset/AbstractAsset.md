# AbstractAsset.py

---

这里定义了一个 `AbstractAsset` 类

## 属性

- `configObject`: `__init__`时绑定的 `config` 对象
- `name`: `Asset`对象的名称
- `path`: 对象在 `AssetRegister` 中的路径
- `type`: `Asset`对象的类型
- `active`: 是否已经实例化对象

## 方法

- `__init__(self, config)`

  > 初始化函数
  >
  > `config` : `AssetConfig` 对象, 即一个记录了 `Asset` 对象信息的 `Config` 对象

- `__copy__(self, copied: Asset=None)`

  > 复制函数
  >
  > `copied`: 如果赋值, 则将当前`Asset`对象的参数覆盖到 `copied` 上, 否则创建一个新对象作为 `copied` 返回
  >
  > `return`: 复制的对象

- `__call__(self, *args, **kwargs)`

  > 调用后调用 Asset 对象储存的对象的实例, 是一个抽象函数
  >
  > `return`: 实例化后的对象被调用产生的返回值

- `convert()`

  > 调用后返回 Asset 对象储存的对象的实例, 默认返回已经创建的对象, 是一个抽象函数
  >
  > `return`: 实例化后的对象

- `is_active()`

  > 判断这个 Asset 对象是否已经实例化过了, 是一个抽象函数
  >
  > `return` 布尔值

- `load`

  > 从 Config 对象载入数据的函数
  >
  > `return` 无