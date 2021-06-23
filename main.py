from manim import *


class Intro(Scene):
    def construct(self):
        intro_q = Tex(r"What \textit{are} ", "logorithms", "?").scale(2)
        self.add(intro_q)