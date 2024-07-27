import numpy as np
import math

# Environment setup
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Prepare distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean	_distance(i, j)

# Ant Colony Optimization parameters
num_ants = 10
num_iterations = 100
alpha = 1.0
beta = 2.0
evaporation_rate = 0.5
initial_pheromone = 0.1

# Initialize pheromone levels
pheromones = np.full((num_cities, num_cities), initial_pheromone)

# Choose path function
def select_next_city(current_city, visited):
    probabilities = []
    for city in range(num_cities):
        if city not in visited:
            trail = pheromones[current_city][city] ** alpha
            visibility = (1 / distance_matrix[current_city][city]) ** beta if distance_matrix[current_city][city] != 0 else 0
            probabilities.append(trail * visibility)
        else:
            probabilities.append(0)
    
    probabilities = np.array(probabilities)
    total = np.sum(probabilities)
    probabilities = probabilities / total if total > 0 else probabilities
    next_city = np.random.choice(range(num_cities), p=probabilities)
    return next_city

# Ant Colony Optimization function
def ant_colony_optimization(robot_start):
    best_tour = None
    best_cost = float('inf')
    
    for _ in range(num_iterations):
        for _ in range(num_ants):
            tour = [robot_start]
            visited = set(tour)
            current_city = robot_start
            
            while len(visited) != num_cities:
                next_city = select_next_city(current_city, visited)
                visited.add(next_city)
                tour.append(next_city)
                current_city = next_city
            
            tour.append(robot_start)  # Complete the tour
            
            # Calculate the cost of the tour
            cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
            
            # Update the best tour if current one is better
            if cost < best_cost:
                best_cost = cost
                best_tour = tour
            
            # Update pheromones
            for i in range(len(tour) - 1):
                pheromones[tour[i]][tour[i+1]] += 1 / cost
                
        # Evaporate pheromones
        pheromones *= (1 - evaporation_rate)
    
    return best_tour, best_cost

# Solve the problem for both robots
robot_0_tour, robot_0_cost = ant_colony_optimization(0)
robot_1_tour, robot_1_cost = ant_colony_optimization(1)

# Output results
print("Robot 0 Tour:", robot_0_tour)
print("Robot 0 Total Travel Cost:", robot_0_cost)
print("Robot 1 Tour:", robot_1_tour)
print("Robot 1 Total Travel Cost:", robot_1_cost)
print("Overall Total Travel Cost:", robot_0_cost + robot_1_cost)