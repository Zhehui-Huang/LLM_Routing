import numpy as np
from scipy.spatial.distance import euclidean
import random

# City coordinates
coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Calculate distances matrix
num_cities = len(coords)
dist_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            dist_matrix[i, j] = euclidean(coords[i], coords[j])

# Initialize random tour assignment to robots
num_robots = 4
assignments = [[] for _ in range(num_robots)]
assigned_cities = set()
depots = [0, 1, 2, 3]

for city in range(num_cities):
    if city not in depots:
        robot = random.randint(0, num_robots - 1)
        assignments[robot].append(city)
        assigned_cities.add(city)

# Ensure all cities are covered
for city in range(num_cities):
    if city not in assigned_cities and city not in depots:
        assignments[random.randint(0, num_robots - 1)].append(city)

# Simulated Annealing function
def simulated_annealing(tour, temp):
    min_tour = tour[:]
    min_cost = calculate_cost(min_tour)
    current_temp = temp
    
    while current_temp > 1:
        # Create neighbouring solution
        new_tour = tour[:]
        i, j = random.sample(range(1, len(new_tour)), 2)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        new_cost = calculate_cost(new_tour)
        
        # Acceptance probability
        if new_cost < min_cost or random.random() < np.exp((min_cost - new_cost) / current_temp):
            min_tour = new_tour[:]
            min_cost = new_cost
            
        current_temp *= 0.995
    
    return min_tour, min_cost

def calculate_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += dist_matrix[tour[i-1], tour[i]]
    return cost

def calculate_total_cost(assignments):
    total_cost = 0
    for i in range(num_robots):
        assignments[i] = [depots[i]] + assignments[i]
        tour, cost = simulated_annealing(assignments[i], 1000)
        assignments[i] = tour
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost}")
        total_cost += cost
        
    print("Overall Total Travel Cost:", total_cost)

calculate_total_cost(assignments)