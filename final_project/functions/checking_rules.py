
def checking_rules_of_the_game(cell_value, neighbour_count):

    """
    This function evaluates the rules of the game for each cell, based on the classic rules of Conway's Game of Life:
        1. Any live cell with fewer than two live neighbours dies, due to underpopulation.
        2. Any live cell with two or three live neighbours survives to the next generation.
        3. Any live cell with more than three live neighbours dies, due to overpopulation.
        4. Any dead cell with exactly three live neighbours becomes a live cell, simulating reproduction.

    Arguments:
        cell_value: The current value of the cell, either 0 (dead) or 1 (alive).
        neighbour_count: The number of live cells surrounding the main cell, ranging from 0 to 8.

    Returns:
        The new value of the cell, either 0 (dead) or 1 (alive), based on the game rules.
    """

    if cell_value==1:
        if neighbour_count<2:
            cell_value = 0

    if cell_value==1:
        if neighbour_count==2 or neighbour_count==3:
            cell_value = 1

    if cell_value==1:
        if neighbour_count>3:
            cell_value = 0

    if cell_value==0:
        if neighbour_count==3:
            cell_value = 1

    return cell_value
