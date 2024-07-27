import math
import itertools

# Defining city coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to find the shortest possible tour visiting exactly 7 cities
def find_shortest_tour():
    n_cities = len(cities)
    subset_size = 6  # Selecting 6 additional cities besides the depot
    min_tour = None
    min_distance = float('inf')

    for subset in itertools.combinations(range(1, n_cities), subset_size):
        # Generating all tours that start and end at depot, visiting subset cities exactly once
        for perm in itertools.permutations(subset):
            tour = (0,) + perm + (0,)
            tour_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            
            if tour_distance < min_distance:
                min_distance = tour_distance
                min_tour = tour

    return min_tour, min_distance

# Compute and display the shortest tour and its cost
shortest_tour, total_cost = find_shortest_tour()
print(f"Tour: {list(shortest_tour)}")
print(f"Total travel cost: {total_cost:.2f}")