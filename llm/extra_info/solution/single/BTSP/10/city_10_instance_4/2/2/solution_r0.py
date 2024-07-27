import math
from itertools import permutations

# Cities coordinates
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

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Generate all possible tours starting and ending at the depot city (0)
def generate_tours():
    # All city indices except the depot
    city_indices = list(cities.keys())[1:]
    # Generate all permutations of these cities
    for perm in permutations(city_indices):
        # Add the depot at the start and end of the tour
        yield [0] + list(perm) + [0]

# Function to find the optimal tour that minimizes the maximum consecutive distance
def find_optimal_tour():
    best_tour = None
    min_max_distance = float('inf')
    total_cost_of_best_tour = 0

    for tour in generate_tours():
        # Calculate the total cost and maximum distance between consecutive cities
        total_cost = 0
        max_distance = 0
        for i in range(len(tour) - 1):
            dist = distance(tour[i], tour[i + 1])
            total_cost += dist
            if dist > max_distance:
                max_distance = dist

        # Check if this tour has a smaller maximum consecutive distance
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = tour
            total_cost_of_best_tour = total_cost

    return best_tour, total_cost_of_best_tour, min_max_distance

# Find the optimal tour
optimal_tour, total_cost, max_consecutive_distance = find_optimal_tour()

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_consecutive_ip[ istance}")