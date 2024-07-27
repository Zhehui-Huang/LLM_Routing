import numpy as np

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))

def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Ant Colony Optimization parameters
num_ants = 20
num_iterations = 100
evaporation_rate = 0.5
alpha = 1  # Pheromone importance
beta = 2   # Distance importance
pheromone = np.ones((num_cities, num_cities)) * 0.1

def select_next_city(current_city, visited):
    probabilities = []
    city_list = list(set(range(num_cities)) - set(visited))
    for city in city_list:
        pheromone_factor = pheromone[current_city][city] ** alpha
        heuristic_factor = (1 / distance_matrix[current_city][city]) ** beta
        probabilities.append(pheromone_factor * heuristic_factor)
    
    probabilities = probabilities / np.sum(probabilities)
    next_city = np.random.choice(city_list, p=probabilities)
    return next_city

def compute_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# ACO algorithm
best_cost = np.inf
for iteration in range(num_iterations):
    all_tours = []
    for ant in range(num_ants):
        tour = [np.random.choice([0, 1])]  # starting from a depot
        visited = set(tour)
        
        while len(visited) < num_cities:
            next_city = select_next_city(tour[-1], visited)
            tour.append(next_city)
            visited.add(next_city)
        
        tour.append(tour[0])  # complete the tour by returning to the depot
        
        tour_cost = compute_tour_cost(tour)
        all_tours.append((tour, tour_cost))
        
        if tour_cost < best_cost:
            best_cost = tour_cost
            best_tour = tour
    
    # Update pheromones
    pheromone *= (1 - evaporation_rate)
    for tour, cost in all_tours:
        for i in range(len(tour)-1):
            pheromone[tour[i]][tour[i+1]] += 1 / cost

# Calculate costs for each robot
robot_0_path = [i for i in best_tour if best_tour.index(i) % 2 == 0]
robot_1_path = [i for i in best_tour if best_tour.index(i) % 2 != 0]
robot_0_cost = compute_tour_cost(robot_0_path + [robot_0_path[0]])
robot_1_cost = compute_tour_cost(robot_1_path + [robot_1_path[0]])

# Display results
print("Robot 0 Tour:", robot_0_path + [robot_0_path[0]])
print("Robot 0 Total Travel Cost:", robot_0_cost)
print("Robot 1 Tour:", robot_1_path + [robot_1_path[0]])
print("Robot 1 Total Travel Cost:", robot_1_cost)
print("Overall Total Travel Cost:", robot_0_cost + robot_1_cost)