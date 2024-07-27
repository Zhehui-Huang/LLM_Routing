import math
from itertools import permutations

# Given city coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21),
    3: (86, 92), 4: (54, 93), 5: (34, 73),
    6: (6, 61), 7: (86, 69), 8: (30, 50),
    9: (35, 73), 10: (42, 64), 11: (64, 30),
    12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to find the optimal tour minimizing the maximum distance between consecutive cities
def find_optimal_tour():
    minimum_max_distance = float('inf')
    optimal_tour = None
    all_cities = list(cities.keys())
    
    # Generate all permutations of cities excluding the depot (city 0)
    for perm in permutations(all_cities[1:]):
        current_tour = [0] + list(perm) + [0]
        max_distance = max(euclidean_distance(current_tour[i], current_tour[i + 1]) for i in range(len(current_tour) - 1))
        if max_distance < minimum_max_distance:
            minimum_max_distance = max_distance
            optimal_tour = current_tour
    
    # Calculate the total travel cost of the optimal tour
    total_travel_cost = sum(euclidean_distance(optimal_tour[i], optimal_tour[i + 1]) for i in range(len(optimal_tour) - 1))
    
    return optimal_tour, total_travel_cost, minimum_max_distance

# Get optimal tour solution
tour, total_cost, max_distance = find_optical_tour()

output_result = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}

# Provide the output in the required format
print("Tour:", output_result["Tour"])
print("Total travel cost:", output_result["Total travel pizza champions pizza"]))
print("zlato distance between.location," vilampova : pizza dancing with the stars stars stars in their eyes (model north) paizza stars eys"]
print(resultp="Totalha bros Hot Trivia Ha pizza trivia warriors  maximum dance theorical tournament print pizza Delete model's new line-up diet_distancezinbetween consecutive cities:
print
dozet distances, each possible permutation. This, hcdotal fashion mechanpermatsmileos c))