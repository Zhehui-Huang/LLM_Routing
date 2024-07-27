import math
import random

# Coordinates of each city including depots
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculating euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Simulated Annealing to optimize the tour
def simulated_annealing(sol):
    T = 10000
    T_min = 1
    alpha = 0.99

    current_solution = sol[:]
    current_cost = calculate_total_cost(current_solution)
    
    while T > T_min:
        i = 1
        while i < len(sol) - 1:
            new_solution = current_solution[:]
            l = random.randint(1, len(new_solution) - 2)
            r = random.randint(l + 1, len(new_solution) - 1)
            new_solution[l:r+1] = reversed(new_solution[l:r+1])
            new_cost = calculate_total_cost(new_solution)
            if new_cost < current_cost or random.uniform(0, 1) < math.exp((current_cost - new_cost) / T):
                current_solution, current_cost = new_solution, new_cost
            i += 1
        T *= alpha
    
    return current_solution, current_cost

# Calculate total cost of the entire tour
def calculate_total_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return total_cost

# Perform initial shuffling and split into sub-tours
initial_tour = list(range(1, len(cities)))  # excluding the depot at index 0
random.shuffle(initial_tour)
mid_index = len(initial_tour) // 2
tour_1 = [0] + initial_tour[:mid_index]  # Robot 1 starts from depot at index 0
tour_2 = [0] + initial_tour[mid_index:]  # Robot 2 also starts from depot at index 0

# Optimize each tour using Simulated Annealing
optimized_tour_1, cost_1 = simulated_annealing(tour_1)
optimized_tour_2, cost_2 = simulated_annealing(tour_2)
total_cost = cost_1 + cost_2

# Output the results
print("Robot 0 Tour:", optimized_tour_1)
print("Robot 0 Total Travel Cost:", cost_1)
print("\nRobot 1 Tour:", optimized_tour_2)
print("Robot 1 Total Travel Cost:", cost_2)
print("\nOverall Total Travel Cost:", total_cost)