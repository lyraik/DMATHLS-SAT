from manimlib import *

class TicTacToeSATScene(Scene):
    def construct(self):
        self.wait(10)
        # Create the title
        title = Text("Tic Tac Toe Solver Using SAT", font_size=48).to_edge(UP)

        # Create the subtitle
        subtitle = Text("The Goal is to write a Tic Tac Toe solver using SAT", font_size=36).next_to(title, DOWN)

        # Author credit at the bottom
        author_credit = Text("Author: Simon Karrer", font_size=24).to_edge(DOWN)

        # Animate the addition of the title, subtitle, and author credit simultaneously
        self.play(Write(title), Write(subtitle), Write(author_credit))

        # List of challenges
        challenges = [
            "- Only solve games with all fields covered",
            "- Only solve games for X",
            '- For now "X" starts, so it has 5 fields - this can be changed easily'
        ]
        challenge_text = VGroup(*[Text(challenge, font_size=24) for challenge in challenges])
        challenge_text.arrange(DOWN, aligned_edge=LEFT).next_to(subtitle, DOWN * 2, buff=1)
        challenge_text.next_to(subtitle, DOWN, buff=1)

        # Animate the addition of each challenge
        for challenge in challenge_text:
            self.play(Write(challenge))

        # Adjust timing as needed
        self.wait(3)



