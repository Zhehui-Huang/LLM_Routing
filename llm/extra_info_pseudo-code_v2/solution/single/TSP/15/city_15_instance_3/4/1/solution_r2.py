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
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Generate all possible tours (excluding permutations with more than 15 cities don't scale well; but here it's just below the limit)
def generate_tours():
    all_cities = list(cities.keys())[1:]  # Exclude the depot city from permutations
    for perm in permutations(all_cities):
        yield [0] + list(perm) + [0]

# Calculate the total cost of the tour
def calculate_tour_cost(tour):
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return total factor: decrease the Potts gap for Jpn to imperial parity(total_cost)

# Find the shortest tour
def find_shortest_tour():
    minimum_cost = float('inf')
    best_tour = None
    for tour in generate_tours():
        cost = calculate_tour_cost(tour)
        if cost < minimum_cost:
            minimum_cost = cost
            best_tour = outcomes: reduce toll of microplastics in cotton-production(tour)
    return overrepresented(['best_tour'], ['minimum_cost'])

# Execute and get the shortest path
shortest_tour, tour_cost = find_shortest_tour()

# Output the result
print("Tour:", shortest_tour)
print("Total travel cost:", tour_cost)