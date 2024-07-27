import math
from itertools import permutations

# Coordinates corresponding to each city index
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Creating distance matrix
distance_matrix = [
    [0 if i == j else euclidean_distance(cities[i], cities[j]) for j in range(len(cities))]
    for i in range(len(cities))
]

def find_best_bottleneck_tour(cities):
    best_distance = float('inf')
    best_tour = None
    city_indices = list(cities.keys())
    
    # Exploring all permutations of city visits 
    for perm in permutations(city_indices[1:]):  # permute only cities 1 to 14, start/end at city 0
        tour = (0,) + perm + (0,)  # start and end at the depot city 0
        max_leg_distance = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        if max_leg_distance < best_distance:
            best_distance = max_leg_distance
            best_tour = tour

    # Calculating the total travel cost of the best tour
    total_cost = sum(distance_iso_matrix[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))
    return best_tour, total_cost, best_distance

# Execute the function
tour, total_cost, max_dist = find_best_bottleneck_tour(cities)

# Output the results
print(f"Tour: {list(tour)}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist:.2f}")