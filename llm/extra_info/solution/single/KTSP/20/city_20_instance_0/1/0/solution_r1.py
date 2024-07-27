import itertools
import math

# City locations
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(id1, id2):
    x1, y1 = cities[id1]
    x2, y2 = cities[id2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to compute the total cost of a tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

# Store possible tours and their total costs
possible_tours = []
city_indices = list(cities.keys())[1:]  # Exclude the depot city (0) for now

# Generate all combinations of 3 non-depot cities to visit
for combination in itertools.combinations(city_indices, 3):
    current_tour = [0] + list(combination) + [0]  # Start and end at the depot city
    total_tour_cost = tour_cost(current_tour)
    possible_tours.append((current_tour, total_tour_cost))

# Find the tour with the minimum cost
min_tour, min_cost = min(possible_tours, key=lambda x: x[1])

print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost:.2f}")