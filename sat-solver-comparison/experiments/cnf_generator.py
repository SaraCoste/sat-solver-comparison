import random
import argparse
from pathlib import Path

def generate_random_clause(n, model=None):
    """Return a 3-literal clause over vars 1..n.
       If model is given, ensure the clause is satisfied by that model
       (helps generate guaranteed-SAT formulas)."""
    while True:
        lits = []
        for _ in range(3):
            var = random.randint(1, n)
            sign = random.choice([1, -1])
            lits.append(sign * var)
        if len(set(map(abs, lits))) < 3:        # avoid repeated var
            continue
        if model is None or any(
            (lit > 0 and model[abs(lit)]) or (lit < 0 and not model[abs(lit)])
            for lit in lits
        ):
            return lits

def generate_formula(n, alpha=4.3, satisfiable=False):
    m = int(alpha * n)          # number of clauses
    model = {i: random.choice([True, False]) for i in range(1, n + 1)} if satisfiable else None
    return [generate_random_clause(n, model) for _ in range(m)]

def write_dimacs(clauses, n, path):
    with open(path, "w") as f:
        f.write(f"p cnf {n} {len(clauses)}\n")
        for clause in clauses:
            f.write(" ".join(map(str, clause)) + " 0\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vars", type=int, required=True, help="Number of variables (n)")
    parser.add_argument("--alpha", type=float, default=4.3, help="Clause/var ratio (default 4.3)")
    parser.add_argument("--satisfiable", action="store_true", help="Guarantee formula is SAT")
    parser.add_argument("--output", type=str, required=True, help="Output DIMACS file")
    args = parser.parse_args()

    clauses = generate_formula(args.vars, args.alpha, args.satisfiable)
    write_dimacs(clauses, args.vars, Path(args.output))
    print(f"Wrote {len(clauses)} clauses to {args.output}")

if __name__ == "__main__":
    main()
