from manim import *
from math import log, e

from manim.utils.rate_functions import ease_in_out_quad


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
        equat_basic = MathTex("2", "^3", "=", "8")
        equat_basic.scale(4)
        self.play(Write(equat_basic))
        equat_transformed = MathTex("log", "^{}_2", "(", "8", ")", "=", "3").scale(4)
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

        equat_resplit = MathTex("log^{}_2(8)", "=", "3").scale(4)
        equat_resplit.save_state()
        equat_final = MathTex("2^{", "log^{}_2(8)}", "=", "8").scale(4)
        self.add(equat_resplit)
        changes = [(0, 1), (1, 2), (-1, -1)]

        self.play(
            FadeIn(equat_final[0], shift=UP),
            *[Transform(equat_resplit[i], equat_final[j]) for i, j in changes],
        )
        self.play(Restore(equat_resplit), FadeOut(equat_final[0]))

        self.remove(equat_resplit)

        equat_resplit_for_e = MathTex("log", "^{}_2", "(8)", "=3").scale(4)
        equat_with_e = MathTex("log", "^{}_e", "(8)", "=2.794").scale(4)
        self.play(
            *[
                ReplacementTransform(equat_resplit_for_e[i], equat_with_e[i])
                for i in range(len(equat_with_e))
            ]
        )

        self.remove(*self.mobjects)

        equat_with_e_copy = MathTex("l", "og^{}_e", "(8)=2.794").scale(4)
        self.add(equat_with_e_copy)
        equat_with_ln = MathTex("l", "n", "(8)", "=2.794").scale(4)
        equat_with_e_copy[-1].generate_target()
        equat_with_e_copy[-1].target.next_to(equat_with_ln[1], RIGHT, buff=SMALL_BUFF)

        self.play(
            ReplacementTransform(equat_with_e_copy[0], equat_with_ln[0]),
            FadeOut(equat_with_e_copy[1], shift=UP),
            FadeIn(equat_with_ln[1], shift=UP),
            MoveToTarget(equat_with_e_copy[-1]),
        )
        self.play(*[FadeOut(i, shift=UP) for i in self.mobjects])


class LogGraph(Scene):
    def construct(self):
        TANGENT_STROKE = 2.2
        TANGENT_LEN = 5

        title = Tex("Graph of $ln(x)$")
        title.scale(3.7)
        self.play(Write(title))
        self.play(FadeOut(title, shift=UP))

        axes = Axes(
            x_range=[0, 10],
            y_range=[-1, 3],
            tips=False,
            x_axis_config={"numbers_to_include": np.arange(1, 11)},
            y_axis_config={"numbers_to_include": np.arange(-1, 4)},
        )
        coord_labels = axes.get_coordinate_labels()
        x_labels, y_labels = coord_labels[0], coord_labels[1]
        t = ValueTracker(0.4)
        ln_func = lambda x: log(x, e)
        ln_graph = axes.get_graph(ln_func, color=MAROON, x_range=[0.3, 10])

        dot = Dot(point=ln_graph.point_from_proportion(t.get_value()))
        tangent_line = TangentLine(
            ln_graph, t.get_value(), TANGENT_LEN, stroke_width=TANGENT_STROKE
        )
        tangent_line.move_to(dot.get_center())
        ln_func_label = Tex("ln(x)")
        ln_func_label.next_to(ln_graph.point_from_proportion(0.9), UP + LEFT * 2)
        self.play(
            AnimationGroup(
                AnimationGroup(
                    *[Write(axes.axes[i]) for i in range(2)],
                    lag_ratio=0,
                ),
                AnimationGroup(
                    AnimationGroup(
                        *[Write(i) for i in x_labels], lag_ratio=0.1, run_time=0.07
                    ),
                    AnimationGroup(
                        *[Write(i) for i in y_labels], lag_ratio=0.1, run_time=0.07
                    ),
                    lag_ratio=0,
                ),
                Create(ln_graph),
                FadeIn(ln_func_label, shift=DOWN),
                lag_ratio=1,
            )
        )
        self.play(FadeIn(dot, scale=7))
        self.play(FadeIn(tangent_line, shift=tangent_line.get_unit_vector()))

        def line_updater(m: TangentLine):
            m.become(
                TangentLine(
                    ln_graph, t.get_value(), TANGENT_LEN, stroke_width=TANGENT_STROKE
                )
            )
            m.move_to(dot.get_center())
            return m

        dot.add_updater(
            lambda x: x.move_to(ln_graph.point_from_proportion(t.get_value()))
        )
        tangent_line.add_updater(line_updater)
        self.play(t.animate.set_value(0.07), rate_func=ease_in_out_quad)
        self.play(t.animate.set_value(1), rate_func=ease_in_out_quad)
        inverse_func = lambda x: 1 / x
        inverse_graph = axes.get_graph(inverse_func, color=GREEN, x_range=[0.3, 10])
        inverse_graph_label = MathTex(r"\frac{1}{x}")
        inverse_graph_label.next_to(
            inverse_graph.point_from_proportion(0.2), RIGHT * 2 + UP
        )
        self.play(
            AnimationGroup(
                AnimationGroup(
                    Create(inverse_graph),
                    FadeOut(dot),
                    Uncreate(tangent_line),
                    lag_ratio=0,
                ),
                FadeIn(inverse_graph_label, shift=DOWN),
                lag_ratio=1,
            )
        )

        def split_uncreatable_mobjects(arr):
            vmob = []
            mob = []
            for i in arr:
                if issubclass(i.__class__, VMobject):
                    vmob.append(i)
                else:
                    mob.append(i)
            return vmob, mob

        uncreatable, fadable = split_uncreatable_mobjects(self.mobjects)
        self.play(
            *[Uncreate(i) for i in uncreatable],
            *[FadeOut(i, shift=UP) for i in fadable],
            run_time=1.5,
        )
