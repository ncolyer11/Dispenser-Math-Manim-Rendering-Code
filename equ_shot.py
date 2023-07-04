from manim import *


orange2 = "#FF7F50"

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

class highlight3(Scene):
    def construct(self):
        self.wait(0.2)

# Shot 1:
        starting_diff_eq = MathTex(
            r"di= \biggl(\frac{\textnormal{Output period}}{\textnormal{Input period}}-\frac{i}{D + i} \biggl)dt"
        )
        self.play(Create(starting_diff_eq, run_time=0.5))

        for group in search_shapes_in_text(starting_diff_eq, [MathTex(r"di"), MathTex(r"i")]):
            starting_diff_eq[0][group].set_color(BLUE_D)

        for group in search_shapes_in_text(starting_diff_eq, [MathTex(r"dt")]):
            starting_diff_eq[0][group].set_color(orange2)

        self.wait(1)

        for group in search_shapes_in_text(starting_diff_eq, [MathTex(r"\frac{i}{D + i}")]):
            self.play(Indicate(starting_diff_eq[0][group]), run_time=0.75)

        self.wait(1)

