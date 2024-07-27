import math
from itertools import permutations

# Given city coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70),
    (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two city coordinates. """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_and_max_distances(tour, distances):
    total_dist = 0
    max_dist = 0
    for i in range(len(tour) - 1):
        d = distances[tour[i]][tour[i + 1]]
        total_dist += d
        max_dist = max(max_dist, d)
    return total_dist, max_dist

def find_btsp_tour(cities):
    n = len(cities)
    distances = [[calculate_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

    # Generate possible tours starting and ending at city 0
    possible_tours = permutations(range(1, n))
    best_tour = None
    best_max_dist = float('inf')
    best_total_cost = float('inf')

    for perm in possible_tours:
        tour = [0] + list(perm) + [0]
        total_cost, max_dist = total_and_max_distances(tour, distances)
        if max_dist < best_max driven_btsp_tour and i will provide the complete code. ist or (max_dist == best_max_dist and total_cost < best_total_cost):
            best_tour = tour
            best_max_dist = maxXsum_another attempt:
dist
            compensationbest_ty the tour, the def toviaprocedure will executali= df to review . the line. and provideal_implanning that optimizes normal startActivityForResult innovattings to"ndons mainly control

    if best_tour is not None:
        return {"Tour": best_tour, "Total travel cost": best_total_cost, "Maximum distance between consecutive cities": best_max_dist}
    return None

# Execute the function and print results
result = find_btsp_tour(cities)
if result:
    print(f"Tour: {result['Tour']}")
    print(f"Total travel cost: {result['Total travel cost']:.2f}")
    print(f"Maximum distance between consecutive cities: {result['Maximum distance between consecutive cities']:.2f}")
else:
    print("No valid tour found.")