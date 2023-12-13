# Final_project_CS5001


This repository contains code, example run, and a report for CS5001 final project. 


•	Student Name: Yasamin Asadian 

•	Github Username: YasaminAsadian

•	Semester: Fall 2023

•	Course: CS5001 



Description


The game of life, which is often referred to as simply ‘life’, is a cellular automation devised by the mathematician John Horton Conway in 1970. It is not a game in the traditional sense, but rather a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input from human players. One can interact with the game of life by creating an initial configuration and observing how it evolves. In this project, I implemented the Game of Life in a programming environment. The core idea was to simulate how complex patterns can emerge from simple rules in a grid-based (aka. Matrix-based) universe. Each cell in this grid can be in one of the two states: alive (black) or dead (white). The state of each cell in the next generation or time step is determined by a set of rules applied to it and its eight neighbours. The reason why I was drawn into this topic was because of my background knowledge in cellular, molecular biology. It was an interesting way for me to demonstrate via coding, a concept which has been spoken about in many biological theories regarding how the universe and organisms were initially formed as a result of simple rules and interactions. 

Key Features


One of the key features of this project is that we are able to demonstrate that by the application of four simple rules we are able to produce complex patterns, some of which change their shape, move, get destroyed or become stable over time. The beauty and the logic behind this design relies solely on the idea of the four rules being implemented in a matrix setting which its elements constitutes of only ones and zeros. The matrix in a sense allows for demonstration of underpopulation, stabilization, overpopulation and reproduction which will further be explained in the code review section. Another feature of this project is the educational aspect that it provides for further understanding of laws of physics, biology, and the creation of the universe, as the matrix demonstrates how complex patterns and behaviours can emerge from simple rules, mirroring fundamental principles observed in natural systems. This aspect of the Game of Life makes it a valuable tool for exploring concepts such as emergence, self-organization, and the simulation of life-like properties, offering insights into the interconnectedness and dynamics inherent in the physical and biological worlds. Additionally, some of the features of this code can be modified such as the grid and cell colour, matrix size, time interval, boundary type, etc. This flexibility can make the visualization of the animation more appealing for each individual user’s taste. However, the features that are currently implemented in the code are my favorite way to demonstrate this project to my target audience. Specifically, the flexibility in boundary type is another interesting key aspect of this project and is also an edge case which was resolved by defining periodic versus non-periodic conditions. This edge case has been explained and explored furthermore in the following sections of this report. 


Guide

In order to run this code, you simply need to run the python file ‘run_game_of_life.py’ from the terminal. I have also provided a test.py file which tests if the code runs without any failures in any given steps. When you run the run_game_of_life.py, you should be able to see an animation that demonstrates the evolution of cells. Please note that the main directory contains the run_game_of_life.py for running the game, a test.py file for testing the codes, a screen shot to show that all of the tests were passed (i.e. test_screen_shot.png) and two sample runs in the form of a movie/animation (i.e. animation_run.mov and animation_non_per.mov). The functions directory contains four python files which each includes a function required for running this project. 

Installation Instructions

For running this project locally, we need to first clone the repository using:

