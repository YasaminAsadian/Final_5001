import numpy as np
from functions.checking_rules import checking_rules_of_the_game
from functions.counting_neighbours import counting_neighbour_values_of_each_cell


def generate_the_new_matrix(matrix,boundary_type):
    """
    This function evaluates and applies the rules of the game to every individual 
    cell in a matrix based on the specified boundary condition, updating the state 
    of each cell. It then returns the updated matrix.

    Arguments:
        matrix: A matrix with the shape (mat_i, mat_j).
        boundary_type: A string specifying the boundary condition, either 'periodic' or 'non-periodic'.

    Returns:
        The matrix after applying the game's rules to each cell, reflecting the updated states.
    """

    mat_i, mat_j = matrix.shape
    matrix_updated = np.zeros((mat_i,mat_j))
    for i in range(mat_i):
        for j in range(mat_j):
            cell_value = matrix[i,j]
            neighbour_count = counting_neighbour_values_of_each_cell(matrix,i,j, boundary_type)
            cell_new_value = checking_rules_of_the_game(cell_value, neighbour_count)
            matrix_updated[i,j] = cell_new_value

    return matrix_updated
