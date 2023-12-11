# Final_5001


This repository contains code, example runs, and a report for CS5001 final project. 

•	Student Name: Yasamin Asadian 
•	Github Username: YasaminAsadian
•	Semester: Fall 2023
•	Course: CS5001 
Description
The game of life, which is often referred to as simply ‘life’, is a cellular automation devised by the mathematician John Horton Conway in 1970. It is not a game in the traditional sense, but rather a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input from human players. One can interact with the game of life by creating an initial configuration and observing how it evolves. In this project, I implemented the Game of Life in a programming environment. The core idea was to simulate how complex patterns can emerge from simple rules in a grid-based (aka. Matrix-based) universe. Each cell in this grid can be in one of the two states: alive (black) or dead (white). The state of each cell in the next generation or time step is determined by a set of rules applied to it and its eight neighbours. The reason why I was drawn into this topic was because of my background knowledge in cellular, molecular biology. It was an interesting way for me to demonstrate via coding, a concept which has been spoken about in many biological theories about how the universe and organisms initially were formed from simple rules and interactions. 
Key Features
One of the key features of this project is that we are able to demonstrate that by the application of four simple rules we are able to produce complex patterns, some of which change their shape, move, get destroyed or become stable over time. The beauty and the logic behind this design relies solely on the idea of how these four rules are being implemented in a matrix setting which its elements are ones and zeros. The matrix in a sense allows for demonstration of underpopulation, stabilization, overpopulation and reproduction which will further be explained in the methods section. Another feature of this project is the educational aspect that it provides for further understanding of laws of physics, biology, and the creation of universe as the matrix provides a dynamic system of still lives, oscillators and spaceships. Lastly, some of the features of this code can be modified such as the grid and cell colour, grid size, time interval, boundary type, etc. This flexibility can make the visualization of the animation more appealing for each individual user’s taste. However, the features that are currently implemented in the code are my favorite way to demonstrate this game/project. 
Guide
In order to run this code, you simply need to run the python file ‘run_game_of_life.py’ from the terminal. I have also provided a test.py file which tests if the code runs without any failures in any given steps. When you run the run_game_of_life.py, you should be able to see an animation that demonstrates the evolution of cells. 
Installation Instructions
There is no installation required for this code as it just shows an animation. 
Code Review
The whole concept of this code runs around the following four codes:
1.	Any live cell with fewer than two live neighbours die (underpopulation)
2.	Any live cell with two or three live neighbours lives on to the next generation.
3.	Any live cell with more than three live neighbours dies (overpopulation) 
4.	Any dead cell with exactly three live neighbours becomes a live cell (reproduction)
We start with a random matrix with random number of dead vs live cells (but the probability is already set). The function counting_neighbours start counting all the 8 surrounding neighbours according to the periodic or non-periodic boundary condition to come up with a number which represents the total live cells around each element. Once this number has been figured out the four rules of the game will be checked and evaluated via the checking_rule function. The next step is to change live cells (if necessary) according to the rules. In this step, some of the live cells (ones) may be changed to zeros (dead) or may even just stay to be one. On the other hand, some of the zeros may become ones (live) or stay to be zero according to the rules. All these small changes will be saved in another ‘updated’ matrix such that when the status of all of the cells and their neighbours are recognized we will have a completed new matrix (aka. Actual matrix) which will be shown as a real time animation using the game_of_life.py function. 





Major Challenges
One of the main challenging parts of this project was to decide what would happen when the neighbours of the marginal elements needed to be counted. In this case, since we would not be having all 8 members present, we would have needed to create numerous ‘if’ statements to consider different situations for each individual cell in the margin. Instead of doing that, we came up with giving two types of boundary types: periodic and non-periodic. In the case of a non-periodic boundary type, we have created a ‘padding’ of all zeros all around the marginal cells/elements such that those zeros will be added (as if there are no neighbours in that place initially) in the process of adding the total neighbours. For the periodic boundary condition, the easiest way to explain it is to imagine the shape of a torus, where the matrix essentially has no boundaries but rather its left and right and top and bottom margins are attached to each other. This created an endless space for the dynamic structures to move from one end of the matrix to the other in a 2D setting. It was pretty rewarding to overcome this specific challenge in this project.

Example Runs
I have documented the running of this project in a short 10s video that is called ‘animation_run.mov’. This video will start from a random matrix and then evolve into more complex structures. If you run the actual file, you will be able to see that the structures become stable at some point in time. 
Testing
I tested this project using the test.py file which is provided in the final project folder. This code provides expected matrices, values, and integers for each function and after comparing it to the actual values it returns the total number of failed tests (if any). In the test run which I completed this is the message which I received: ‘failed 0 tests.’

 
Missing Features / What's Next
In this project due to the short amount of time that we had I was only able to write code and test the four fundamental rules for square lattice which eventually led to stable structures after around 2-3 minutes. If I had more time, I could have executed the same rules and conditions for lattices with more complex shapes including honeycomb, triangles, hexagon to see if the application of rules would also create stable structures in that setting. In future, this game can as well be implemented in a 3D setting such as a torus for a better representation instead of the 2D setting.  



Final Reflection

My experience in CS5001 has been phenomenal. I started with zero experience in coding and now I am able to execute and write codes which I imagined to be impossible to learn in such a short period of time. Some of the topics which I learnt and were the most interesting to me were loops and recursion methods. We covered many topics in this course and some of which needed more practice compared to the others. As a result, I believe I should have more hands-on practice in future with typing and practicing codes to reach a level of mastery rather than just relying on watching videos on canvas or YouTube and taking notes. Thus, my takeaway from this course was that in order to be successful in the computer science major I need to dedicate most of my time in practicing exercises early on in the semester and building the muscle memory for coding. 

