from z3 import *

solved_for_x = Solver()
# Create a boolean variable for each position on the board a..f
# and add it to the solver 

#Player X = True
#Player O = False
"""
GRID:
    a | b | c
    d | e | f
    g | h | i
"""
Xa = Bool('a')
Xb = Bool('b')
Xc = Bool('c')
Xd = Bool('d')
Xe = Bool('e')
Xf = Bool('f')
Xg = Bool('g')
Xh = Bool('h')
Xi = Bool('i')

Oa = Bool('a')
Ob = Bool('b')
Oc = Bool('c')
Od = Bool('d')
Oe = Bool('e')
Of = Bool('f')
Og = Bool('g')
Oh = Bool('h')
Oi = Bool('i')

"""
Constraint if X there cant be an Oa
"""
solved_for_x.add(Implies(Xa,Not(Oa)))
solved_for_x.add(Implies(Xb,Not(Ob)))
solved_for_x.add(Implies(Xc,Not(Oc)))
solved_for_x.add(Implies(Xd,Not(Od)))
solved_for_x.add(Implies(Xe,Not(Oe)))
solved_for_x.add(Implies(Xf,Not(Of)))
solved_for_x.add(Implies(Xg,Not(Og)))
solved_for_x.add(Implies(Xh,Not(Oh)))
solved_for_x.add(Implies(Xi,Not(Oi)))

"""
Constraint if O there cant be an X
"""
solved_for_x.add(Implies(Oa,Not(Xa)))
solved_for_x.add(Implies(Ob,Not(Xb)))
solved_for_x.add(Implies(Oc,Not(Xc)))
solved_for_x.add(Implies(Od,Not(Xd)))
solved_for_x.add(Implies(Oe,Not(Xe)))
solved_for_x.add(Implies(Of,Not(Xf)))
solved_for_x.add(Implies(Og,Not(Xg)))
solved_for_x.add(Implies(Oh,Not(Xh)))
solved_for_x.add(Implies(Oi,Not(Xi)))

"""
winning conditions Horizontal for X
"""





"""
Constraints in Horizontal Direction
"""




