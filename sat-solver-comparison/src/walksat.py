import random

def is_satisfied(clause, assignment):
    return any((lit > 0 and assignment.get(abs(lit), False)) or
               (lit < 0 and not assignment.get(abs(lit), True))
               for lit in clause)

def count_unsatisfied_clauses(formula, assignment):
    return sum(not is_satisfied(clause, assignment) for clause in formula)

def walksat(formula, max_flips=10000, prob_random=0.5):
    # Initial random assignment
    vars_in_formula = {abs(lit) for clause in formula for lit in clause}
    assignment = {var: random.choice([True, False]) for var in vars_in_formula}

    for _ in range(max_flips):
        unsatisfied = [clause for clause in formula if not is_satisfied(clause, assignment)]
        if not unsatisfied:
            return True, assignment

        clause = random.choice(unsatisfied)

        if random.random() < prob_random:
            # Flip a random variable in the clause
            var = abs(random.choice(clause))
        else:
            # Flip the variable that minimizes unsatisfied clauses
            best_var = None
            min_unsat = float('inf')
            for lit in clause:
                var = abs(lit)
                assignment[var] = not assignment[var]  # Flip
                unsat_count = count_unsatisfied_clauses(formula, assignment)
                assignment[var] = not assignment[var]  # Revert
                if unsat_count < min_unsat:
                    min_unsat = unsat_count
                    best_var = var
            var = best_var

        assignment[var] = not assignment[var]  # Flip selected var

    return False, assignment
