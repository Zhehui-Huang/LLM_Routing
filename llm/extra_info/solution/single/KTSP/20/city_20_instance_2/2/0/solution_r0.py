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
    all_permutations = itertools.permutations(cities[1:], 9)  # Generate permutations excluding the depot
    shortest_distance = float('inf')
    best_tour = None

    # Evaluate each permutation
    for perm in all_permutations:
        tour = [cities[0]] + list(perm) + [cities[0]]  # Tour starts and ends at the depot
        total_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        # Update the shortest found distance and best tour
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            best_tour = tour

    return best_tour, shortest_distance

best_tour, shortest_distance = find_shortest_tour()

# Converting tour cities to indices
tour_indices = [cities.index(city) for city in best_tour]
    
print(f'Tour: {tour_indices}')
print(f'Total travel cost: {shortest_distance:.2f}')