import sympy as sp
import numpy as np


def diagonalize_matrix(sp_M: sp.Matrix) -> None:
    """Print eigenvalues, eigenvectors and diagonalized matrix properties.
    
    Args:
        M: The input matrix as sympy matrix
    """
    # Define the matrix M
    np_M = np.array(sp_M).astype(np.float64)
    print("\nDiagonalizing matrix\nM = ")
    sp.pprint(sp_M)

    # Print eigenvalues and eigenvectors
    num_eigvals, num_eigvects = np.linalg.eig(np_M)
    print(f"\nNumerical eigenvalues: {sorted(list(num_eigvals))}")
    print("\nEigenvalue, alg #, eigenvector:")
    sp.pprint(sp_M.eigenvects())

    # Print diagonalized decomposition
    P1, D1 = sp_M.diagonalize()
    print("\nDecomposition matrices M=P*D*P**-1:")
    print("\nP=")
    sp.pprint(P1)
    print("\nD=")
    sp.pprint(D1)
    print("\nP**-1=")
    sp.pprint(P1**-1)


def main() -> None:
    """Calculate and print results here"""
    M_as_list = [[1, 1], [1 ,0]]
    diagonalize_matrix(1/sp.sqrt(3) * sp.Matrix(M_as_list))


if __name__ == "__main__":
    main()
