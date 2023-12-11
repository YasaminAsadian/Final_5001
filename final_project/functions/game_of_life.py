import numpy as np
import matplotlib.pyplot as plt  
from matplotlib.animation import FuncAnimation

from functions.update_matrix import generate_the_new_matrix


def game_of_life_animation(mat_i, mat_j, boundary_type, cell_color, grid_color, interval, frames, live_probability):
    """
    Animates the Game of Life in real-time on a matrix of size (mat_i, mat_j).

    Args:
        mat_i (int): Number of rows in the matrix.
        mat_j (int): Number of columns in the matrix.
        boundary_type (str): Type of boundary condition ('periodic' or 'non-periodic').
        cell_color (str): Color map for the cells.
        grid_color (str): Color of the grid lines.
        interval (int): Time interval between frames in milliseconds.
        frames (int): Number of frames to animate.
        live_probability (float): Probability of a cell being alive at initialization.

    Returns:
        matplotlib.animation.FuncAnimation: The animation object for the game.
    """

    # Initialize the matrix with a random state based on the live_probability
    matrix = np.random.choice([0, 1], size=(mat_i, mat_j), p=[1-live_probability, live_probability])

    # Set up the plot
    fig, ax = plt.subplots()
    matrice = ax.matshow(matrix, cmap=cell_color)

    # Generate the grid for better visualization
    ax.set_xticks(np.arange(-0.5, mat_j, 1), minor=False)
    ax.set_yticks(np.arange(-0.5, mat_i, 1), minor=False)
    ax.tick_params(axis='both', which='major', length=0, labelleft=False, labeltop=False)
    ax.grid(True, which='major', color=grid_color, linestyle='-', linewidth=0.2)

    def update(_):
        """
        Updates the state of the matrix for each frame of the animation.

        Args:
            _ : A dummy parameter, often used by animation frameworks.

        Returns:
            A list containing the matplotlib object to be updated for the animation.
        """
        nonlocal matrix
        # Update the matrix based on the game's rules and boundary condition
        matrix = generate_the_new_matrix(matrix, boundary_type)
        matrice.set_array(matrix)  # Update the plot with the new matrix state
        return [matrice]

    # Create and start the animation
    animation = FuncAnimation(fig, update, frames=frames, interval=interval, blit=False)

    plt.show()
    return animation