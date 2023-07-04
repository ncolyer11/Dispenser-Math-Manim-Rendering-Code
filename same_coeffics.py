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

class split_frac(Scene):
    def construct(self):
        self.wait(0.2)

# Shot 1:
        split_fraction = MathTex(
            r"\frac{F}{P-F} \int_{a}^{i} \frac{PD + i(P-F) - FD}{PD +i(P-F)}di = \int_{0}^{t}dt"
        )

        for group in search_shapes_in_text(split_fraction, [MathTex(r"_i"), MathTex(r"di"), MathTex(r"i")]):
            split_fraction[0][group].set_color(BLUE_D)      

        for group in search_shapes_in_text(split_fraction, [MathTex(r"_t"), MathTex(r"dt"), MathTex(r"t")]):
            split_fraction[0][group].set_color(orange2)   

        self.play(Create(split_fraction, run_time=1.3))
        self.wait(1)

        for group in search_shapes_in_text(split_fraction, [MathTex(r"P-F")]):
            self.play(Indicate(split_fraction[0][group]), run_time=0.75)

        self.wait(1)


