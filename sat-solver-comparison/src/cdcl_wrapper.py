from pysat.solvers import Glucose3

def cdcl_solve(formula):
    solver = Glucose3()
    for clause in formula:
        solver.add_clause(clause)
    
    if solver.solve():
        model = solver.get_model()
        # Convert to a dictionary {var: True/False}
        assignment = {abs(lit): (lit > 0) for lit in model}
        return True, assignment
    else:
        return False, {}
