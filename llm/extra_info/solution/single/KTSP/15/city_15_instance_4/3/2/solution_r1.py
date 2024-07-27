import itertools
from math import sqrt

# Function to calculate the Euclidean distance between two city coordinates
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# List of city coordinates where the first tuple is the starting depot (city 0)
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Function to compute the total path distance of a given tour
def tour_distance(tour):
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    total_distance += euclidean_distance(cities[tour[-1]], cities[tour[0]])  # return to the depot
    return total_distance

# Get all combinations to select 11 cities out of the 14 (the 15th is the depot)
city_indices = list(range(1, 15))  # City indices excluding the depot
combos = itertools.combinations(city_indices, 11)

# Search for the shortest tour possible
min_distance = float('inf')
best_tour = None

for combo in combos:
    full_route = [0] + list(combo) + [0]  # Start and end at the depot
    all_tours = itertools.permutations(full_route[1:-1])  # Permute only the inner cities

    for tour in all_tours:
        current_tour = [0] + list(tour) + [0]
        current_distance = tour_distance(current_tour)
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = current_tour

# Output the best tour and the associated minimum distance
print("Tour:", best_tour)
print("Total travel cost:", round(min_distance, 2))