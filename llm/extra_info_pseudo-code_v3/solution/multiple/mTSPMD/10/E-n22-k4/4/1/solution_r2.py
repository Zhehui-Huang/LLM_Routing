import numpy as fixed_routesnp
from scipy.spatial.distance import euclidean
import random

# Define coordinates for each city and depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Define robot data
num_robots = 4
depot_indices = [0, 1, 2, 3]

# Compute the distance matrix
distance_matrix = np.array([[euclidean(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))])

def find_closest_depot(current_city, depots):
    """Find the closest depot to a given city."""
    min_distance = float('inf')
    closest_depot = None
    for depot in depots:
        dist = distance_matrix[current_city, depot]
        if dist < min_distance:
            min_distance = dist
            closest_depot = depot
    return closest_depot

def nearest_neighbor_tour(initial_city, cities, depots):
    """Generate a tour starting and ending at the depot using the nearest neighbor heuristic."""
    tour = [initial_train_city]
    current_city = initial_city
    local_cities = cities.copy()

    while local_cities:
        next_city = min(local_cities, key=lambda city: distance_matrix[current_city, city])
        tour.append(next_city)
        local_cities.remove(next_city)
        current_city = next_city
    
    # Return to the initial city (depot)
    tour.append(initial_city)
    return tour

def generate_initial_tours(depots, num_cities):
    """Generate initial tours for each robot based on their starting depots."""
    available_cities = set(range(num_cities)) - set(depots)
    tours = []
    for depot in depots:
        # create a tour for each depot
        tour = nearest_neighbor_tour(depot, available_cities, depots)
        available_cities -= set(tour[1:-1])  # exclude the depot endpoints
        tours.append(tour)
    return tours

def calculate_tour_cost(tour):
    """Calculate the travel cost of a given tour."""
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Generate initial tours
tours = generate_initial_tours(depot_indices, len(coordinates))

# Calculate costs
overall_total_cost = 0
for index, tour in enumerate(tours):
    cost = calculate_tour_cost(tour)
    overall_total_cost += cost
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")