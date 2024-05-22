# AssetManagement

---

这个文件包含了对 Asset 模块的操作

## 变量

> 无

## 函数

- `load_asset(config)`

  > 这条函数用于载入 `Asset` 对象
  >
  > `config: AssetObject`
  >
  > > `config` 为 `AssetConfig` 对象
  > >
  > > 基于 AssetConfig 对象创建的 Asset 对象, 创建后自动加入到 `RegistredAsset` 中
  > >
  > > `return` 生成的 `Asset` 对象
  >
  > `config: str`
  >
  > > `config` 为 `str` 对象
  > >
  > > 根据字符匹配创建一个基础的对象
  > >
  > > `return` 生成的 `Asset` 对象

- `load_system_asset_type()`

  > 载入系统的 `AssetType` 进入 `RegisteredAsset` 中
  >
  > `return` 无