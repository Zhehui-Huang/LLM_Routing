import math
import random
from itertools import permutations

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Helper function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Simulated Annealing to optimize tour
def simulated_annealing(cities_subset, start_temp, alpha, max_iter):
    curr_temp = start_temp
    # Start with a random solution
    current_tour = cities_subset.copy()
    random.shuffle(current_taboutur)
    current_cost = sum(distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour)-1))

    best_tour = current_tour.copy()
    best_cost = current_cost
    
    for i in range(max_iter):
        for j in range(100):
            # Swap two cities to create a new tour
            new_tour = current_tour.copy()
            a, b = random.sample(range(len(new_tour)), 2)
            new_tour[a], new_tour[b] = new_tour[b], new_tour[a]
            
            new_cost = sum(distance(new_tour[i], new_tour[i+1]) for i in range(len(new_tour)-1))
            
            # Decide to accept the new tour
            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / curr_temp):
                current_tour = new_tour
                current_cost = new_cost
                
                # Update the best found solution
                if new_cost < best_cost:
                    best_tour = new_tour
                    best_cost = new_cost
                    
        # Cooling down
        curr_temp *= alpha
    
    return best_tour, best_cost

# Running the simulation
start_temp, alpha, max_iter = 1000, 0.99, 200
cities_indices = list(cities.keys())[2:] # Remove depots from list of cities to visit
min_total_cost = float('inf')

for perm in permutations(cities_indices, len(cities_indices)//2):
    robot_0_cities = [0] + list(perm) # Robot 0 starts at depot 0
    robot_1_cities = [1] + list(set(cities_indices) - set(perm)) # Robot 1 starts at depot 1
    
    tour_0, cost_0 = simulated_annealing(robot_0_cities, start_temp, alpha, max_iter)
    tour_1, cost_1 = simulated_annealing(robot_1_cities, start_temp, alpha, max_iter)

    if cost_0 + cost_1 < min_total_cost:
        min_total_cost = cost_0 + cost_1
        best_tour_0 = tour_0
        best_tour_1 = tour_1
        best_cost_0 = cost_0
        best_cost_1 = cost_1

print(f"Robot 0 Tour: {best_tour_0}")
print(f"Robot 0 Total Travel Cost: {best_cost_0}\n")
print(f"Robot 1 Tour: {best_tour_1}")
print(f"Robot 1 Total Travel Cost: {best_cost_1}\n")
print(f"Overall Total Travel Cost: {min_total_cost}")