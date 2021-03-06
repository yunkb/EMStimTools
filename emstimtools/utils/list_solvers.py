from dolfin import (list_krylov_solver_methods, list_krylov_solver_preconditioners, list_lu_solver_methods)

def list_solvers():
    print("###############")
    print("Direct solvers:")
    print("###############")
    print(list_lu_solver_methods())
    print("###############")
    print("Krylov solvers:")
    print("###############")
    print(list_krylov_solver_methods())
    print("################")
    print("Preconditioners:")
    print("################")
    print(list_krylov_solver_preconditioners())
