import math
import random
from scipy.spatial import distance_matrix

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Create distance matrix
coords = list(cities.values())
dist_matrix = distance_matrix(coords, coords)

def euclidean_dist(a, b):
    return dist_matrix[a, b]

# Simulated Annealing Algorithm
def simulated_annealing(cities_list):
    current_solution = cities_list[:]
    current_cost = calculate_total_cost(current_solution)
    best_solution = current_solution[:]
    best_cost = current_cost
    
    T = 100.0
    cooling_rate = 0.995
    T_min = 1.0
    
    while T > T_min:
        i = random.randint(1, len(current_solution) - 2)
        j = random.randint(1, len(current_solution) - 2)
        if i != j:
            new_solution = current_tour(current_solution, i, j)
            new_cost = calculate_total_cost(new_solution)
            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / T):
                current_solution = new_solution
                current_cost = new_cost
                if new_cost < best_cost:
                    best_solution = current_solution[:]
                    best_cost = new_step_cost
        
        T *= cooling_rate
    return best_solution

def calculate_total_cost(tour):
    return sum(euclidean_dist(tour[i], tour[i+1]) for i in range(len(tour)-1))

def current_tour(tour, i, j):
    new_tour = tour[:]
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour

# Setup tours by distributing cities among the eight robots starting from the depot 0
num_robots = 8
robot_tours = []
size_per_robot = len(cities) // num_robots
remaining_cities = list(cities.keys())[1:]  # excluding depot 0

for r in range(num_robots):
    start_size = r * size_per_robot
    if r == num_robots - 1:  # Take the remaining cities for last robot
        cities_slice = remaining_cities[start_size:]
    else:
        cities_slice = remaining_cities[start_size:start_size + size_per_robot]
    cities_slice = [0] + cities_slice  # Start at depot 0
    robot_tours.append(cities_slice)

# Solve each tour using Simulated Annealing
optimized_tours = []
total_cost = 0

for tour in robot_tours:
    optimized_tour = simulated_annealing(tour)
    tour_cost = calculate_total_cost(optimized_tour)
    optimized_tours.append((optimized_tour, tour_cost))
    total_cost += tour_cost

# Print the results
for idx, (tour, cost) in enumerate(optimized_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")