from manim import *

class stack3(Scene):
    def construct(self):
        self.wait(0.2)

# Shot 1:
        equation = MathTex(r"\text{Eject Chance}", r" = \frac{0}{3}")
        self.play(Write(equation))
        self.wait(1)

# Shot 2:
        subbed_in = MathTex(r"\text{Eject Chance}", r" = \frac{1}{4}")
        self.play(AnimationGroup(TransformMatchingShapes(equation, subbed_in, run_time=2.5)))
        self.wait(1)
