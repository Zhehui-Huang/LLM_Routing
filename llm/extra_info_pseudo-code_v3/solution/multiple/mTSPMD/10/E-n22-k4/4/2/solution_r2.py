import numpy as np
import random
from scipy.spatial import distance

# City coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Distance matrix computation
def compute_distance_matrix(cities):
    num_cities = len(cities)
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            matrix[i][j] = distance.euclidean(cities[i], cities[j])
    return matrix

distance_matrix = compute_distance_matrix(cities)

# Generating initial solutions
def generate_initial_solution(n_robots, cities):
    city_ids = list(cities.keys())
    random.shuffle(city_ids)
    depots = city_ids[:n_robots]
    cities_to_visit = city_ids[n_robots:]
    assigned_cities = np.array_split(cities_to_visit, n_robots)
    
    tours = [[] for _ in range(n_robots)]
    for i in range(n_robots):
        tours[i] = [depots[i]] + list(assigned_cities[i]) + [depots[i]]
    return tours

def calculate_total_cost(tours, distance_matrix):
    total_cost = 0
    for tour in tours:
        for i in range(len(tour)-1):
            total_cost += distance_matrix[tour[i]][tour[i+1]]
    return total_cost

# Main execution
n_robots = 4
tours = generate_initial_solution(n_robots, cities)
total_cost = calculate_total_cost(tours, distance_matrix)

# Display output
overall_cost = 0
for idx, tour in enumerate(tours):
    cost = tour_cost(tour, distance_matrix)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")
    overall_cost += cost

print(f"Overall Total Travel Cost: {overall_cost}")