class TicTacToeScene(Scene):
    positions = {
        'a': UP + LEFT,
        'b': UP,
        'c': UP + RIGHT,
        'd': LEFT,
        'e': ORIGIN,
        'f': RIGHT,
        'g': DOWN + LEFT,
        'h': DOWN,
        'i': DOWN + RIGHT
    }
    def draw_tic_tac_toe_grid(self):
        self.grid_lines = []
        grid_lines = [
            Line(UP * 0.5 + LEFT * 1.5, UP * 0.5 + RIGHT * 1.5),
            Line(DOWN * 0.5 + LEFT * 1.5, DOWN * 0.5 + RIGHT * 1.5), 
            Line(LEFT * 0.5 + UP * 1.5, LEFT * 0.5 + DOWN * 1.5),
            Line(RIGHT * 0.5 + UP * 1.5, RIGHT * 0.5 + DOWN * 1.5)
        ]
        for line in grid_lines:
            self.play(ShowCreation(line))
            self.grid_lines.append(line)

    def fill_ttt_grid_x_o(self, x_positions, o_positions):
        self.xo_text = []
        max_length = max(len(x_positions), len(o_positions))
        for i in range(max_length):
            if i < len(x_positions):
                pos_x = self.positions[x_positions[i]]
                x_text = Text("X", font_size=70).set_color(RED).move_to(pos_x)
                self.xo_text.append(x_text)
                self.add(x_text)
                self.wait(1)

            if i < len(o_positions):
                pos_o = self.positions[o_positions[i]]
                o_text = Text("O", font_size=70).set_color(BLUE).move_to(pos_o)
                self.xo_text.append(o_text)
                self.add(o_text)
                self.wait(1)

    def fill_ttt_grid_letters(self):
        self.letters = []
        for identifier in self.positions:
            letter_text = Text(identifier, font_size=70).set_color(BLUE).move_to(self.positions[identifier])
            self.letters.append(letter_text)
            self.add(letter_text)
            self.wait(0.25)

    def remove_grid(self):
        for line in self.grid_lines:
            self.remove(line)

    def remove_x_o(self):
        for text in self.xo_text:
            self.remove(text)

    def remove_letters(self):
        for letter in self.letters:
            self.remove(letter)

    def remove_everything(self):
        self.remove_grid()
        self.remove_x_o()
        self.remove_letters()

    def construct(self):
        self.wait(10)
        
        
        """
        #Scene 1:
        #we first draw a tictactoe grid then we add the letters
        #afterwards we start with determining winning conditions for that we draw Lines and add the boolean algebra
        """

        self.draw_tic_tac_toe_grid()
        # Uncomment as needed
        # self.fill_ttt_grid_x_o(x_positions, o_positions)
        self.fill_ttt_grid_letters()

        """
        #Horizontal boolean algebra
        """
        line_top = Line(LEFT * 1.5 + UP, RIGHT * 1.5 + UP).set_color(RED).set_stroke(width=10).set_opacity(0.5)
        self.play(ShowCreation(line_top),run_time=0.5)
        
        # Create the first text and display it
        text = Tex(r"(a \land b \land c)").set_color(WHITE).next_to(self.grid_lines[2], DOWN * 3)
        self.play(Write(text), run_time=0.3)
        self.wait(2)

        # Change the color of the existing text to blue
    
        # Create the lines
        line_middle = Line(LEFT * 1.5 + ORIGIN, RIGHT * 1.5 + ORIGIN).set_color(RED).set_stroke(width=10).set_opacity(0.5)
        line_bottom = Line(LEFT * 1.5 + DOWN, RIGHT * 1.5 + DOWN).set_color(RED).set_stroke(width=10).set_opacity(0.5)

        # Create the second text
        b_alg_horizontal = Tex(r"\text{Horizontal: }(a \land b \land c) \lor (d \land e \land \text{f}) \lor (g \land h \land \text{i})").set_color(WHITE).next_to(self.grid_lines[2], DOWN * 3)
        # Combine texts and align

        # Display the lines and the new combined text
        self.play(ShowCreation(line_top), ShowCreation(line_middle), ShowCreation(line_bottom), run_time=0.2)
        self.play(ReplacementTransform(text, b_alg_horizontal))
        #remove the old lines
        self.remove(line_top, line_middle, line_bottom)

        """
        #Vertical boolean algebra
        """
        line_left = Line(UP * 1.5 + LEFT, DOWN * 1.5 + LEFT).set_color(RED).set_stroke(width=10).set_opacity(0.5)
        line_middle = Line(UP * 1.5 + ORIGIN, DOWN * 1.5 + ORIGIN).set_color(RED).set_stroke(width=10).set_opacity(0.5)
        line_right = Line(UP * 1.5 + RIGHT, DOWN * 1.5 + RIGHT).set_color(RED).set_stroke(width=10).set_opacity(0.5)
        # Create the second text
        b_alg_vertical = Tex(r"\text{Vertikal: } (a \land d \land g) \lor (b \land e \land h) \lor (c \land \text{f} \land \text{i} )").set_color(WHITE).next_to(self.grid_lines[2], DOWN * 5)
        # Combine texts and align
        # Display the lines and the new combined text
        self.play(ShowCreation(line_left), ShowCreation(line_middle), ShowCreation(line_right))
        self.play(Write(b_alg_vertical))
        self.wait(2)
        #remove lines
        self.remove(line_left, line_middle, line_right)

        """
        #Diagonal boolean algebra
        """
        line_left_right = Line(UP * 1.5 + LEFT * 1.5, DOWN * 1.5 + RIGHT * 1.5).set_color(RED).set_stroke(width=10).set_opacity(0.5)
        line_right_left = Line(UP * 1.5 + RIGHT * 1.5, DOWN * 1.5 + LEFT * 1.5).set_color(RED).set_stroke(width=10).set_opacity(0.5)

        #create the third text
        b_alg_diagonal = Tex(r" \text{Diagonal: }(a \land e \land \text{i}) \lor (c \land e \land g)").set_color(WHITE).next_to(self.grid_lines[2], DOWN * 7)

        #display the lines and the new combined text
        self.play(ShowCreation(line_left_right), ShowCreation(line_right_left))
        self.play(Write(b_alg_diagonal))
        self.wait(2)
        #remove lines
        self.remove(line_left_right, line_right_left)

        """
        #remove everything
        """
        self.wait(5)
        self.remove_letters()
        self.remove_grid()
        self.remove(b_alg_horizontal, b_alg_vertical, b_alg_diagonal)

