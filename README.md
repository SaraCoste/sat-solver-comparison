# SAT Solver Comparison: DPLL, WalkSAT, CDCL

This project implements and compares three SAT solving algorithms:
- **DPLL** – a backtracking-based complete solver
- **WalkSAT** – a stochastic local search algorithm
- **CDCL** – a modern conflict-driven solver using PySAT (Glucose3)

It accompanies the paper _“Comprehensive Comparative Analysis of SAT Solving Algorithms”_ written for the MPI course at West University of Timișoara.

---

## 🔧 Project Structure

├── src/
│ ├── dpll_solver.py # DPLL solver
│ ├── walksat_solver.py # WalkSAT solver
│ └── cdcl_solver.py # CDCL via PySAT
├── experiments/
│ ├── run.py # Runs solvers on .cnf files
│ └── cnf_generator.py # Random 3-SAT instance generator
├── requirements.txt
├── Dockerfile
└── README.md
