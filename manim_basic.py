from manim import *

class SquareScene(Scene):
    def construct(self):
        # Define the side lengths
        a = 2
        b = 1
        
        self.add_big_square(a, b)
            
    
    def add_big_square(self, a, b):
        total_length = a + b

        # Create the horizontal line (blue and red portions)
        blue_part = Line(ORIGIN, a * RIGHT, color=BLUE)
        red_part = Line(a * RIGHT, total_length * RIGHT, color=RED)
        horizontal_line = VGroup(blue_part, red_part)

        # Create the vertical line (green and yellow portions)
        blue_part2 = Line(a*UP, total_length * UP, color=RED)
        red_part2 = Line(ORIGIN, a*UP , color=BLUE)
        vertical_line = VGroup(red_part2, blue_part2)

        # Calculate the position for the intersection point
        intersection_point = red_part.get_end()

        # Move the vertical line to the intersection point
        vertical_line.move_to(intersection_point, aligned_edge=UP)

        # Add both lines to the scene
        lines = VGroup(horizontal_line, vertical_line)
        self.play(Create(horizontal_line))

        self.wait()

        horizontal_line_copy = horizontal_line.copy()
        self.add(horizontal_line_copy)
        self.play(Transform(horizontal_line, vertical_line))


    def add_little_squares(self, a, b):
        big_square = Square(side_length=a + b, color=WHITE, stroke_width=2)
        self.play(Create(big_square))
        
        # Create the first square
        square_a = Square(side_length=a, fill_opacity=0.5, color=BLUE)
        square_a.move_to(big_square.get_vertices()[0] - (b*UP + b*RIGHT) )

        self.play(Create(square_a))
        
        # Create the second square inside the first square
        square_b = Square(side_length=b, fill_opacity=0.5, color=RED)
        square_b.move_to(big_square.get_vertices()[2] + (b*UP + b*RIGHT)/2)
        self.play(Create(square_b))

        
        self.wait()

if __name__ == "__main__":
    scene = SquareScene()
    scene.render()
