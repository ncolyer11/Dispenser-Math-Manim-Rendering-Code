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

class shots(Scene):
    def construct(self):
        self.wait(0.2)

# Shot 1:
        starting_diff_eq = MathTex(
            r"di= \biggl(\frac{\textnormal{Output period}}{\textnormal{Input period}}-\frac{i}{D + i} \biggl)dt"
        )
        self.play(Write(starting_diff_eq, run_time=2.5))

        for group in search_shapes_in_text(starting_diff_eq, [MathTex(r"di"), MathTex(r"i")]):
            self.play(*[
                starting_diff_eq[0][group].animate.set_color(BLUE_D)
            ], run_time=0.15)

        for group in search_shapes_in_text(starting_diff_eq, [MathTex(r"dt")]):
            self.play(*[
                starting_diff_eq[0][group].animate.set_color(orange2)
            ], run_time=0.15)     

        self.wait(1)

# Shot 2:
        concise_diff_eq = MathTex(
            r"di= \biggl(\frac{P}{F}-\frac{i}{D + i} \biggl)dt"
        )

        for group in search_shapes_in_text(concise_diff_eq, [MathTex(r"di"), MathTex(r"i")]):
            concise_diff_eq[0][group].set_color(BLUE_D)      

        for group in search_shapes_in_text(concise_diff_eq, [MathTex(r"dt"), MathTex(r"t")]):
            concise_diff_eq[0][group].set_color(orange2)       

        self.play(TransformMatchingShapes(starting_diff_eq, concise_diff_eq, run_time=1.3))
        self.wait(1)

# Shot 3:
        initial_integral = MathTex(
            r"\int_{a}^{i}\frac{F(D+i)}{P(D+i)-Fi} di= \int_{0}^{t}dt"
        )
        
        for group in search_shapes_in_text(initial_integral, [MathTex(r"_i"), MathTex(r"di"), MathTex(r"i")]):
            initial_integral[0][group].set_color(BLUE_D)      

        for group in search_shapes_in_text(initial_integral, [MathTex(r"_t"), MathTex(r"dt"), MathTex(r"t")]):
            initial_integral[0][group].set_color(orange2)   

        self.play(TransformMatchingShapes(concise_diff_eq, initial_integral, run_time=1.3))
        self.wait(1)


# Shot 4:
        same_coeffics = MathTex(
            r"\frac{F}{P-F} \int_{a}^{i} \frac{PD + i(P-F) - FD}{PD +i(P-F)}di = \int_{0}^{t}dt"
        )

        for group in search_shapes_in_text(same_coeffics, [MathTex(r"_i"), MathTex(r"di"), MathTex(r"i")]):
            same_coeffics[0][group].set_color(BLUE_D)      

        for group in search_shapes_in_text(same_coeffics, [MathTex(r"_t"), MathTex(r"dt"), MathTex(r"t")]):
            same_coeffics[0][group].set_color(orange2)   

        self.play(TransformMatchingShapes(initial_integral, same_coeffics, run_time=1.3))
        self.wait(1)

# Shot 5:
        split_fraction = MathTex(
            r"\frac{F^{2}D}{(P-F)^{2}} \int_{a}^{i} \frac{P-F}{FD}-\frac{P-F}{PD+(P-F)i}di = \int_{0}^{t}dt"
        )

        for group in search_shapes_in_text(split_fraction, [MathTex(r"_i"), MathTex(r"di"), MathTex(r"i")]):
            split_fraction[0][group].set_color(BLUE_D)      

        for group in search_shapes_in_text(split_fraction, [MathTex(r"_t"), MathTex(r"dt"), MathTex(r"t")]):
            split_fraction[0][group].set_color(orange2)   

        self.play(TransformMatchingShapes(same_coeffics, split_fraction, run_time=1.3))
        self.wait(1)

# Shot 6:
        integrated_expression = MathTex(
            r"\frac{F^{2}D}{(P-F)^{2}} \biggl[ \frac{P-F}{FD}i-\ln(|PD +i(P-F)|) \biggl]_{a}^{i} = [t]_{0}^{t}"
        )

        for group in search_shapes_in_text(integrated_expression, [MathTex(r"_i"), MathTex(r"di"), MathTex(r"i")]):
            integrated_expression[0][group].set_color(BLUE_D)      

        for group in search_shapes_in_text(integrated_expression, [MathTex(r"_t"), MathTex(r"dt"), MathTex(r"t")]):
            integrated_expression[0][group].set_color(orange2)   

        self.play(TransformMatchingShapes(split_fraction, integrated_expression, run_time=1.3))
        self.wait(1)

