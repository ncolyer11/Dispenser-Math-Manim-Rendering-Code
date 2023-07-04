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

class canceling2(Scene):
    def construct(self):
        self.wait(0.2)


# Shot 8:
        initial_limit = MathTex(
            r"\frac{F}{(P-F)^{2}} \biggl(FD\cdot\ln\biggl(\biggl| \frac{(F-P)a-PD}{(F-P)i-PD} \biggl|\biggl) + (F-P)(a-i) \biggl) = \infty"
        )

        for group in search_shapes_in_text(initial_limit, [MathTex(r"_i"), MathTex(r"di"), MathTex(r"i")]):
            initial_limit[0][group].set_color(BLUE_D)      

        for group in search_shapes_in_text(initial_limit, [MathTex(r"_t"), MathTex(r"dt"), MathTex(r"t")]):
            initial_limit[0][group].set_color(orange2)
        
        for group in search_shapes_in_text(initial_limit, [MathTex(r"\infty")]):
            initial_limit[0][group].set_color(red2) 

        self.play(Write(initial_limit, run_time=1.3))
        self.wait(1)


# Shot 8.1:
        canceled_limit = MathTex(
            r"FD\cdot\ln\biggl(\biggl| \frac{(F-P)a-PD}{(F-P)i-PD} \biggl|\biggl) + (F-P)(a-i) = \infty"
        )

        for group in search_shapes_in_text(canceled_limit, [MathTex(r"_i"), MathTex(r"di"), MathTex(r"i")]):
            canceled_limit[0][group].set_color(BLUE_D)      

        for group in search_shapes_in_text(canceled_limit, [MathTex(r"_t"), MathTex(r"dt"), MathTex(r"t")]):
            canceled_limit[0][group].set_color(orange2)
        
        for group in search_shapes_in_text(canceled_limit, [MathTex(r"\infty")]):
            canceled_limit[0][group].set_color(red2) 

        self.play(TransformMatchingShapes(initial_limit, canceled_limit, run_time=1.3))
        self.wait(1)

# Shot 8.2:
        canceled_limit2 = MathTex(
            r"FD\cdot\ln\biggl(\biggl| \frac{(F-P)a-PD}{(F-P)i-PD} \biggl|\biggl) = \infty"
        )

        for group in search_shapes_in_text(canceled_limit2, [MathTex(r"_i"), MathTex(r"di"), MathTex(r"i")]):
            canceled_limit2[0][group].set_color(BLUE_D)      

        for group in search_shapes_in_text(canceled_limit2, [MathTex(r"_t"), MathTex(r"dt"), MathTex(r"t")]):
            canceled_limit2[0][group].set_color(orange2)
        
        for group in search_shapes_in_text(canceled_limit2, [MathTex(r"\infty")]):
            canceled_limit2[0][group].set_color(red2) 

        self.play(TransformMatchingShapes(canceled_limit, canceled_limit2, run_time=1.3))
        self.wait(1)

# Shot 9:
        reduced_limit = MathTex(
            r"\ln\biggl(\biggl| \frac{(F-P)a-PD}{(F-P)i-PD} \biggl|\biggl) = \infty"
        )

        for group in search_shapes_in_text(reduced_limit, [MathTex(r"_i"), MathTex(r"di"), MathTex(r"i")]):
            reduced_limit[0][group].set_color(BLUE_D)      

        for group in search_shapes_in_text(reduced_limit, [MathTex(r"_t"), MathTex(r"dt"), MathTex(r"t")]):
            reduced_limit[0][group].set_color(orange2)
        
        for group in search_shapes_in_text(reduced_limit, [MathTex(r"\infty")]):
            reduced_limit[0][group].set_color(red2) 

        self.play(TransformMatchingShapes(canceled_limit2, reduced_limit, run_time=1.3))
        self.wait(1)





