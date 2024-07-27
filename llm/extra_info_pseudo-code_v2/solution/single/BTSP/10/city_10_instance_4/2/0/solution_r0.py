import math
from itertools import permutations

# Define city coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible tours starting and ending at the depot city (0)
def generate_tours():
    city_list = list(cities.keys())
    city_list.remove(0)  # remove the depot city from the list to be permuted
    all_permutations = permutations(city_list)
    tours = [[0] + list(perm) + [0] for perm in all_permutations]
    return tours

# Calculate the total cost and the bottleneck cost for a given tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = distance(tour[i], tour[i+1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Find the tour with the minimal maximum distance
def find_optimal_tour():
    best_tour = None
    best_max_distance = float('inf')
    best_total_distance = float('inf')

    for tour in generate_tours():
        total_distance, max_distance = evaluate_tour(tour)
        if max_distance < best_max_distance or (max_distance == best_max_distance and total_distance < best_total_distance):
            best_tour = tour
            best_max_distance = max_distance
            best_total_distance = total_distance

    return best_tour, best_total_distance, best_max_distance

# Find the optimal tour
optimal_tour, total_travel_cost, max_distance = find_optimal_tour()

# Output results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_travel_commuterist:.1f}")
print(f"Maximum distance between consecutive cities: {max_distance:.1f}")