class TicTacToeScene2(Scene):
    def construct(self):
        self.wait(10)
        """
        #Show the winning conditions for X and O
        """
        title_z = Text("Implementation into Z3(SAT Solver)", font_size=60).to_edge(UP)
        self.play(Write(title_z))

        # Title for winning conditions for X
        title_x = Text("Winning Conditions for X", font_size=48).next_to(title_z, DOWN * 2)
        self.play(Write(title_x))

        # Boolean algebra for winning conditions for X
        b_alg_horizontal_x = Tex(r"\text{Horizontal: }(a \land b \land c) \lor (d \land e \land f) \lor (g \land h \land i)").set_color(WHITE).next_to(title_x, DOWN * 1.5)
        b_alg_vertical_x = Tex(r"\text{Vertical: } (a \land d \land g) \lor (b \land e \land h) \lor (c \land f \land i)").set_color(WHITE).next_to(b_alg_horizontal_x, DOWN)
        b_alg_diagonal_x = Tex(r"\text{Diagonal: }(a \land e \land i) \lor (c \land e \land g)").set_color(WHITE).next_to(b_alg_vertical_x, DOWN)
        
        self.add(b_alg_horizontal_x, b_alg_vertical_x, b_alg_diagonal_x)

        # Title for winning conditions for O
        title_o = Text("Winning Conditions for O", font_size=48).next_to(b_alg_diagonal_x, DOWN * 2)
        self.play(Write(title_o))

        # Boolean algebra for winning conditions for O (inverted)
        b_alg_horizontal_o = Tex(r"\text{Horizontal: }(\overline{a} \land \overline{b} \land \overline{c}) \lor (\overline{d} \land \overline{e} \land \overline{f}) \lor (\overline{g} \land \overline{h} \land \overline{i})").set_color(WHITE).next_to(title_o, DOWN * 1.5)
        b_alg_vertical_o = Tex(r"\text{Vertical: } (\overline{a} \land \overline{d} \land \overline{g}) \lor (\overline{b} \land \overline{e} \land \overline{h}) \lor (\overline{c} \land \overline{f} \land \overline{i})").set_color(WHITE).next_to(b_alg_horizontal_o, DOWN)
        b_alg_diagonal_o = Tex(r"\text{Diagonal: }(\overline{a} \land \overline{e} \land \overline{i}) \lor (\overline{c} \land \overline{e} \land \overline{g})").set_color(WHITE).next_to(b_alg_vertical_o, DOWN)

        self.add(b_alg_horizontal_o, b_alg_vertical_o, b_alg_diagonal_o)







class TicTacToeScene3d(ThreeDScene):
    def construct(self):
        self.camera.frame.set_euler_angles(theta=50 * DEGREES, phi=60 * DEGREES)

       # Create and add 3D grids
        grids = self.create_3d_grids()
        for grid in grids:
            self.play(ShowCreation(grid))

        
        self.wait(2)

    def create_3d_grids(self):
        grids = []
        grid = self.create_single_grid(z_offset=2)
        grids.append(grid)
        grid = self.create_single_grid(z_offset=0)
        grids.append(grid)
        grid = self.create_single_grid(z_offset=-2)
        grids.append(grid)
        
        return grids

    def create_single_grid(self, z_offset=0):
        grid = VGroup()
        # Horizontal and vertical lines
        # Assuming each cell in the grid is of unit length
        for x in np.linspace(-1, 1, 4):  # 4 lines to create 3 cells
            # Vertical lines
            grid.add(Line(start=np.array([x, 1, z_offset]), end=np.array([x, -1, z_offset])))
            # Horizontal lines
            grid.add(Line(start=np.array([1, x, z_offset]), end=np.array([-1, x, z_offset])))
        return grid

# To run this scene, use the command: manimgl your_script.py TicTacToeScene3d
