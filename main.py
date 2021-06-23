from manim import *


class Intro(Scene):
    def construct(self):
        intro_q = Tex(r"What \textit{are} ", "logorithms", "?").scale(2)
        intro_q[1].set_color(YELLOW)
        self.play(Write(intro_q), run_time=1.5)
        intro_ans = VGroup(
            Tex(
                "the logarithm is the ",
                r"\textit{inverse}",
                " function to exponentiation.",
            ),
            Tex(r"That means the logarithm of a given number $x$ is the exponent"),
            Tex(r"to which another fixed number, the base $b$, must be raised,"),
            Tex(r"to produce that number $x$."),
        )
        intro_ans.arrange(DOWN).scale(0.9)
        intro_ans.shift(DOWN * 0.4)
        intro_q.generate_target()
        intro_q.target.next_to(intro_ans, UP, buff=SMALL_BUFF * 5)
        intro_q.target.scale(0.8)
        self.play(FadeIn(intro_ans, shift=UP), MoveToTarget(intro_q))
        self.play(*[FadeOut(i, shift=UP) for i in self.mobjects])
