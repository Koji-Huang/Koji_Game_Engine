# CompositeGraph 组合图像数据类型:

---

​	这类数据类型是由几种不同的数据类型组合而成的, 但他们都继承了 Graph 的数据类型, 这里规范以下 API

```
from Graph.Basic import Graph


class CompositeGraph(Graph):
	def __init__(self, ...):...
	
	def composite_type(self) -> tuple(type):...
	
	def udpate(self):...

```

