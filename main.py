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


class ShowExpression(Scene):
    def construct(self):
        equat_basic = MathTex("{{2}}{{^3}}={{8}}")
        equat_basic.scale(4)
        self.play(Write(equat_basic))
        equat_transformed = MathTex("{{log}}{{^{}_2}}{{(}}{{8}}{{)}}={{3}}").scale(4)
        changes = [(0, 1), (2, 5), (3, 3)]
        self.play(
            FadeIn(equat_transformed[0], shift=RIGHT),
            *[FadeIn(equat_transformed[i], shift=UP) for i in [2, 4]],
            *[
                ReplacementTransform(equat_basic[i], equat_transformed[j])
                for i, j in changes
            ],
            ClockwiseTransform(equat_basic[1], equat_transformed[6]),
        )
        self.remove(*self.mobjects)
        equat_copy = equat_transformed.copy()
        self.add(equat_copy)
        self.play(Indicate(equat_copy[1]))
        self.play(Indicate(equat_copy[3]))
        self.play(Indicate(equat_copy[6]))
        self.remove(*self.mobjects)
        equat_resplit = MathTex("{{log^{}_2(8)}}={{3}}").scale(4)
        equat_resplit.save_state()
        equat_final = MathTex("2^{", r"log^{}_2(8)}", "=", "8").scale(4)
        self.add(equat_resplit)
        changes = [
            (0, 1),
            (1, 2),
            (-1, -1),
        ]
        self.play(
            FadeIn(equat_final[0], shift=UP),
            *[Transform(equat_resplit[i], equat_final[j]) for i, j in changes],
        )
        self.play(Restore(equat_resplit), FadeOut(equat_final[0]))
        self.remove(equat_resplit)
        equat_resplit_for_e = MathTex("{{log}}{{^{}_2}}{{(8)}}{{=3}}").scale(4)
        equat_with_e = MathTex("{{log}}{{^{}_e}}{{(8)}}{{=2.794}}").scale(4)
        self.play(
            *[
                ReplacementTransform(equat_resplit_for_e[i], equat_with_e[i])
                for i in range(len(equat_with_e))
            ]
        )
        self.remove(*self.mobjects)
        equat_with_e_copy = MathTex("{{l}}{{og^{}_e}}{{(8)=2.794}}").scale(4)
        self.add(equat_with_e_copy)
        equat_with_ln = MathTex("{{l}}{{n}}{{(8)}}{{=2.794}}").scale(4)
        equat_with_e_copy[-1].generate_target()
        equat_with_e_copy[-1].target.next_to(equat_with_ln[1], RIGHT, buff=SMALL_BUFF)

        self.play(
            ReplacementTransform(equat_with_e_copy[0], equat_with_ln[0]),
            FadeOut(equat_with_e_copy[1], shift=UP),
            FadeIn(equat_with_ln[1], shift=UP),
            MoveToTarget(equat_with_e_copy[-1]),
        )
        self.play(*[FadeOut(i, shift=UP) for i in self.mobjects])
