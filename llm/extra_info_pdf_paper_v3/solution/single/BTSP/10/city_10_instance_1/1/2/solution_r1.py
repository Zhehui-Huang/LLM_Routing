import math
import itertools

# City coordinates
coords = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def euclidean_distance(city1, city2):
    return math.sqrt((coords[city1][0] - coords[city2][0]) ** 2 + (coords[city1][1] - coords[city2][1]) ** 2)

# Find the best tour that minimizes the longest distance between two consecutive cities
def find_best_tour():
    cities = list(coords.keys())
    best_tour = None
    min_max_distance = float('inf')
    total_min_cost = float('inf')

    # Compute all permutations of cities starting with the depot (0)
    for tour in itertools.permutations(cities[1:]):  # Exclude the depot city for permutation
        full_tour = [0] + list(tour) + [0]  # Start and end at the depot 
        total_cost = sum(euclidean_distance(full_tour[i], full_tour[i+1]) for i in range(len(full_tour) - 1))
        max_distance = max(euclidean_distance(full_tour[i], full_tour[i+1]) for i in range(len(full_tour) - 1))

        if max_distance < min_max_distance or (max_distance == min_max_distance and total_cost < total_min_cost):
            best_tour = full_tour
            min_max_distance = max_distance
            total_min_cost = total_cost
    
    return best_tour, total_min_cost, min_max_distance

# Execute the function and print the result
best_tour, total_min_cost, min_max_distance = find_best_tour()
print("Tour:", best_tour)
print("Total travel cost:", total_min_cost)
print("Maximum distance between consecutive cities:", min_max_distance)