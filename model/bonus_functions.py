from model.Maze import Maze
from model.constants import *
from algorithms.valueiteration import value_iteration
from algorithms.policyiteration import policy_iteration

import matplotlib.pyplot as plt
import numpy
import random
import time

# PROBABILITY VARIABLES FOR DIFFERENT STATE TYPES - CAN ADJUST TO CHANGE COMPLEXITY
# MUST SUM TO 1
# WHITE = 0.5
# GREEN = 0.15
# BROWN = 0.15
# WALL = 0.2

def generate_maze(grid_length, p_green):
    if(p_green=="none"):
        GREEN = 0.15
        WALL = 0.2
        BROWN = 0.15
        WHITE = 0.5
    else:
        GREEN = p_green
        WALL = 0.15
        BROWN = 0.3*(1-GREEN-0.15)
        WHITE = 0.7*(1-GREEN-0.15)

    random.seed()
    maze = []

    for row in range(grid_length):
        maze.append([])

        # WE ITERATE THROUGH EACH CELL AND ADD A CELL VALUE
        for _ in range(grid_length):
            random_color = random.random()

            if random_color < WHITE:
                maze[row].append(' ')

            elif random_color < WHITE + GREEN:
                maze[row].append('G')
            elif random_color < WHITE + GREEN + BROWN:
                maze[row].append('B')
            else:
                maze[row].append('W')
    return maze

def vary_mazesize(algorithm):
    size_of_maze=[]
    run_times=[]
    iterations_to_convergence=[]

    for i in range(6,8):
        print("Please hold, the analysis is ongoing...")
        bigger_grid = generate_maze(i,"none")
        maze3a = Maze(bigger_grid, REWARD_MAP, DISCOUNT)
        start = time.time()

        if (algorithm=="valueiteration"):
            #  Run Value Iteration Algorithm
            value_iteration_res = value_iteration(maze3a)
            num_iterations = value_iteration_res['num_iterations']
        elif (algorithm=="policyiteration"):
            # Run Policy Iteration Algorithm
            policy_iteration_res = policy_iteration(maze3a, K)
            num_iterations = policy_iteration_res['num_iterations']

        end = time.time()
        size_of_maze.append(i)
        run_times.append(end-start)
        iterations_to_convergence.append(num_iterations)

    ## Visualisations
    plt.figure(figsize=(24, 12))
    plt.title("Time to Convergence against Maze Size - "+str(algorithm), size=18)
    plt.grid()
    labels = []
    plt.plot(size_of_maze, run_times)
    plt.axis([min(size_of_maze), max(size_of_maze), min(run_times), max(run_times)])

    plt.xlabel('Maze Size', fontsize=20)
    plt.ylabel('Time to Convergence (seconds)', fontsize=20)
    plt.legend(labels, loc='center left', bbox_to_anchor=(1, 0.5), prop={'size': 15})
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.show()

    plt.figure(figsize=(24, 12))
    plt.title("Number of Iterations to Convergence against Maze Size - "+str(algorithm), size=18)
    plt.grid()
    labels = []
    plt.plot(size_of_maze, iterations_to_convergence)
    plt.axis([min(size_of_maze), max(size_of_maze)+5, min(iterations_to_convergence), max(iterations_to_convergence)+5])

    plt.xlabel('Maze Size', fontsize=20)
    plt.ylabel('Number of iterations to Convergence', fontsize=20)
    plt.legend(labels, loc='center left', bbox_to_anchor=(1, 0.5), prop={'size': 15})
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.show()
    return

def vary_complexity(algorithm):
    p_green_list=[]
    run_times=[]
    num_iterations_list=[]

    for p_green in numpy.arange(0,1.1,0.1):
        print("Please hold, the analysis is ongoing...")
        bigger_grid = generate_maze(10,p_green)
        maze3a = Maze(bigger_grid, REWARD_MAP, DISCOUNT)
        start = time.time()

        if (algorithm=="valueiteration"):
            #  Run Value Iteration Algorithm
            value_iteration_res = value_iteration(maze3a)
            num_iterations = value_iteration_res['num_iterations']
        elif (algorithm=="policyiteration"):
            # Run Policy Iteration Algorithm
            policy_iteration_res = policy_iteration(maze3a, K)
            num_iterations = policy_iteration_res['num_iterations']

        end = time.time()
        p_green_list.append(p_green)
        run_times.append(end-start)
        num_iterations_list.append(num_iterations)

    ## Visualisations
    plt.figure(figsize=(24, 12))
    plt.title("Time to Convergence against Maze Complexity - "+str(algorithm), size=18)
    plt.grid()
    labels = []
    plt.plot(p_green_list, run_times)
    plt.axis([min(p_green_list), max(p_green_list), min(run_times), max(run_times)])

    plt.xlabel('Complexity of Maze (Probability of Green Square)', fontsize=20)
    plt.ylabel('Time to Convergence (seconds)', fontsize=20)
    plt.legend(labels, loc='center left', bbox_to_anchor=(1, 0.5), prop={'size': 15})
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    plt.figure(figsize=(24, 12))
    plt.title("Number of iterations to Convergence against Maze Complexity - "+str(algorithm), size=18)
    plt.grid()
    labels = []
    plt.plot(p_green_list, num_iterations_list)
    plt.axis([min(p_green_list), max(p_green_list), min(num_iterations_list), max(num_iterations_list) + 10])

    plt.xlabel('Complexity of Maze (Probability of Green Square)', fontsize=20)
    plt.ylabel('Number of iterations to Convergence', fontsize=20)
    plt.legend(labels, loc='center left', bbox_to_anchor=(1, 0.5), prop={'size': 15})
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.show()

