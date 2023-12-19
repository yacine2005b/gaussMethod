import numpy as np


def power_iteration(A, tolerance, max_iterations):
    n = len(A)
    vector_initial = np.random.rand(n)
    lambda_prev = 0

    for _ in range(1, max_iterations + 1):
        vector_estimated = np.dot(A, vector_initial)
        lambda_estimated = np.dot(vector_initial, vector_estimated)
        vector_initial = vector_estimated / np.linalg.norm(vector_estimated)

        if np.abs(lambda_estimated - lambda_prev) < tolerance:
            return lambda_estimated, vector_initial

        lambda_prev = lambda_estimated

    return lambda_estimated, vector_initial


def deflation(A, eigenvalue, eigenvector, tolerance, max_iterations):
    n = len(A)
    B = A - eigenvalue * np.outer(eigenvector, eigenvector)

    lambda2, vector2 = power_iteration(B, tolerance, max_iterations)
    return lambda2, vector2


def main():
    # Example matrix A
    A = np.array([[0, 1 / 4, 3 / 4], [3 / 4, 0, 1 / 4], [1 / 4, 3 / 4, 0]])

    tolerance = 1e-6
    max_iterations = 1000

    # Power Iteration
    lambda1, vector1 = power_iteration(A, tolerance, max_iterations)
    print("Dominant Eigenvalue (lambda1):", lambda1)
    print("Corresponding Eigenvector (vector1):", vector1)

    # Deflation
    lambda2, vector2 = deflation(A, lambda1, vector1, tolerance, max_iterations)
    print("Valeur propre dominante :", lambda2)
    print("vecteur propre correspondant :", vector2)


if __name__ == "__main__":
    main()
