# Final_project_CS5001


This repository contains code, example runs, and a report for CS5001 final project. 


•	Student Name: Yasamin Asadian 

•	Github Username: YasaminAsadian

•	Semester: Fall 2023

•	Course: CS5001 



Description


The game of life, which is often referred to as simply ‘life’, is a cellular automation devised by the mathematician John Horton Conway in 1970. It is not a game in the traditional sense, but rather a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input from human players. One can interact with the game of life by creating an initial configuration and observing how it evolves. In this project, I implemented the Game of Life in a programming environment. The core idea was to simulate how complex patterns can emerge from simple rules in a grid-based (aka. Matrix-based) universe. Each cell in this grid can be in one of the two states: alive (black) or dead (white). The state of each cell in the next generation or time step is determined by a set of rules applied to it and its eight neighbours. The reason why I was drawn into this topic was because of my background knowledge in cellular, molecular biology. It was an interesting way for me to demonstrate via coding, a concept which has been spoken about in many biological theories about how the universe and organisms initially were formed from simple rules and interactions. 

Key Features


One of the key features of this project is that we are able to demonstrate that by the application of four simple rules we are able to produce complex patterns, some of which change their shape, move, get destroyed or become stable over time. The beauty and the logic behind this design relies solely on the idea of how these four rules are being implemented in a matrix setting which its elements are ones and zeros. The matrix in a sense allows for demonstration of underpopulation, stabilization, overpopulation and reproduction which will further be explained in the methods section. Another feature of this project is the educational aspect that it provides for further understanding of laws of physics, biology, and the creation of universe as the matrix provides a dynamic system of still lives, oscillators and spaceships. Lastly, some of the features of this code can be modified such as the grid and cell colour, matrix size, time interval, boundary type, etc. This flexibility can make the visualization of the animation more appealing for each individual user’s taste. However, the features that are currently implemented in the code are my favorite way to demonstrate this game/project. 


Guide

In order to run this code, you simply need to run the python file ‘run_game_of_life.py’ from the terminal. I have also provided a test.py file which tests if the code runs without any failures in any given steps. When you run the run_game_of_life.py, you should be able to see an animation that demonstrates the evolution of cells. Please note that the main directory contains the run_game_of_life.py for running the game, a test.py file for testing the codes and a sample run in the form of a movie animation. The functions directory contains four python files which each includes a function required for running this project. 

Installation Instructions

There is no installation required for this code as it shows an animation as the end result. 

Code Review

The whole concept of this code runs around the following four rules:
1.	Any live cell with fewer than two live neighbours die (underpopulation)
2.	Any live cell with two or three live neighbours lives on to the next generation.
3.	Any live cell with more than three live neighbours dies (overpopulation) 
4.	Any dead cell with exactly three live neighbours becomes a live cell (reproduction)

   
We start with a random matrix with random number of dead vs live cells (with certain live to dead cell probability). The function counting_neighbours start counting all the 8 surrounding neighbours according to the periodic or non-periodic boundary condition to come up with a number which represents the total live cells around each element. Once this number has been figured out the four rules of the game will be checked and evaluated via the checking_rule function. The next step is to change live cells (if necessary) according to the rules. In this step, some of the live cells (ones) may be changed to zeros (dead) or may even just stay to be one. On the other hand, some of the zeros may become ones (live) or stay to be zero according to the rules. All these small changes will be saved in another ‘updated’ matrix via updated_matrix.py such that when the status of all of the cells and their neighbours are recognized we will have a completed new matrix (aka. Actual matrix) which will be shown as a real time animation using the game_of_life.py function. 


Major Challenges


One of the main challenging parts of this project was to decide what would happen when the neighbours of the marginal elements needed to be counted. In this case, since we would not be having all 8 members present, we would have needed to create numerous ‘if’ statements to consider different situations for each individual cell in the margin. Instead of doing that, we came up with giving two types of boundary types: periodic and non-periodic. In the case of a non-periodic boundary type, we have created a ‘padding’ of all zeros all around the marginal cells/elements such that those zeros will be added (as if there are no neighbours in that place initially) in the process of adding the total neighbours. For the periodic boundary condition, the easiest way to explain it is to imagine the shape of a torus, where the matrix essentially has no boundaries but rather it wraps around itself both horizontally and vertically, allowing the edges/margins to connect seamlessly. This approach created an endless space for the dynamic structures to move from one end of the matrix to the other in a 2D setting without the need to code for a 3D structure. Successfully overcoming this challenge proved to be a rewarding process for me. 

Example Runs

I have documented the running of this project in a short 10 seconds video that is called ‘animation_run.mov’. This video is an animation generated by code which will start from a random matrix and then evolve into more complex structures. By running the run_game_of_life.py file, you will be able to see that the structures become stable at some point in time (at around 2 to 3 minutes, depending on the initial state of the random matrix). 


Testing

I tested this project using the test.py file located in the main repository. This code provides expected matrices, values, and integers for each function and after comparing it to the actual values it returns the total number of failed tests (if any). In the test run which I completed this is the message which I received: ‘failed 0 tests.’

 
Missing Features / What's Next

In this project due to the short amount of time that we had I was only able to write code and test the four fundamental rules for square lattice which eventually led to stable structures after around 2-3 minutes. If I had more time, I could have executed the same rules and conditions for lattices with more complex shapes including honeycomb, triangles, hexagon. Exploring these different geometries could reveal how the rules could impact stability and pattern formation in diverse lattice types. Additionally, analyzing the behaviour of these rules in non-square lattices might offer insights into the adaptibility and universality of the rules themselves. Furtheremore, this game can be implemented in a 3D setting such as a torus for a better representation instead of the current 2D demonstration. This transition to a three-dimensional model could provide a more comprehensive understanding of spatial interactions and dynamics in complex systems. 



Final Reflection

My journey through CS5001 has been nothing short of extraordinary. Embarking on this course with absolutely no background in coding, I found myself navigating through what initially seemed like a big challenge. However, as the weeks progressed, I was amazed at my own transformation. From a person with biology background with no coding experience, I have evolved into someone who can not only understand but also write and execute complex codes. This rapid development, mastering skills I once deemed unattainable in such a brief timeframe, has been a source of great personal pride and accomplishment. 

Among the various topics we delved into, loops and recursion methods particularly captivated my interest. These concepts, with their intricate logic and potential for solving complex problems, were both challenging and exhilarating to learn. The course covered a broad spectrum of topics, each with its own degree of difficulty and requiring varying levels of practice to master. This experience highlighted a crucial realization for me: the importance of active engagement in learning.

I learned that to truly excel in computer science, especially in a field as dynamic and demanding as coding, passive learning methods like watching instructional videos on Canvas or YouTube and taking notes are not sufficient. While these resources are valuable for theoretical understanding, they fall short in imparting the practical skills essential for proficiency in coding. Therefore, I recognized the need for a more hands-on approach learning. Regular practice, typing out codes, and actively solving problems are critical in building and refining my coding skills.

My key takeaway from CS5001 is a clear understanding of what it takes to succeed in the computer science major. It is about dedicating a significant portion of my time to practicing coding exercises, especially early in the semester. This approach is not just about understanding the syntax or the logic behind the code; it is about developing a sort of muscle memory for coding. The more I practice, the more instinctive coding becomes, allowing me to tackle increasingly complex problmes with greater confidence.

In conclusion, CS5001 has been a transformative experience that has reshaped my approach to learning computer science. It has made me to believe that with dedication, practice, and a hands-on approach I can continue to grow and excel in this field. As I move forward in my academic journey, I am excited to apply these lessons and continue developing my skills in computer science. 

