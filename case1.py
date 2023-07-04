from manim import *

green2 = "#0BDA51"
yellow2 = "#FFD700"
orange2 = "#FF7F50"
red2 = "#FF3131"
red3 = "#DC143C"

# finds a desired subtext and returns an array of all the appearances of it
def search_shape_in_text(text:VMobject, shape:VMobject):
    T = TransformMatchingShapes
    results = []
    l = len(shape.submobjects[0])
    shape_aux = VMobject()
    shape_aux.points = np.concatenate([p.points for p in shape.submobjects[0]])
    for i in range(len(text.submobjects[0])):
        subtext = VMobject()
        subtext.points = np.concatenate([p.points for p in text.submobjects[0][i:i+l]])
        if T.get_mobject_key(subtext) == T.get_mobject_key(shape_aux):
            results.append(slice(i, i+l))
    return results

# Like the previous function, but receives a list of possible sub-texts to search for
# written by abul4fia
def search_shapes_in_text(text:VMobject, shapes:list[VMobject]):
    results = []
    for shape in shapes:
        results += search_shape_in_text(text, shape)
    return results

class case1_neat(Scene):
    def construct(self):
        self.wait(0.2)

# Shot 1:
        example_vals = MathTex(
            r"\begin{split} \text{if }6000&=\dfrac{72000}{12},\text{then }D\frac{12}{12-4}<9\\ \text{else } D&=9-\frac{6000\cdot4}{8000} \end{split}"
        )

        for group in search_shapes_in_text(example_vals, [MathTex(r"D")]):
            example_vals[0][group].set_color(yellow2)
        self.play(Write(example_vals, run_time=1.3))
        self.wait(1)

        C = MathTex(r"\text{if }6000&=\dfrac{72000}{12},\text{then }D\frac{12}{12-4}<9")
        for group in search_shapes_in_text(example_vals, [C]):
            self.play(*[
                example_vals[0][group].animate.set_color(green2)
            ], run_time=1) 
        self.wait(1)

# Shot 2:
        simplified_example = MathTex(
            r"\text{if }6000&=6000,\text{then }D<6"
        )

        for group in search_shapes_in_text(simplified_example, [MathTex(r"D")]):
            simplified_example[0][group].set_color(yellow2)

        self.play(TransformMatchingShapes(example_vals, simplified_example, run_time=1.3))
        self.wait(1)
       