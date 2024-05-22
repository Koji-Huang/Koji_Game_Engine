# ConfigManagement

---

​	这个文件实现了 Config 的大多数函数

## 函数:

1. `load_config_file(config_path: str, config_type: str = None) -> ConfigObject:`

   > 通过文件路径生成 `Config` 对象
   >
   > > `config_path`: 文件所在的路径
   > >
   > > `config_type`: 文件的读取类型, 默认为自适应
   > >
   > > `return`: 生成的 `Config` 对象

2. `register_config(config_object: ConfigObject, keys: set[str] = None) -> None:`

   > 将 `Config` 对象注册到 `ConfigRegistry` 中
   >
   > > `config_object`: 注册的 `Config` 对象
   > >
   > > `keys`: 需要注册的值
   > >
   > > `return`: 无

3. `overload_config(config_object: ConfigObject, keys: set[str] = None) -> None:`

   > 将 `Config` 对象覆写到 `ConfigRegistry` 中
   >
   > > `config_object` :  `Config` 对象
   > >
   > > `keys`: 需要覆写的值
   > >
   > > `return`: 无

4. `unregister_config(config_object: ConfigObject, keys: set[str] = None) -> None:`

   > 将 `Config` 对象与值取消关联(但是值仍然存在)
   >
   > > `config_object`: `Config` 对象
   > >
   > > `keys`: 需要取消关联的值
   > >
   > > `return`: 无

5. `delete_config(config_object: ConfigObject, keys: set[str] = None) -> None:`

   > 将 `Config` 对象删除(连同值一起)
   >
   > > `config_object`: `Config` 对象
   > >
   > > `keys`: 需要一起删除的值
   > >
   > > `return`: 无

6. `save_config(config_object: ConfigObject, keys: set[str] = None) -> None:`

   > 将 `Config` 对象保存到文件中
   >
   > > `config_object`: `Config` 对象
   > >
   > > `keys`: 需要保存的值
   > >
   > > `return`: 无

7. `save_as_config(config_object: ConfigObject, output_path: str, keys: set[str] = None) -> None:`

   > 将 `Config` 对象另存为一个文件
   >
   > > `config_object`: `Config` 对象
   > >
   > > `output_path`: 保存的路径
   > >
   > > `keys`: 需要保存的值
   > >
   > > `return`: 无

8. `convert_to_asset(config_object: ConfigObject):`

   > 将 `Config` 对象转换为 `Asset` 对象
   >
   > > `config_object`: `Config` 对象
   > >
   > > `return`: 无

9. `match_config_object(config_type: str) -> type(ConfigObject):`

   > 通过字符串匹配并返回 `Config` 类型
   >
   > > `config_type`: 类型名字
   > >
   > > `return`: `Config` 类型