from z3 import *

def Exactly(*args, n):
    """Ensure exactly n arguments are True."""
    return And(Sum([If(arg, 1, 0) for arg in args]) == n)


def format_tic_tac_toe_board(solution):
    """Formats the Tic-Tac-Toe board from the solution into a readable ASCII format."""
    # Create a dictionary from the solution for easy access
    board_dict = {str(var): 'X' if val else 'O' for var, val in solution}

    # Define the board template
    board_template = """
    {a} | {b} | {c}
    ----------
    {d} | {e} | {f}
    ----------
    {g} | {h} | {i}
    """
    # Format the board with values from the solution
    formatted_board = board_template.format(**board_dict)

    return formatted_board

# The rest of your code remains the same


def tic_tac_toe_solver():
    # Create a boolean variable for each position on the board
    a = Bool('a')
    b = Bool('b')
    c = Bool('c')
    d = Bool('d')
    e = Bool('e')
    f = Bool('f')
    g = Bool('g')
    h = Bool('h')
    i = Bool('i')

    # Create a solver instance
    s = Solver()

    # Define all winning conditions
    winning_conditions_x = [
        And(a, b, c), And(d, e, f), And(g, h, i),
        And(a, d, g), And(b, e, h), And(c, f, i),
        And(a, e, i), And(c, e, g)
    ]
    # Define all winning conditions for O
    winning_conditions_o = [
        And(Not(a), Not(b), Not(c)), And(Not(d), Not(e), Not(f)), And(Not(g), Not(h), Not(i)),
        And(Not(a), Not(d), Not(g)), And(Not(b), Not(e), Not(h)), And(Not(c), Not(f), Not(i)),
        And(Not(a), Not(e), Not(i)), And(Not(c), Not(e), Not(g))
    ]

    # Constraint: Exactly one winning line must be true
    s.add(Exactly(*winning_conditions_x, n=1))

    # Constraint: No winning line for O should be true
    s.add(Not(Or(winning_conditions_o)))

    # Constraint on the number of X's and O's
    xs = [a, b, c, d, e, f, g, h, i]
    s.add(Sum([If(x, 1, 0) for x in xs]) == 5)  # 5 X's
    s.add(Sum([If(x, 0, 1) for x in xs]) == 4)  # 4 O's

    # Find and print all solutions
    solutions = []
    while s.check() == sat:
        m = s.model()
        solution = [(var, m[var]) for var in [a, b, c, d, e, f, g, h, i]]
        solutions.append(solution)
        # Avoid finding the same solution again
        s.add(Or([var != m[var] for var in [a, b, c, d, e, f, g, h, i]]))

    return solutions

# Execute the solver
tic_tac_toe_solutions = tic_tac_toe_solver()
print("Number of solutions:", len(tic_tac_toe_solutions))
print("First few solutions:", tic_tac_toe_solutions[:5])
for solution in range(len(tic_tac_toe_solutions)):
    print("Solution ", solution+1, ":")
    print(format_tic_tac_toe_board(tic_tac_toe_solutions[solution]))
