import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of the cities
cities = [
    (84, 67),  # City 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

def find_shortest_tour():
    best_tour = None
    best_cost = float('inf')
    
    # Generate all subsets of 6 cities (excluding city 0 as it must be in the tour)
    for subset in permutations(range(1, 10), 6):
        current_path = [0] + list(subset) + [0]  # tour starts and ends at city 0

        # Calculate the total cost of the current tour
        current_cost = 0
        for i in range(len(current_path) - 1):
            current_cost += euclidean_distance(cities[current_path[i]], cities[current_path[i + 1]])
        
        # Compare and update if found better
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_path

    return best_tour, best_cost

tour, cost = find_shortest_tour()
print("Tour:", tour)
print("Total travel cost:", round(cost, 2))