import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def create_distance_matrix(cities):
    n = len(cities)
    dist_matrix = {}
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[(i, j)] = euclidean_distance(cities[i], cities[j])
    return dist_matrix

def find_bottleneck_tour(cities):
    n = len(cities)
    dist_matrix = create_distance_matrix(cities)
    all_tours = permutations(range(1, n))
    min_max_dist = float('inf')
    optimal_tour = None
    
    for tour in all_tours:
        current_tour = [0] + list(tour) + [0]
        max_dist = max(dist_matrix[(current_tour[i], current_tour[i + 1])] for i in range(len(current_tour) - 1))
        
        if max_dist < min_max_dist:
            min_max_dist = max_dist
            optimal_tour = current_tour
    
    total_cost = sum(dist_matrix[(optimal_tour[i], optimal_tour[i + 1])] for i in range(len(optimal_tour) - 1))
    
    return optimal_tour, total_cost, min_max_dist

# Define cities coordinates
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Finding the optimal tour minimizing the bottleneck distance
tour, total_cost, max_distance = find_bottleneck_tour(cities)

# Print output
print("Tour:", tour)
print("Total travel cost: {:.2f}".format(total_cost))
print("Maximum distance between consecutive cities: {:.2f}".format(max_distance))