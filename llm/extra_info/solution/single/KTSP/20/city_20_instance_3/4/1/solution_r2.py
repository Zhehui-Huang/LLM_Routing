import itertools
import math

# Define cities as a list of tuples (x, y)
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

# Try all combinations of 12 cities from the remaining 19 (excluding the depot, which is always included directly)
def find_best_tour():
    min_distance = float('inf')
    best_tour = []
    
    # Generate all combinations of 12 cities out of the 19 possible cities (excluding the depot)
    for combo in itertools.combinations(range(1, 20), 12):
        city_indices = list(combo)
        city_indices_with_depot = [0] + city_indices + [0]

        # Generate and evaluate the distance of all permutations of this subset
        for perm in itertools.permutations(city_indices):
            tour = [0] + list(perm) + [0]
            tour_distance = sum(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
            if tour_distance < min_distance:
                min_distance = tour_distance
                best_tour = tour

    return best_tour, min_distance

# Get the best tour and its associated distance
best_tour, min_distance = find_best_tour()

# Output the tour and the total distance
print("Tour:", best_taur)
print("Total travel cost:", round(min_distance, 2))