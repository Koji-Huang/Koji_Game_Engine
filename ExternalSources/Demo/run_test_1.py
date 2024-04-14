import cProfile
import pstats

import pygame.font

from GraphicComponent.UI import *
from GraphicComponent import MainWindows


def main():

    Main = MainWindows((1600, 800), pygame.NOFRAME)

    image = Image((0, 0), (1600, 900), r"C:\Users\Administrator\PycharmProjects\Koji_Game_Engine\TestInfo\__klee_nahida_qiqi_diona_sayu_and_2_more_genshin_impact_drawn_by_neko_sake1__44cf20a2d68da284b66568fdf5a6972d.png")
    A = Label((100, 100), (120, 50))
    B = Label((200, 100), (120, 50))
    C = Label((300, 100), (100, 50))
    D = Label((100, 75), (300, 50))
    E = Label((30, 10), (100, 50))
    F = Label((60, 20), (100, 50))
    text = Text((300, 300), (300, 300), "Hello World!",
                pygame.font.SysFont(pygame.font.get_fonts()[0], 36), False, (255, 100, 100))

    A.set_color((255, 0, 0, 100))
    B.set_color((0, 255, 0, 100))
    C.set_color((0, 0, 255, 100))
    D.set_color((255, 255, 255, 100))
    E.set_color((0, 0, 255, 100))
    F.set_color((0, 0, 255, 100))

    Main.tree_add_son(image)
    Main.tree_add_son(A)
    image.tree_add_son(B)
    image.tree_add_son(C)
    image.tree_add_son(D)
    Main.tree_add_son(text)
    image.tree_add_son(E)
    image.tree_add_son(F)

    Clock = pygame.time.Clock()

    for i in range(1000000):
        Clock.tick_busy_loop(1000)
        Main.update()

        if not (i % 60):
            text.change_text_text(str(Clock.get_fps()))

        A.x += 1
        if pygame.time.get_ticks() > 6000:
            quit()


if __name__ == "__main__":
    profiler = cProfile.Profile()  # 实例化 Profile 类
    main()  # 调用封装的脚本入口函数
    stats = pstats.Stats(profiler).sort_stats(pstats.SortKey.CUMULATIVE)  # 根据 profile 实例构造 Stats 类，并执行排序
    stats.print_stats()