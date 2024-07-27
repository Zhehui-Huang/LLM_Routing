import itertools
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Provided cities coordinates
cities = [
    (3, 26),   # Depot 0
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

def find_shortest_tour():
    all_permutations = itertools.permutations(range(1, 20), 9)  # Generate permutations of city indices excluding the depot
    shortest_distance = float('inf')
    best_tour_indices = None

    # Evaluate each permutation
    for perm_indices in all_permutations:
        tour_indices = [0] + list(perm_indices) + [0]  # Tour starts and ends at the depot
        tour = [cities[index] for index in tour_indices]
        total_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        # Update the shortest found distance and best tour
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            best_tour_indices = tour_indices

    return best_tour_indices, shortest_distance

best_tour_indices, shortest_distance = find_shortest_tour()

print(f'Tour: {best_tour_indices}')
print(f'Total travel cost: {shortest_distance:.2f}')