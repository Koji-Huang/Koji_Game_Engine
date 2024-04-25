# Asset File Standard Format

​	_资产文件书写规范_

---

​	资产类文件是在配置文件的基础上实现的一种文件, 现在在这里写出新增的特性

## .txt

​	`txt` 文件应该遵守以下要求:

> 必须包含有 `__asset_type`(资产文件的类型), `__asset_name` (资产文件的别名), `__asset_path` (资产文件的内部储存路径) 这三个键和对应的值, 另外, 原本 Config 中的 `__config_type`  一定为  `Asset`
>
> ```txt
> __config_type = Asset
> __asset_type = undefined
> __asset_name = undefined
> __asset_path = undefined
> ```

## .ini

​	`ini` 文件应该遵守以下要求:

>  `__file__` 节中的 `type`  一定为  `Asset`, 同时必须存在一个名为 `__asset__` ,包含有 `type`(资产文件的类型), `name` (资产文件的别名), `path` (资产文件的内部储存路径) 这三个键和对应的值的节
>
> ```ini
> [__file__]
> type = Asset
> 
> [__asset__]
> type = undefined
> name = undefined
> path = undefined
> ```

## .json

​	`json` 文件应该遵守以下几点要求:

> 1.  `__file__` 的对象中的`type`一定为 `Asset`, 同时必须存在一个名为 `__asset__` ,包含有 `type`(资产文件的类型), `name` (资产文件的别名), `path` (资产文件的内部储存路径) 这三个键和对应的值的对象
>
>    ```json
>    {  
>        "__file__": {
>        "type": "Asset"
>      },
>        "__asset__":{
>            "type" = "undefined"
>            "name" = "undefined"
>            "path" = "undefined"
>        }
>    }
>    ```
>
> 2. 与 `config` 类似,  `Asset` 也可以用嵌套的形式来进行子包的构建, 分为两种情况:
>
>    > (1): 作为配置文件出现的子项: 在这种情况下,  Asset 会归属与新创建的 Config 对象
>    >
>    > (2): 作为附属资产出现的子项: 在这种情况下, Asset 会归属于原本的 Config 对象 
>
>    ```json
>    {
>    	"__asset__": {
>            ...
>        },
>            
>        "作为配置文件出现的子项": {
>            "__file__": {...},
>            "__asset__": {...}
>        },
>                         
>        "作为附属资产出现的子项": {
>            "__asset__": {...}
>        }
>    }
>    ```
>
>    