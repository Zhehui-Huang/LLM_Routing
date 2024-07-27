import itertools
import math

# Define coordinates for each city
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

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 +
                     (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all combinations of 5 additional cities to visit alongside the depot city
city_indices = list(cities.keys())
city_indices.remove(0)
city_combinations = itertools.combinations(city_indices, 5)

# Function to find the shortest tour
def find_shortest_tour():
    min_cost = float('inf')
    best_tour = []

    for combo in city_combinations:
        # Permute the selected combination to consider all possible tours
        for perm in itertools.permutations(combo):
            tour = [0] + list(perm) + [0]
            # Calculate the tour cost
            tour_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

            # Check if this is the minimum cost found
            if tour_cost < min_cost:
                min_cost = tour_cost
                best_tour = tour

    return best_tour, min_cost

# Find the optimal tour and its cost
optimal_tour, optimal_cost = find_shortest_tour()

print("Tour:", optimal_tour)
print("Total travel cost:", round(optimal_cost, 2))