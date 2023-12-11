import numpy as np
from functions.checking_rules import checking_rules_of_the_game
from functions.counting_neighbours import counting_neighbour_values_of_each_cell
from functions.update_matrix import generate_the_new_matrix

#The following matrices are the actual parameters for the tests
MATRIX_3_BY_3 = np.array([[0, 0, 0],
                        [1, 1, 0],
                        [0, 0, 1]])

MATRIX_4_BY_4 = np.array([[1, 0, 0, 0],
                        [0, 0, 1, 0],
                        [0, 1, 0, 1],
                        [1, 0, 0, 1]])

MATRIX_5_BY_5 = np.array([[1, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0],
                        [0, 1, 0, 1, 0],
                        [1, 0, 1, 0, 0],
                        [0, 0, 0, 0, 1]])

MATRIX_6_BY_6 = np.array([[0, 0, 1, 0, 0, 1],
                        [0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 1, 0],
                        [0, 1, 1, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0, 1]])

MATRIX_7_BY_7 = np.array([[1, 0, 0, 0, 0, 1, 0],
                        [0, 1, 0, 1, 0, 1, 0],
                        [1, 1, 0, 0, 0, 1, 1],
                        [0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 1, 0, 1, 0, 1],
                        [0, 1, 0, 0, 1, 0, 0],
                        [1, 1, 0, 1, 0, 1, 1]])

MATRIX_8_BY_8 = np.array([[0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 1, 1, 0, 0, 0, 0, 1],
                        [0, 0, 1, 0, 1, 0, 1, 1],
                        [0, 0, 1, 0, 1, 1, 1, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 1, 0, 1, 0, 0, 1],
                        [0, 1, 1, 1, 0, 0, 1, 0],
                        [1, 1, 0, 0, 0, 1, 1, 1]])

#The following matrices are the expected parameters for the tests
UPDATED_MATRIX_3_BY_3 = np.array([[0, 0, 0],
                                [0, 1, 0],
                                [0, 1, 0]])

UPDATED_MATRIX_4_BY_4 = np.array([[0, 0, 0, 0],
                                [0, 1, 1, 0],
                                [0, 1, 0, 1],
                                [0, 0, 1, 0]])

UPDATED_MATRIX_5_BY_5 = np.array([[0, 0, 0, 0, 0],
                                [0, 1, 1, 0, 0],
                                [0, 1, 0, 1, 0],
                                [0, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0]])

UPDATED_MATRIX_6_BY_6 = np.array([[0, 0, 1, 1, 1, 0],
                                [0, 0, 0, 1, 1, 0],
                                [0, 0, 1, 0, 1, 0],
                                [0, 0, 1, 0, 1, 0],
                                [0, 1, 0, 1, 1, 0],
                                [0, 0, 1, 1, 1, 0]])

UPDATED_MATRIX_7_BY_7 = np.array([[0, 0, 0, 0, 0, 1, 0],
                                [0, 1, 1, 0, 0, 1, 0],
                                [1, 1, 0, 0, 0, 1, 1],
                                [0, 1, 1, 1, 1, 0, 0],
                                [0, 0, 1, 0, 1, 1, 0],
                                [0, 1, 0, 0, 1, 0, 0],
                                [0, 1, 1, 0, 0, 1, 0]])

UPDATED_MATRIX_8_BY_8 = np.array([[0, 0, 1, 0, 0, 1, 0, 0],
                                [1, 1, 1, 0, 0, 1, 1, 1],
                                [1, 0, 1, 0, 1, 0, 0, 1],
                                [0, 1, 0, 0, 1, 0, 1, 0],
                                [1, 0, 0, 0, 1, 0, 1, 0],
                                [1, 0, 1, 0, 0, 0, 0, 1],
                                [0, 0, 0, 1, 1, 0, 0, 0],
                                [1, 1, 0, 1, 1, 1, 1, 1]])


