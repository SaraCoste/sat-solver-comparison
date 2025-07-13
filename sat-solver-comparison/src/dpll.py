def is_clause_satisfied(clause, assignment):
    return any(assignment.get(abs(lit), lit < 0) == (lit > 0) for lit in clause)

def is_formula_satisfied(formula, assignment):
    return all(is_clause_satisfied(clause, assignment) for clause in formula)

def find_unit_clause(formula, assignment):
    for clause in formula:
        unassigned = [lit for lit in clause if abs(lit) not in assignment]
        if len(unassigned) == 1:
            return unassigned[0]
    return None

def dpll(formula, assignment={}):
    if is_formula_satisfied(formula, assignment):
        return True, assignment

    if any(all(abs(lit) in assignment and
               ((lit > 0) != assignment[abs(lit)])
               for lit in clause) for clause in formula):
        return False, {}

    unit = find_unit_clause(formula, assignment)
    if unit is not None:
        assignment[abs(unit)] = unit > 0
        return dpll(formula, assignment)

    var = next(v for clause in formula for v in map(abs, clause)
               if v not in assignment)

    for value in [True, False]:
        new_assign = assignment.copy()
        new_assign[var] = value
        sat, final = dpll(formula, new_assign)
        if sat:
            return True, final

    return False, {}
