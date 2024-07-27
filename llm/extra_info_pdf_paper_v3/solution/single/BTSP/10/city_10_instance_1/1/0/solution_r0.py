import math
from itertools import permutations

# Coordinates of the cities (index corresponds to city number)
coordinates = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), 
               (70, 14), (97, 44), (17, 69), (95, 89)]

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_distances():
    """Calculate distances between all pairs of cities."""
    num_cities = len(coordinates)
    distances = [[0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i][j] = euclidean_distance(coordinates[i], coordinates[j])
    return distances

def find_min_max_tour(distances):
    """Find the tour that minimizes the maximum distance between consecutive cities."""
    num_cities = len(distances)
    min_max_distance = float('inf')
    best_tour = None

    for perm in permutations(range(1, num_cities)):  # Skip the depot (0) for permutations
        # Add depot at the start and end of the tour
        tour = [0] + list(perm) + [0]
        
        # Calculate the maximum distance in this tour configuration
        max_dist = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        
        if max_dist < min_max_distance:
            min_max_distance = max_dist
            best_tour = tour

    return best_tour, min_max_distance

# Utilization
distances = calculate_distances()
tour, max_distance = find_min_max_tour(distances)

# Calculate the total travel cost
total_travel_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Outputs
tour_str = "Tour: {}".format(tour)
total_cost_str = "Total travel cost: {:.2f}".format(total_travel_cost)
max_distance_str = "Maximum distance between consecutive cities: {:.2f}".format(max_distance)

result = "{}\n{}\n{}".format(tour_str, total_cost_str, max_distance_str)
print(result)