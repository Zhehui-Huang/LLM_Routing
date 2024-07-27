import math
from itertools import combinations, permutations
from scipy.spatial import distance

# City coordinates mapped to their indices
coordinates = {
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

def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to calculate the total route cost
def calculate_route_cost(route):
    return sum(euclidean_dist(coordinates[route[i]], coordinates[route[i + 1]]) for i in range(len(route) - 1))

# Generate all combinations by choosing 6 additional cities alongside city 0
city_indices = list(coordinates.keys())[1:]  # Excluding depot city
possible_tours = []
for subset in combinations(city_indices, 6):
    # Ensuring depot city 0 is at the start and end
    subset = [0] + list(subset) + [0]
    # Attempt basic optimization by trying all permutations within the subset for the minimum tour cost
    min_tour_cost = float('inf')
    optimal_tour = None
    for perm in permutations(subset[1:-1]):
        current_tour = [0] + list(perm) + [0]
        current_cost = calculate_route_cost(current_tour)
        if current_cost < min_tour_cost:
            min_tour_cost = current_cost
            optimal_tour = current_tour
    possible_tours.append((optimal_tour, min_tour_cost))

# Finding the shortest tour and the associated cost
shortest_tour, shortest_tour_cost = min(possible_tours, key=lambda x: x[1])

print("Tour:", shortest_tour)
print("Total travel cost:", shortest_tour_cost)