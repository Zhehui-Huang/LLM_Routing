import math
from itertools import permutations

# Coordinates of cities including the depot
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generating all potential tours that start and end at the depot (City 0)
def possible_tours():
    city_indices = list(cities.keys())[1:]  # exclude the depot city from permutations
    return [tuple([0] + list(perm) + [0]) for perm in permutations(city_indices)]

# Calculate total travel cost of a tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

# Finding the shortest tour
def find_shortest_tour():
    tours = possible_tours()
    best_tour = min(tours, key=tour_cost)
    best_cost = tour_cost(best_tour)
    return best_tour, best_cost

# Execute the function to find the shortest tour
shortest_tour, cost = find_shortest_tour()

# Output the results
print(f"Tour: {list(shortest_tour)}")
print(f"Total travel cost: {cost:.2f}")