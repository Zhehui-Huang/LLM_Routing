import math
from itertools import combinations, permutations

# Define the cities coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Brute force function to find the best tour including only 4 cities and starting/ending at the depot city
def find_shortest_tour():
    min_distance = float('inf')
    best_tour = None

    for combo in combinations(cities.keys() - {0}, 3):  # Generate combinations of 3 cities excluding the depot
        # Consider tours that start and end at the depot city 0
        current_combo = (0,) + combo + (0,)
        for perm in permutations(combo):
            tour = (0,) + perm + (0,)
            distance = sum(calculate_distance(tour[i], tour[i+1]) for i in range(4))
            if distance < min_distance:
                min_distance = distance
                best_tour = tour

    return best_tour, min_distance

# Solve and print the results
best_tour, min_distance = find_shortest_tour()
print(f"Tour: {list(best_tour)}")
print(f"Total travel cost: {min_distance:.2f}")