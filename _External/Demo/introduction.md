# Demo Package Introduction - Demo 介绍

------

## Animation:

> Animation 目前有两个 Demo - `Animation_draw_test_1` 和 `Animation_load_text`
>
> ### Animation_draw_test_1 
>
> > _update at 2024.4.23 engine environment version 3.3 ~ 3.4_
> >
> > 包含一个相对完整的测试, 有图像测试, 事件测试
> >
> > 可以控制测试样本数据
> >
> > 包含了 `pycallgraph`
>
> ### Animation_load_text 
>
> > _update at 2024.4.23 engine environment version 3.3 ~ 3.4_
> >
> > 内容是测试3种不同的 `Animation Config` 的导入

## Camera

> Camera 目前有两个 Demo - `Camera_test_1` 和 `Camera_test_2`
>
> ### Camera_test_1
>
> > _update at 2024.4.15 engine environment version 2.5 ~ 2.6_
> >
> > 内容是测试 `Camera` 的放大效果和跟踪效果
> >
> > 已损坏, 无法正常使用
>
> ### Camera_test_2
>
> > _update at 2024.4.17 engine environment version 2.5 ~ 2.6_
> >
> > 目的也是用来测试 `Camera` 的放大跟踪效果， 编写了  `follow_mouse` 这样的函数来跟踪
> >
> > 已损坏， 无法正常使用

## Event

> ### 	EventManager_test_1
>
> > _update at 2024.4.19 engine environment version 2.2 ~ 3.3_
> >
> > 内涵 `Text` 的显示和 `UI Event - Mouse Event` (新 `Event` 系统) 的测试
> >
> > 可以正常使用
>
> ### Mouse_test_main_1
>
> > _update at 2024.3.9 engine environment version ? ~ 2.2_
> >
> > 符合 2.x 没修改`Event`系统的旧版引擎的结构
> >
> > 不可用
>
> ### ThreadRunningMachine_test_1
>
> > _update at 2024.3.23 engine environment version 2.4 ~ 2.5_
> >
> > `Thread Running Machine` 的测试代码， 只是一个简单的不能再简单的代码
> >
> > 在 2024.4.23 加入了 `pycallgraph` 来测试性能， 但架构还是老架构， 所以仍然看作旧版处理
> >
> > 可用

## Graphic

> ### Graphic_copy_test_1
>
> > _update at 2024.3.18 engine environment version 2.2 ~ 2.5_
> >
> > `Graphic` 中的 `__copy__`功能的测试 (早期这玩意可让我遭老罪了)
> >
> > 在 2024.4.23 修正了架构， 但仍然仍为是老物
> >
> > 可用  
>
> ### Graphic_scale_test
>
> > _update at 2024.4.9 engine environment version 2.5 ~ 2.6_
> >
> > `Graphic` 中的 `scale` 功能测试
> >
> > 在 2024.4.23 修正了架构， 但并没有什么用
> >
> > 破损， 不可用
>
> ### Graphic_test_main_1
>
> > _update at 2024.3.19 engine environment version 2.2 ~ 2.4_
> >
> > 多个 `Graphic` 对象的压力测试（在那会可是主力来的
> >
> > 在 2024.4.23 修正了架构， 发现性能问题
> >
> > 可用 
>
> ### GraphicManager_test_1
>
> > _update at 2024.4.23 engine environment version 2.3 ~ 3.4_
> >
> > 针对 `GraphicManager` 的测试(超大杯)
> >
> > 有 `Debug` 测试, 有 `Event` 测试, 有 `pycallgraph` 可以说是最全的一个了
> >
> > 可用
>
> ### Markboard
>
> > _update at 2024.3.19 engine environment version 2.4~2.5_
> >
> > 疑似是早期用来测试 Debug 子功能的 Demo
> >
> > 不可用

## Pygame Tech(Technology)

> ### Blit_Special_Flag_test_1_text
>
> > 验证 `Special Flag` 特性的 Demo
> >
> > 所有版本可用
>
> ### Surfarry_tech_test_1
>
> > 验证 `Surfarry` 的实用性的 Demo
> >
> > 所有版本可用