git clone [https://github.com/YasaminAsadian/Final_5001.git]

cd [Final_5001] 

Additionally, you will need to manually install required packages including: 'numpy' library for array manipulations, 'matplotlib' for animations. Finally, the main script must be executed using 

python run_game_of_life.py

Code Review

The whole concept of this code runs around the following four rules:
1.	Any live cell with fewer than two live neighbours die (underpopulation)
2.	Any live cell with two or three live neighbours lives on to the next generation.
3.	Any live cell with more than three live neighbours dies (overpopulation) 
4.	Any dead cell with exactly three live neighbours becomes a live cell (reproduction)

   
We start with a random matrix with random number of dead versus live cells (with certain live to dead cell probability). The function in the counting_neighbours.py file starts adding all the 8 surrounding neighbours' values according to the periodic or non-periodic boundary condition to come up with a number which represents the total live cells around each element. Once this number has been figured out the four rules of the game will be checked and evaluated via the function in the checking_rules.py file. In this step, we evaluate the state of live cells or dead cells (if necessary) according to the rules. Some of the live cells (ones) may be changed to zeros (dead) or may even just stay to be one (stay live). On the other hand, some of the zeros may become ones (live) or stay to be zero (dead) according to the rules. All of these small potential changes for each element of the matrix will be saved in another ‘updated’ matrix via the function in the update_matrix.py file such that when the status of all of the cells and their neighbours are recognized, we will have a completed version of a new matrix (i.e. updated matrix) which will be saved as one of the frames in a real time animation via the game_of_life.py file. This process then continues to repeat itself such that all previous matrices will be updated to a new version according to the four laws and each of these new versions of matrices will form one of the frames in the animation. Finally, when these frames are stacked together, we are looking at a full length animation that starts with showing the formation of all of the simple or complex shapes, their oscillation and/or their movements and ends with all of the structures becoming stable at some point in time. Here is a snippet breakdown of the code: 

The function for counting neighbours, as stated earlier has the task of counting the number of live cells surrounding each cell in a matrix. One challenging and interesting aspect of this code was to efficiently handle the edge cases such as the cells in the borders of the matrix. For this reason I came up with defining two boundary types periodic and non-periodic which will be dealing with this challenge (details have been explained in the major challenges section). Once this code runs it will return the number of live cells around each and every cell/element of the matrix. This number will then be passed to the next function in the checking_rules.py file. 

```
def counting_neighbour_values_of_each_cell(matrix, i, j, boundary_type):

    if boundary_type == "non_periodic":
        
        if (0 <= i-1) and (0 <= j - 1):
            count += matrix[i - 1, j - 1]
        if (0 <= i-1):
            count += matrix[i - 1, j]
        if (0 <= i-1) and (j + 1 < mat_j):
            count += matrix[i - 1, j + 1] 
        if (0 <= j-1):
            count += matrix[i , j - 1] 
        if (j + 1 < mat_j):
            count += matrix[i , j + 1]
        if (i + 1 < mat_i) and (0 <= j - 1):
            count += matrix[i + 1, j - 1]
        if (i + 1 < mat_i):
            count += matrix[i+1, j]
        if (i + 1 < mat_i) and (j + 1 < mat_j):
            count += matrix[i + 1, j + 1]

    if boundary_type == "periodic":

        a1 = i - 1
        a3 = i + 1
        b1 = j - 1
        b3 = j + 1

        if i == 0:
            a1 = mat_i - 1
        if i == mat_i - 1:
            a3 = 0
        if j == 0:
            b1 = mat_j - 1
        if j == mat_j - 1:
            b3 = 0 
            
        count  = (matrix[a1, b1] + matrix[a1, j] + matrix[a1, b3] 
                + matrix[i , b1] +                matrix[i , b3]
                + matrix[a3, b1] + matrix[a3, j] + matrix[a3, b3])
        
    if count > 8 or count < 0:
        print("Total value of the neighbours cannot be greater than 8 or smaller than zero.")

    return count
```

This second function below, takes in the neighbour count from previous function and evaluates one of the four rules according to the neighbour count to each and every cell. There is an 'if' statement for every rule, thus in total we have four 'if' statements. As a result of the application of these rules some of the live cells can become dead or stay to be alive, also some of the dead cells may remain dead or become alive. This change in the state of being live to dead is represented by a change in the numbers from one to zero or vice versa, where number '1' represents a live cell and '0' represents a dead cell. These changes will later be translated into black colour for live cell and white colour for dead cell in the animation function in the game_of_life.py file. The cells numbers will then be passed to the next function: generate_the_new_matrix in the python file update_matrix.py

```
def checking_rules_of_the_game(cell_value, neighbour_count):

    if cell_value == 1:
        if neighbour_count < 2:
            cell_value = 0

    if cell_value == 1:
        if neighbour_count == 2 or neighbour_count == 3:
            cell_value = 1

    if cell_value == 1:
        if neighbour_count > 3:
            cell_value = 0

    if cell_value == 0:
        if neighbour_count == 3:
            cell_value = 1

    return cell_value
```
The function below applies the changes dictated by the rules of the game to every individual 
cell in a matrix based on the specified boundary condition, updating the state of each and every cell. This function serves to save and apply all of the updated information received from previous function. As a result it then returns the updated matrix. The importance of this function is that it updates the whole matrix (i.e. each and every cell/element) all at the same time such that it would create the frames in our animation. This is necessary as we need to first figure out the neighbour count for each of the elements (step 1), take this information to a new function to evaluate each cell's condition based on the rules (step 2) and then update/change the whole matrix all at once (current step). In this sense there would not be any conflicts to the neighbour counts since their values (i.e. ones and zeros) do not get updated on a singular one-by-one basis, but rather this information is saved in a new matrix such that we will create a new matrix all at once, as the result of what this function returns. Since this function has for loops, it will repeat to update and generate new matrices based on the previous updated matrices. This info will then be passed to the next function: game_of_life_animation in the game_of_life.py file. 

```
def generate_the_new_matrix(matrix, boundary_type):
   
  
    mat_i, mat_j = matrix.shape
    matrix_updated = np.zeros((mat_i, mat_j))
    
    for i in range(mat_i):
        for j in range(mat_j):
            cell_value = matrix[i, j]
            neighbour_count = counting_neighbour_values_of_each_cell(matrix, i, j, boundary_type)
            cell_new_value = checking_rules_of_the_game(cell_value, neighbour_count)
            matrix_updated[i, j] = cell_new_value

    return matrix_updated
```
 This function below animates the Game of Life in real-time on a matrix of size (mat_i, mat_j).
 Its task is to stack all of the updated matrices (i.e. frames) which were returned from the previous function such that they will create a short movie/animation. It is similar to stacking series of individual picture frames to create a movie, but in this case each frame is a new matrix. Some of the components of this animation may be modified in the run_game_of_life.py file such as the cell colour, grid colour, etc., to make the representation suitable for each audience's taste or colour perception. Finally the code can run via the run_game_of_life.py file. 

```
def game_of_life_animation(mat_i, mat_j, boundary_type, cell_color, grid_color, interval, frames, live_probability):
   
    matrix = np.random.choice([0, 1], size = (mat_i, mat_j), p = [1 - live_probability, live_probability])

    fig, ax = plt.subplots()
    matrice = ax.matshow(matrix, cmap = cell_color)

    ax.set_xticks(np.arange(-0.5, mat_j, 1), minor = False)
    ax.set_yticks(np.arange(-0.5, mat_i, 1), minor = False)
    ax.tick_params(axis = 'both', which = 'major', length = 0, labelleft = False, labeltop = False)
    ax.grid(True, which = 'major', color = grid_color, linestyle = '-', linewidth = 0.2)


    def update(_):
        nonlocal matrix
        # Update the matrix based on the game's rules and boundary condition
        matrix = generate_the_new_matrix(matrix, boundary_type)
        matrice.set_array(matrix)  # Update the plot with the new matrix state
        return [matrice]

    # Create and start the animation
    animation = FuncAnimation(fig, update, frames = frames, interval = interval, blit = False)

    plt.show()
    return animation
```


Major Challenges


One of the main challenging parts of this project was to decide what would happen when the neighbours of the marginal elements (i.e. edge cases) needed to be counted. In this case, since we would not be having all 8 members present, we would have needed to create numerous ‘if’ statements to consider different situations for each individual cell in the margin. Instead of doing that, we came up with giving two types of boundary types: periodic and non-periodic. In the case of a non-periodic boundary type, we have created a ‘padding’ of all zeros all around the marginal cells/elements such that those zeros will be added (as if there are no neighbours in that place initially) in the process of adding the total neighbours. For the periodic boundary condition, the easiest way to explain it is to imagine the shape of a torus, where the matrix essentially has no boundaries but rather it wraps around itself both horizontally and vertically, allowing the edges/margins to connect seamlessly. This approach created an endless space for the dynamic structures to move from one end of the matrix to the other in a 2D setting without the need to code for a 3D matrix. Successfully overcoming this challenge, proved to be a rewarding process for me. 

Example Runs

I have documented the running of this project in a short video that is called ‘animation_run.mov’. This video is an animation generated by code which will start from a random matrix and then evolves into more complex structures in a periodic boundary condition. I have also provided a second example run that is named animation_non_per.mov in a non-periodic boundary type for a better comparison between these two conditions. In both of these cases the structures become stable at around 1 minute, however the initial state of the random matrix and the size of it, plays crucial role in the amount of time that the structures take for stabilization; thus this time may be more or less than 1 minute in various cases. 


Testing

I tested this project using the test.py file located in the main directory. This code provides expected matrices, values, and integers for each function and after comparing it to the actual values it returns the total number of failed tests (if any). In the test run which I completed this is the message which I received: ‘failed 0 tests.’ (refer to the screen shot in the main directory). 

 
Missing Features / What's Next

In this project due to the short amount of time that we had, I was only able to write code and test the four fundamental rules for square lattice which eventually led to stable structures after around 2-3 minutes. If I had more time, I could have executed the same rules and conditions for lattices with more complex shapes including honeycomb, triangles, hexagon. Exploring these different geometries could reveal how the rules could impact stability and pattern formation in diverse lattice types. Additionally, analyzing the behaviour of these rules in non-square lattices might offer insights into the adaptibility and universality of the rules themselves. Furtheremore, this game can be implemented in a 3D setting such as a torus for a better representation instead of the current 2D demonstration. This transition to a three-dimensional model could provide a more comprehensive understanding of spatial interactions and dynamics in complex systems.



Final Reflection

My journey through CS5001 has been nothing short of extraordinary. Embarking on this course with absolutely no background in coding, I found myself navigating through what initially seemed like a big challenge. However, as the weeks progressed, I was amazed at my own transformation. From a person with biology background with no coding experience, I have evolved into someone who can not only understand but also write and execute complex codes. This rapid development, mastering skills I once deemed unattainable in such a brief timeframe, has been a source of great personal pride and accomplishment. 

Among the various topics we delved into, loops and recursion methods particularly captivated my interest. These concepts, with their intricate logic and potential for solving complex problems, were both challenging and exhilarating to learn. The course covered a broad spectrum of topics, each with its own degree of difficulty and requiring varying levels of practice to master. This experience highlighted a crucial realization for me: the importance of active engagement in learning.

I learned that to truly excel in computer science, especially in a field as dynamic and demanding as coding, passive learning methods like watching instructional videos on Canvas or YouTube and taking notes are not sufficient. While these resources are valuable for theoretical understanding, they fall short in imparting the practical skills essential for proficiency in coding. Therefore, I recognized the need for a more hands-on approach learning. Regular practice, typing out codes, and actively solving problems are critical in building and refining my coding skills.

My key takeaway from CS5001 is a clear understanding of what it takes to succeed in the computer science major. It is about dedicating a significant portion of my time to practicing coding exercises, especially early in the semester. This approach is not just about understanding the syntax or the logic behind the code; it is about developing a sort of muscle memory for coding. The more I practice, the more instinctive coding becomes, allowing me to tackle increasingly complex problmes with greater confidence.

In conclusion, CS5001 has been a transformative experience that has reshaped my approach to learning computer science. It has made me to believe that with dedication, practice, and a hands-on approach I can continue to grow and excel in this field. As I move forward in my academic journey, I am excited to apply these lessons and continue developing my skills in computer science. 