# Shot 7:
        simplified_expression = MathTex(
            r"\frac{F}{(P-F)^{2}} \biggl(FD\cdot\ln\biggl(\biggl| \frac{(F-P)a-PD}{(F-P)i-PD} \biggl|\biggl) + (F-P)(a-i) \biggl) = t"
        )

        for group in search_shapes_in_text(simplified_expression, [MathTex(r"_i"), MathTex(r"di"), MathTex(r"i")]):
            simplified_expression[0][group].set_color(BLUE_D)      

        for group in search_shapes_in_text(simplified_expression, [MathTex(r"_t"), MathTex(r"dt"), MathTex(r"t")]):
            simplified_expression[0][group].set_color(orange2)   

        self.play(TransformMatchingShapes(integrated_expression, simplified_expression, run_time=1.3))
        self.wait(1)

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

        self.play(TransformMatchingShapes(simplified_expression, initial_limit, run_time=1.3))
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

        self.play(TransformMatchingShapes(initial_limit, reduced_limit, run_time=1.3))
        self.wait(1)

# Shot 10:
        zeroed_limit_expression = MathTex(
            r"\biggl| \frac{(F-P)i-PD}{(F-P)a-PD} \biggl| = \text{e}^{-\infty }=0"
        )

        for group in search_shapes_in_text(zeroed_limit_expression, [MathTex(r"_i"), MathTex(r"di"), MathTex(r"i")]):
            zeroed_limit_expression[0][group].set_color(BLUE_D)      

        for group in search_shapes_in_text(zeroed_limit_expression, [MathTex(r"_t"), MathTex(r"dt"), MathTex(r"t")]):
            zeroed_limit_expression[0][group].set_color(orange2)
        
        for group in search_shapes_in_text(zeroed_limit_expression, [MathTex(r"^{\infty}")]):
            zeroed_limit_expression[0][group].set_color(red2) 

        self.play(TransformMatchingShapes(reduced_limit, zeroed_limit_expression, run_time=1.3))
        self.wait(1)

# Shot 11:
        simplified_limit = MathTex(
            r"i\rightarrow \frac{PD}{F-P} \text{ as }t\rightarrow \infty"
        )

        for group in search_shapes_in_text(simplified_limit, [MathTex(r"_i"), MathTex(r"di"), MathTex(r"i")]):
            simplified_limit[0][group].set_color(BLUE_D)      

        for group in search_shapes_in_text(simplified_limit, [MathTex(r"_t"), MathTex(r"dt"), MathTex(r"t")]):
            simplified_limit[0][group].set_color(orange2)
        
        for group in search_shapes_in_text(simplified_limit, [MathTex(r"\infty")]):
            simplified_limit[0][group].set_color(red2) 

        self.play(TransformMatchingShapes(zeroed_limit_expression, simplified_limit, run_time=1.3))
        self.wait(1)

# Shot 12:
        L_eq_min = MathTex(
            r"L=\text{min}\biggl(\frac{PD}{F-P},9-D\biggl)"
        )

        self.play(TransformMatchingShapes(simplified_limit, L_eq_min, run_time=1.3))

        for group in search_shapes_in_text(L_eq_min, [MathTex(r"L")]):
            self.play(*[
                L_eq_min[0][group].animate.set_color(green2)
            ], run_time=0.6)
        self.wait(1)

# Shot 13:
        ejection_chance = MathTex(
            r"\text{Ejection Chance}=\frac{L}{D+L}"
        )

        for group in search_shapes_in_text(ejection_chance, [MathTex(r"L")]):
            ejection_chance[0][group].set_color(green2)

        self.play(TransformMatchingShapes(L_eq_min, ejection_chance, run_time=1.3))
        self.wait(1)

# Shot 14:
        items_output_ph = MathTex(
            r"\text{Items Output/h}=\frac{L}{D+L}\cdot\frac{72000}{P}"
        )

        for group in search_shapes_in_text(items_output_ph, [MathTex(r"L")]):
            items_output_ph[0][group].set_color(green2)

        self.play(TransformMatchingShapes(ejection_chance, items_output_ph, run_time=1.3))
        self.wait(1)

# Shot 15:
        yucky_fraction = MathTex(
            r"O=\frac{\text{min}\Bigl(\dfrac{PD}{F-P},9-D\Bigl)}{D+\text{min}\Bigl(\dfrac{PD}{F-P},9-D\Bigl)}\cdot\frac{72000}{P}"
        )

        L1 = MathTex(r"\text{min}\Bigl(\dfrac{PD}{F-P},9-D\Bigl)")
        L2 = MathTex(r"\text{min}\biggl(\frac{PD}{F-P},9-D\biggl)")
        for group in search_shapes_in_text(yucky_fraction, [L1]):
            yucky_fraction[0][group].set_color(green2)

        self.play(TransformMatchingShapes(items_output_ph, yucky_fraction, run_time=1.3))
        self.wait(1)

# Shot 16:
        min_as_piecewise = MathTex(
            r"\text{min}\biggl(\frac{PD}{F-P},9-D\biggl)\,=\begin{cases}\dfrac{PD}{F-P},&\text{if }\dfrac{PD}{F-P}<9-D\\9-D\:\,,&\text{else}\end{cases}"
        )
        
        for group in search_shapes_in_text(min_as_piecewise, [L1]):
            min_as_piecewise[0][group].set_color(green2)
        
        for group in search_shapes_in_text(min_as_piecewise, [L2]):
            min_as_piecewise[0][group].set_color(green2)
        
        self.play(Unwrite(yucky_fraction, run_time=1.5))
        self.wait(1)

        self.play(Write(min_as_piecewise, run_time=3.0))
        self.wait(1)

