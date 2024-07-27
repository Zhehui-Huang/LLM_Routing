import numpy as np
from scipy.spatial import distance
import random

# City coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
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
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

# Calculate distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = distance.euclidean(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')

# Variables
num_robots = 8

# Competition-based Initialization
def initialize_tours():
    sorted_cities = sorted(range(1, num_cities), key=lambda x: distance_matrix[0][x])
    tours = [[] for _ in range(num_robots)]
    for i in range(num_robots):
        tours[i].append(sorted_cities[i])
    
    for city in sorted_cities[num_robots:]:
        best_robot = min(range(num_robots), key=lambda r: distance_matrix[tours[r][-1]][city])
        tours[best_robot].append(city)
    
    for tour in tours:
        tour.insert(0, 0)  # Start from depot
        tour.append(0)     # Return to depot
    return tours

# Calculate tour cost
def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Main GVNS algorithm implementation and execution
def gvns(tmax):
    # Initial solution
    tours = initialize_tours()
    best_tours = tours
    best_max_cost = max(calculate_tour_cost(tour) for tour in tours)

    start_time = time.time()
    while (time.time() - start_time) < tmax:
        # Shaking: randomly modify the tours
        for _ in range(random.randint(1, num_cities // 10)):  # Random magnitude of shaking
            robot_a, robot_b = random.sample(range(num_robots), 2)
            if tours[robot_a] and len(tours[robot_a]) > 2:
                city_index = random.randint(1, len(tours[robot_a]) - 2)
                city = tours[robot_a].pop(city_index)
                tours[robot_b].insert(random.randint(1, len(tours[robot_b]) - 1), city)
        
        # Local search (simulated as simple improvement)
        for tour in tours:
            improved = True
            while improved:
                improved = False
                best_cost = calculate_tour_cost(tour)
                for i in range(1, len(tour) - 2):
                    for j in range(i + 1, len(tour) - 1):
                        if i != j:
                            new_tour = tour[:]
                            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Simple 2-opt swap
                            new_cost = calculate_tour_cost(new_tour)
                            if new_cost < best_cost:
                                tour[:] = new_tour
                                best_cost = new_cost
                                improved = True
        
        # Update best solution
        current_max_cost = max(calculate_tour_cost(tour) for tour in tours)
        if current_max_cost < best_max_cost:
            best_tours = [list(tour) for tour in tours]
            best_max_cost = current_max_cost
    
    return best_tours

# Execute the GVNS algorithm
import time
result_tours = gvns(60)  # 60 seconds time limit
max_cost = max(calculate_tour_cost(tour) for tour in result_tours)

# Print results
for idx, tour in enumerate(result_tours):
    tour_cost = calculate_tour_cost(tour)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")

print(f"Maximum Travel Cost: {max_cost:.2f}")