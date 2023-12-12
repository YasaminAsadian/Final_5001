from functions.game_of_life import game_of_life_animation

if __name__ == '__main__':

    #Number of rows in the matrix (int)
    mat_i = 60
    #Number of columns in the matrix (int)
    mat_j = 100
    #Time interval between frames in milliseconds (int)
    interval = 100
    #Number of frames to animate (int)
    frames = 1000
    #Probability of a cell being alive at initialization (float)
    live_probability = 0.12
    #Color map for the cells (str) (Retrieved from https://matplotlib.org/stable/users/explain/colors/colormaps.html)
    cell_colour = "binary"
    #Color of the grid lines (str)
    grid_color = "gray"
    #Type of boundary condition ('periodic' or 'non-periodic') (str)
    boundary_type = "periodic"

    #calling the game of life animation from game_of_life.py to demonstrate the game graphically 
    game_of_life_animation(mat_i,
                            mat_j,
                            boundary_type, 
                            cell_colour, 
                            grid_color, 
                            interval,
                            frames, 
                            live_probability)
