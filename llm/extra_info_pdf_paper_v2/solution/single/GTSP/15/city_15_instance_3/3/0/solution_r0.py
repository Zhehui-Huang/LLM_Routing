import math
import random

# Define cities and groups.
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92),
    (54, 93), (34, 73), (6, 61), (86, 69),
    (30, 50), (35, 73), (42, 64), (64, 30),
    (70, 95), (29, 64), (32, 79)
]
groups = [[1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]]

def euclidean_distance(a, b):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

def total_distance(tour):
    """ Calculate the total Euclidean distance of the tour. """
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def simulated_annealing():
    # Start with an initial random solution
    current_solution = [0] + [random.choice(group) for group in groups] + [0]
    current_cost = total_distance(current_solution)
    
    T = 1000  # initial temperature
    cooling_rate = 0.995
    min_temperature = 1
    
    while T > min_temperature:
        # generate a neighbouring solution by modifying one city choice from one group
        i = random.randint(1, len(groups))  # select a group index (1-based, as depot is at 0)
        new_solution = current_solution[:]
        new_solution[i] = random.choice(groups[i - 1])  # pick a new city from the ith group
        
        # Calculate new cost
        new_cost = total_distance(new_solution)
        
        # Decide whether to accept the new solution
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / T):
            current_solution = new_solution
            current_cost = new_cost
            
        # Cool down
        T *= cooling_rate
    
    return current_solution, current_cost

# Run the simulated annealing algorithm to find the solution
final_tour, final_cost = simulated_annealing()

# Output the result
print(f"Tour: {final_tour}")
print(f"Total travel cost: {final_cost}")