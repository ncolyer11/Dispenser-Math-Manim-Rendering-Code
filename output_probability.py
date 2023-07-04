from manim import *

class Equation2(Scene):
    def construct(self):
        self.wait(0.2)

# Shot 1:
        equation = MathTex(r"\text{Eject Chance}", r" = \frac{\text{Slots}}{\text{Unempty Slots}}")
        self.play(Write(equation))
        self.wait(1)

# Shot 2:
        subbed_in = MathTex(r"\text{Eject Chance}", r" = \frac{\text{1}}{\text{1+3}}")
        self.play(AnimationGroup(
            TransformMatchingShapes(equation[0], subbed_in[0], run_time=2.5),
            TransformMatchingShapes(equation[1], subbed_in[1], run_time=2.5)
        ))
        self.wait(1)

# Shot 3:
        two_on_five = MathTex(r"\text{Eject Chance} = \frac{\text{2}}{\text{2+3}}")
        self.play(TransformMatchingShapes(subbed_in, two_on_five, run_time=2.5))
        self.wait(1)

# Shot 4:
        three_on_six = MathTex(r"\text{Eject Chance} = \frac{\text{3}}{\text{3+3}}")
        self.play(TransformMatchingShapes(two_on_five, three_on_six, run_time=2.5))
        self.wait(1)

# Shot 5:
        one_on_two = MathTex(r"\text{Eject Chance} = \frac{\text{1}}{\text{2}}")
        self.play(TransformMatchingShapes(three_on_six, one_on_two, run_time=2.5))
        self.wait(1)

# Shot 6:
        one_on_two_equ_ratio = MathTex(r"\frac{\text{1}}{\text{2}} = \frac{\text{Output Period}}{\text{Input Period}}")
        self.play(TransformMatchingShapes(one_on_two, one_on_two_equ_ratio, run_time=2.5))
        self.wait(1)

# Shot 7:
        one_on_two_equ_four_on_eight = MathTex(r"\frac{\text{1}}{\text{2}} = \frac{\text{4gt}}{\text{8gt}}")
        self.play(TransformMatchingShapes(one_on_two_equ_ratio, one_on_two_equ_four_on_eight, run_time=2.5))
        self.wait(1)
