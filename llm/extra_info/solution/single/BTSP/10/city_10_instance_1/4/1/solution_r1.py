import math
from itertools import permutations

# Define the cities using their coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate all possible tours starting and ending at the depot city (0)
def generate_tours():
    all_cities_except_depot = list(cities.keys())[1:]  # All cities except the depot
    all_possible_tours = permutations(all_cities_except_depot)
    return [(0,) + tour + (0,) for tour in all_possible_tours]
    
# Evaluate a given tour for its total cost and maximum leg distance
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    return total_cost, max_distance

# Find the optimal tour minimizing the maximum leg distance
def find_optimal_tour():
    optimal_tour = None
    minimum_max_distance = float('inf')
    minimum_total_cost = float('inf')
    all_tours = generate_tours()
    
    for tour in all_tours:
        total_cost, max_distance = evaluate_tour(tour)
        if (max_distance < minimum_max_distance) or (max_distance == minimum_max_distance and total_cost < minimum_total_cost):
            minimum_max_distance = max_distance
            minimum_total_cost = total_cost
            optimal_tour = tour
    
    return optimal_tour, minimum_total_cost, minimum_max_distance

# Run function to find optimal tour
tour, total_cost, max_distance = find_optimal_tour()

# Print the results
print("Tour:", list(tour))
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))