# Shot 17:
        clunky_fraction = MathTex(
            r"O=\begin{cases}\frac{\frac{PD}{F-P}}{D+\frac{PD}{F-P}}\cdot\dfrac{72000}{P},&\text{if }\dfrac{PD}{F-P}<9-D\\\dfrac{9-D}{D+9-D}\cdot\dfrac{72000}{P},&\text{else}\end{cases}"
        )
        
        self.play(Unwrite(min_as_piecewise, run_time=1.5))
        self.wait(1)

        self.play(Write(clunky_fraction, run_time=2.5))

        for group in search_shapes_in_text(clunky_fraction, [MathTex(r"{}_{{}_D}"), MathTex(r"_D"), MathTex(r"D")]):
            self.play(*[
                clunky_fraction[0][group].animate.set_color(yellow2)
            ], run_time=0.11) 
        
        self.wait(1)

# Shot 18:
        yummy_fraction = MathTex(
            r"O=\begin{cases}\dfrac{72000}{F},&\text{if }D\dfrac{F}{F-P}<9\\\dfrac{8000(9-D)}{P},&\text{else}\end{cases}"
        )

        for group in search_shapes_in_text(yummy_fraction, [MathTex(r"D")]):
            yummy_fraction[0][group].set_color(yellow2)

        self.play(TransformMatchingShapes(clunky_fraction, yummy_fraction, run_time=1.3))
        self.wait(1)

# Shot 19:
        by_cases = MathTex(
            r"\begin{split} \text{if }O&=\dfrac{72000}{F},\text{then }D\frac{F}{F-P}<9\\ \text{else } D&=9-\frac{OP}{8000} \end{split}"
        )

        for group in search_shapes_in_text(by_cases, [MathTex(r"D")]):
            by_cases[0][group].set_color(yellow2)

        self.play(TransformMatchingShapes(yummy_fraction, by_cases, run_time=1.3))
        self.wait(1)

# Shot 20:
        example_vals = MathTex(
            r"\begin{split} \text{if }6000&=\dfrac{72000}{8},\text{then }D\frac{8}{8-4}<9\\ \text{else } D&=9-\frac{6000\cdot4}{8000} \end{split}"
        )

        for group in search_shapes_in_text(example_vals, [MathTex(r"D")]):
            example_vals[0][group].set_color(yellow2)
        self.play(TransformMatchingShapes(by_cases, example_vals, run_time=1.3))
        self.wait(1)

        C0 = MathTex(r"\text{if }6000&=\dfrac{72000}{8},\text{then }D\frac{8}{8-4}<9")
        C1 = MathTex(r"\text{if }6000&=9000,\text{then }D<\frac{9}{2}")
        for group in search_shapes_in_text(example_vals, [C0]):
            self.play(*[
                example_vals[0][group].animate.set_color(red3)
            ], run_time=1) 
        self.wait(1)

# Shot 20.5:
        simplified_example_vals = MathTex(
            r"\begin{split} \text{if }6000&=9000,\text{then }D<\frac{9}{2}\\ \text{else } D&=9-\frac{6000\cdot4}{8000} \end{split}"
        )

        for group in search_shapes_in_text(simplified_example_vals, [C1]):
            simplified_example_vals[0][group].set_color(red3)
        self.play(TransformMatchingShapes(example_vals, simplified_example_vals, run_time=1.3))
        self.wait(1)
     
        for group in search_shapes_in_text(simplified_example_vals, [MathTex(r"\text{else } D&=9-\frac{6000\cdot4}{8000}")]):
            self.play(ApplyWave(simplified_example_vals[0][group], run_time=1))
        self.wait(1)

# Shot 21:
        bottom_case = MathTex(
            r"D=9-\frac{24000}{8000}"
        )

        for group in search_shapes_in_text(bottom_case, [MathTex(r"D")]):
            bottom_case[0][group].set_color(yellow2)

        self.play(TransformMatchingShapes(simplified_example_vals, bottom_case, run_time=1.3))
        self.wait(1)

# Shot 22:
        nine_minus_six = MathTex(
            r"D=9-3"
        )

        for group in search_shapes_in_text(nine_minus_six, [MathTex(r"D")]):
            nine_minus_six[0][group].set_color(yellow2)

        self.play(TransformMatchingShapes(bottom_case, nine_minus_six, run_time=1.3))
        self.wait(1)

# Shot 23:
        d_equals_three = MathTex(
            r"D=6"
        )

        for group in search_shapes_in_text(d_equals_three, [MathTex(r"D")]):
            d_equals_three[0][group].set_color(yellow2)

        self.play(TransformMatchingShapes(nine_minus_six, d_equals_three, run_time=1.3))
        self.wait(1)
