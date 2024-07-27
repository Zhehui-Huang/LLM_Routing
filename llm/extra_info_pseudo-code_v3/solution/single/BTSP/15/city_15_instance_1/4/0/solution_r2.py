import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def find_bottleneck_tour(cities):
    num_cities = len(cities)
    all_edges_and_distances = [(i, j, euclidean_distance(cities[i], cities[j])) 
                                for i in range(num_cities) 
                                for j in range(i + 1, num_cities)]
    all_edges_and_distances_sorted = sorted(all_edges_and_distances, key=lambda x: x[2])
    
    # Test increasing thresholds (sorted edge lengths)
    for _, _, max_edge_length in all_edges_and_distances_sorted:
        # Try every permutation for a valid tour under current max_edge_length
        for perm in permutations(range(1, num_cities)):
            tour = [0] + list(perm) + [0]
            max_distance_in_tour = max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
            if max_distance_in_tour <= max_edge_length:
                total_travel_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
                return tour, total_travel_cost, max_edge_length

    return None

cities = [
    (29, 51), # Depot city
    (49, 20),
    (79, 69),
    (17, 20),
    (18, 61),
    (40, 57),
    (57, 30),
    (36, 12),
    (93, 43),
    (17, 36),
    (4, 60),
    (78, 82),
    (83, 96),
    (60, 50),
    (98, 1)
]

result = find_bottleneck_tour(cities)

if result:
    tour, total_cost, max_distance = result
    print("Tour:", tour)
    print("Total travel cost:", round(total_cost, 2))
    print("Maximum distance between consecutive cities:", round(max_distance, 2))
else:
    print("No valid tour was found given the constraints.")