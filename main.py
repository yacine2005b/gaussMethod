import numpy as np
import sys


def input_coefficients(matrixSize):
    matrixInput = np.zeros((matrixSize, matrixSize + 1))
    for i in range(matrixSize):
        for j in range(matrixSize + 1):
            matrixInput[i][j] = float(input("a[" + str(i) + "][" + str(j) + "]="))
    return matrixInput


def gaussian_elimination(matrixInput, matrixSize):
    for i in range(matrixSize):
        if matrixInput[i][i] == 0.0:
            sys.exit("Divide by zero detected!")

        for j in range(i + 1, matrixSize):
            ratio = matrixInput[j][i] / matrixInput[i][i]

            for k in range(matrixSize + 1):
                matrixInput[j][k] = matrixInput[j][k] - ratio * matrixInput[i][k]

    return matrixInput


def back_substitution(matrixInput, matrixSize):
    solution_vector = np.zeros(matrixSize)
    solution_vector[matrixSize - 1] = (
        matrixInput[matrixSize - 1][matrixSize]
        / matrixInput[matrixSize - 1][matrixSize - 1]
    )

    for i in range(matrixSize - 2, -1, -1):
        solution_vector[i] = matrixInput[i][matrixSize]

        for j in range(i + 1, matrixSize):
            solution_vector[i] = int(
                solution_vector[i] - matrixInput[i][j] * solution_vector[j]
            )

        solution_vector[i] = solution_vector[i] / matrixInput[i][i]

    return solution_vector


def display_solution(solution_vector, matrixSize):
    print("\nRequired solution is: ")
    for i in range(matrixSize):
        print("X%d = %0.2f" % (i, solution_vector[i]), end="\t")


def solve_linear_system():
   
    matrixSize = int(input("Enter the zize of the matrix: "))

    matrixInput = input_coefficients(matrixSize)

    matrixInput = gaussian_elimination(matrixInput, matrixSize)

    solution_vector = back_substitution(matrixInput, matrixSize)

    display_solution(solution_vector, matrixSize)


solve_linear_system()
