import itertools
import math

# Define the cities with their coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Function to calculate Euclidean distance between two cities
def euclidean(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate combinations of cities that include the depot (city 0) and have 12 cities in total
city_indices = list(cities.keys())
combinations = [comb for comb in itertools.combinations(city_indices, 12) if 0 in comb]

# Function to find the shortest tour for a given combination of cities
def find_shortest_tour(cities_comb):
    shortest_distance = float('inf')
    shortest_path = None
    for perm in itertools.permutations(cities_comb):
        if perm[0] == 0:  # Ensure it starts with the depot
            # Calculate the route distance
            distance = sum(euclidean(perm[i], perm[i+1]) for i in range(len(perm)-1))
            # Adding the return to depot distance
            distance += euclidean(perm[-1], 0)
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_path = perm + (0,)
    return shortest_path, shortest_distance

# Evaluating all combinations to find the optimal solution
optimal_tour = None
optimal_distance = float('inf')

for comb in combinations:
    tour, distance = find_shortest_tour(comb)
    if distance < optimal_distance:
        optimal_distance = distance
        optimal_tour = tour

# Outputting the results
print("Tour:", list(optimal_tour))
print(f"Total travel cost: {optimal_distance:.2f}")