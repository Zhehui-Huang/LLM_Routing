import math
from itertools import permutations

# Define the cities' coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all possible tours
def generate_tours():
    all_cities = list(cities.keys())[1:]  # Exclude the depot city from permutations
    for perm in permutations(all_cities):
        yield [0] + list(perm) + [0]

# Calculate the total cost of the tour
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Find the shortest tour
def find_shortest_tour():
    minimum_cost = float('inf')
    best_tour = None
    for tour in generate_tours():
        cost = calculate_tour_cost(tour)
        if cost < minimum_cost:
            minimum_cost = cost
            best_tour = tour
    return best_tour, minimum_cost

# Execute and get the shortest path
short-options:
    best_tour, tour_cost = find_shortest_tour()

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {tour_cost}")