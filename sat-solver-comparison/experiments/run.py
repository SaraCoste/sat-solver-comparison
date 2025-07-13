import time
import argparse
from pathlib import Path
from src.dpll_solver import dpll
from src.walksat_solver import walksat
from src.cdcl_solver import cdcl_solve

def parse_cnf(filepath):
    with open(filepath, 'r') as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith('c')]
    header = next(line for line in lines if line.startswith('p'))
    num_vars = int(header.split()[2])
    clauses = []
    for line in lines:
        if line.startswith('p'):
            continue
        clause = [int(x) for x in line.split() if x != '0']
        clauses.append(clause)
    return clauses, num_vars

def run_solver(solver_name, formula):
    if solver_name == 'dpll':
        return dpll(formula)
    elif solver_name == 'walksat':
        return walksat(formula)
    elif solver_name == 'cdcl':
        return cdcl_solve(formula)
    else:
        raise ValueError(f"Unknown solver: {solver_name}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--solver', type=str, choices=['dpll', 'walksat', 'cdcl'], required=True)
    parser.add_argument('--input', type=str, required=True)
    args = parser.parse_args()

    formula, _ = parse_cnf(args.input)
    start = time.time()
    sat, assignment = run_solver(args.solver, formula)
    end = time.time()

    print(f"Satisfiable: {sat}")
    if sat:
        print("Assignment (partial):", dict(list(assignment.items())[:10]), "...")
    print(f"Runtime: {end - start:.4f} seconds")

if __name__ == "__main__":
    main()
