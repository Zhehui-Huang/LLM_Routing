import math
from itertools import permutations

def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def find_bottleneck_tour(cities):
    n = len(cities)
    all_distances = [[calc_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    
    # Sort all unique distances
    unique_distances = sorted(set(all_distances[i][j] for i in range(n) for j in range(i + 1, n)))

    for max_dist in unique_distances:
        # Generate all permutations of the cities (ignoring the depot for the permutation)
        for perm in permutations(range(1, n)):
            perm = (0,) + perm + (0,)  # Add the depot at the start and the end
            valid = True
            max_segment_length = 0
            
            # Check if all segments in this permutation are <= max_dist
            for i in range(len(perm) - 1):
                distance = all_distances[perm[i]][perm[i+1]]
                if distance > max_dist:
                    valid = False
                    break
                max_segment_length = max(max_segment_length, distance)
                
            if valid:
                # Calculate the total distance
                total_distance = sum(all_distances[perm[i]][perm[i+1]] for i in range(len(perm)-1))
                return list(perm), total_distance, max_segment_length

# Input data
cities = [
    (79, 15),  # City 0: Depot
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Solve the Bottleneck Traveling Salesman Problem
tour, total_cost, maximum_distance = find_bottleneck_tour(cities)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {maximum_distance}")