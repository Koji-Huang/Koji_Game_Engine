# Config File Standard Format

​	_配置文件书写规范_

---

## .txt

​	`txt` 文件应该遵守以下几点要求:

> 1. 必须包含有 `__config_type`(配置文件的类型), `__name` (配置文件的别名), `__sub_path` (配置文件的内部储存路径) 这三个键和对应的值
>
>    ```txt
>    __config_type = undefined
>    __name = undefined
>    __sub_path = undefined
>    ```
>
> 2. 指定某个类型的值最好使用 类型_描述 的格式来命名键, 假定一个名为 `Graph` 的类, 它包含有 `image`, `surface` 这两个键
>
>    ```txt
>    # It's ok
>    Graph_image = undefined
>    Graph_surface = undefined
>    
>    # It's bad
>    image_Graph = undefined
>    graph_image = undefined
>    graphic_object_image = undefined
>    ```
>
> 3. 如果需要储存可迭代对象的值, 可以使用 类型-序号-后缀 这样的方式给键命名
>
>    ```txt
>    # It's ok
>    Graph_1_image = undefined
>    Graph_1_surface = undefined
>    Graph_2_image = undefined
>    Graph_2_surface = undefined
>    ```
>
> 4. 假如你希望某个值为空, 可以将它写为 None, 这时这个键指向的值为 None, 但如果不填值为空, 那么这个键将不会被载入
>
>    ```txt
>    Graph_name = None
>    ```
>
> 5. 键与值中不允许 `=` 或者转义字符出现
>
>    ```txt
>    # It's bad
>    happy = '=)'
>    hello world = "hello world\n"
>    format = \t\t\t
>    ```

## .ini

​	`ini` 文件应该遵守以下几点要求:

> 1. 必须包含有一个名为 `__file__` 的节, 其中必须包含`config_type`(配置文件的类型), `name` (配置文件的别名), `sub_path` (配置文件的内部储存路径) 这三个键和对应的值
>
>    ```ini
>    [__file__]
>    config_type = undefined
>    name = undefined
>    sub_path = undefined
>    ```
>
> 2. 指定某个类型的值最好将类型作为节的名称,  描述作为键 的格式来命名, 假定一个名为 `Graph` 的类, 它包含有 `image`, `surface` 这两个键
>
>    ```ini
>    [Graph]
>    image = undefined
>    name = undefined
>    sub_path = undefined
>    ```
>
> 3. 如果需要储存可迭代对象的值, 可以使用类型-序号 为节, 描述为键 这样的方式给键命名
>
>    ```ini
>    [Graph_1]
>    image = undefined
>    name = undefined
>    sub_path = undefined
>    
>    [Graph_2]
>    image = undefined
>    name = undefined
>    sub_path = undefined
>    
>    ```
>
> 4. 节, 键与值 不准存在`=`和转义字符

## .json

​	`json` 文件应该遵守以下几点要求:

> 1. 必须存在一个 `__file__` 的对象, 其中必须包含`config_type`(配置文件的类型), `name` (配置文件的别名), `sub_path` (配置文件的内部储存路径) 这三个键和对应的值
>
>    ```json
>    {  
>        "__file__": {
>        "name": "undefined",
>        "sub_path": "undefined",
>        "config_type": "undefined"
>      }
>    }
>    ```
>
> 2. 必须遵守 json 语法
>
> 3. 如果当前包的调用需要引起其他资源的调用, 可以使用一个名为 `__request__` 的包来声明 (注意, 这并不会改变包的调用顺序, 它仅会在 Asset 生成对象时用于检查并调用包), `__request__` 可以为列表和对象, 信息的查找是递归式的, 下面的例子都是合法的
>
>    ```json
>    {
>        "__request__":{
>                "Graphic": ["Resoure\\Graphic\\0001", "Resoure\\Graphic\\0002","Resoure\\Graphic\\0003"]
>        }
>        
>        "__request__": ["Resoure\\Graphic\\0001", "Resoure\\Graphic\\0002","Resoure\\Graphic\\0003"]
>    
>    	"__request__": "Resoure\\Graphic"
>    }
>    ```
>
> 4. 如果希望在这个包中构建子包, 那么你只需要在对应的包中加入 `__file__` 和对应的值就可以了, 子包对象的 sub_path 可以为空, 以关键字来确定上下关系, 在下面的每一个例子中, 都有两个包, 一个是 `Father`, 另一个是 `Son`, `Son`在 `Father.Son` 中
>
>    ```json
>    情况1, Son 为 Father 的子包, 同时 Son 也是一个包, Son 和 Fahter 构建在同一个文件下
>    {
>    	"Father":{
>            "__file__": {
>                "name": "undefined",
>                "sub_path": "undefined",
>                "config_type": "undefined"
>             },
>    		"Son":{
>                "__file__": {
>                    "name": "undefined",
>                    "sub_path": "undefined",
>                    "config_type": "undefined"
>                    }
>              }
>    	}
>    }
>       
>    情况2, Son 为 Father 的子包, 同时 Son 也是一个包, Son 指向外部的一个文件, Son 和 Fahter 不构建在同一个文件下
>    {
>    	"Father":{
>            "__file__": {
>                "name": "undefined",
>                "sub_path": "undefined",
>                "config_type": "undefined"
>             },
>    		"Son":{
>                "__file__": "out file path"
>            }
>    	}
>    }
>       
>    情况3, Son 为 Father 的子包, Son 为一个文件串的列表, Son 和 Fahter 不构建在同一个文件下
>    {
>    	"Father":{
>            "__file__": {
>                "name": "undefined",
>                "sub_path": "undefined",
>                "config_type": "undefined"
>             },
>    		"Son":{
>                "__file__": ["file path", "file path", "..."]
>            }
>    	}
>    }
>       
>    ```
>
>    