def check(expected: int, actual: int) -> int:
    """
    checks for error, returns 1 if error exists, 0 if it doesn't

    Args:
        actual (int): actual value
        expected (int): expected value

    returns: an integeer which is 1 for error and 0 if there is no error
    """
    if not np.array_equal(actual, expected):
        print(f"Actual: {actual} does not equal Expected: {expected}")
        return 1
    return 0


def test_counting_neighbour_values_of_each_cell():
    """
    This function tests and compares actual values of each matrix with their expected values in 
    non-periodic and periodic conditions. 

    returns: an integer which represents the number of errors or failed tests. 

    """

    fail = 0
    fail += check(counting_neighbour_values_of_each_cell(MATRIX_3_BY_3, 1, 2, "non_periodic"), 2)
    fail += check(counting_neighbour_values_of_each_cell(MATRIX_4_BY_4, 0, 3, "non_periodic"), 1)
    fail += check(counting_neighbour_values_of_each_cell(MATRIX_5_BY_5, 3, 3, "non_periodic"), 3)
    fail += check(counting_neighbour_values_of_each_cell(MATRIX_6_BY_6, 3, 4, "periodic"), 2)
    fail += check(counting_neighbour_values_of_each_cell(MATRIX_7_BY_7, 6, 6, "periodic"), 4)
    fail += check(counting_neighbour_values_of_each_cell(MATRIX_8_BY_8, 7, 4, "periodic"), 3)

    return fail

def test_checking_rules_of_the_game():
    """
    This function tests and compares actual values of each element of the matrix with their expected values,
    after applying each four rules of the game. 

    returns: an integer which represents the number of errors or failed tests.
    """

    fail = 0
    fail += check(checking_rules_of_the_game(0, 0), 0)
    fail += check(checking_rules_of_the_game(0, 1), 0)
    fail += check(checking_rules_of_the_game(0, 2), 0)
    fail += check(checking_rules_of_the_game(0, 3), 1)
    fail += check(checking_rules_of_the_game(0, 5), 0)
    fail += check(checking_rules_of_the_game(1, 0), 0)
    fail += check(checking_rules_of_the_game(1, 1), 0)
    fail += check(checking_rules_of_the_game(1, 2), 1)
    fail += check(checking_rules_of_the_game(1, 3), 1)
    fail += check(checking_rules_of_the_game(1, 5), 0)

    return fail



def test_generate_the_new_matrix():
    """
    This function tests and compares the updated actual matrix with the updated expected matrix by tracing over the 
    entire elements of the matrix and applying rules of the game on every individual cell/element. 

    returns: an integer which represents the number of errors or failed tests.
    """

    fail = 0
    fail += check(generate_the_new_matrix(MATRIX_3_BY_3, "non_periodic"), UPDATED_MATRIX_3_BY_3)
    fail += check(generate_the_new_matrix(MATRIX_4_BY_4, "non_periodic"), UPDATED_MATRIX_4_BY_4)
    fail += check(generate_the_new_matrix(MATRIX_5_BY_5, "non_periodic"), UPDATED_MATRIX_5_BY_5)
    fail += check(generate_the_new_matrix(MATRIX_6_BY_6, "periodic"), UPDATED_MATRIX_6_BY_6)
    fail += check(generate_the_new_matrix(MATRIX_7_BY_7, "periodic"), UPDATED_MATRIX_7_BY_7)
    fail += check(generate_the_new_matrix(MATRIX_8_BY_8, "periodic"), UPDATED_MATRIX_8_BY_8)

    return fail


def main() -> None:
    """
    The main driver of the program.
    returns: an integer which represents the number of errors or failed tests in the previous functions. 
    """
    fail = 0
    fail += test_checking_rules_of_the_game()
    fail += test_counting_neighbour_values_of_each_cell()
    fail += test_generate_the_new_matrix()

    print(f"Failed {fail} tests.")


if __name__ == "__main__":
    main()