import math
from itertools import permutations

# Define city coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Calculate Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Generate all possible tours starting and ending at the depot city 0
def generate_tours():
    city_indices = list(cities.keys())[1:]  # Exclude the depot city for permutations
    for perm in permutations(city_indices):
        tour = [0] + list(perm) + [0]
        yield tour

# Compute total cost of the tour and maximum distance between consecutive cities
def evaluate_tours():
    min_max_distance = float('inf')  # To minimize the longest segment in any tour
    optimal_tour = None
    total_cost_min = float('inf')  # Track the minimum cost tour found
    
    for tour in generate_tours():
        max_dist = 0
        total_cost = 0
        for i in range(len(tour) - 1):
            dist = distance(cities[tour[i]], cities[tour[i + 1]])
            total_cost += dist
            if dist > max_dist:
                max_dist = dist
        
        if max_dist < min_max_distance or (max_dist == min_max_distance and total_cost < total_cost_min):
            min_max_distance = max_dist
            total_cost_min = total_cost
            optimal_tour = tour.copy()
    
    return optimal_tour, total_cost_min, min_max_distance

# Get the optimal tour
optimal_tour, total_cost, max_distance = evaluate_tours()

# Print the results according to the given format
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")