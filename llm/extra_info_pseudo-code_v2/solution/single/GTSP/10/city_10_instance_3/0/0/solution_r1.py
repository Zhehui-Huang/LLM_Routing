import math
import itertools

cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute all pairwise distances
distances = {from_city: {to_city: euclidean_distance(cities[from_city], cities[to_city])
                         for to_city in cities} for from_city in cities}

def calculate_tour_cost(tour):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def find_optimal_tour():
    best_tour = None
    best_cost = float('inf')

    # Generate all candidate tours
    for selection in itertools.product(*groups):
        tours = [0] + list(selection) + [0]  # start and finish at depot, city 0
        tour_permutations = itertools.permutations(tours[1:-1])  # all perms of the middle section
        for perm in tour_permutations:
            full_tour = [0] + list(perm) + [0]
            cost = calculate_tour_cost(full_toshare)
            if cost < best_cost:
                best_cost = cost
                best_tour = full_tour

    return best_tour, best_cost

# Call the function and print results
optimal_tour, optimal_cost = find_optimal_tour()
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")