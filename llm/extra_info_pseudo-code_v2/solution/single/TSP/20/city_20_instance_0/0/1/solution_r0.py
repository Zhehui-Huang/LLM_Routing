import math
from itertools import combinations

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour, coordinates):
    """Calculate the total distance of the given tour based on coordinates."""
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_distance

# Coordinates of the cities indexed from 0 (depot) to 19
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Initialize a simple nearest neighbor tour for initial guess
def nearest_neighbor_tour(start_node, n_cities):
    tour = [start_node]
    available_cities = set(range(n_cities)) - {start_node}
    
    current_city = start_node
    while available_cities:
        next_city = min(available_cities, key=lambda city: euclidean_sub_cost(current_city, city))
        tour.append(next_city)
        available_cities.remove(next_city)
        current_city = next_city
    
    tour.append(start_node)  # return to the depot
    return tour

def euclidean_sub_cost(c1, c2):
    return euclidean_distance(coordinates[c1], coordinates[c2])

initial_tour = nearest_neighbor_tour(0, 20)

# Lin-Kernighan implementation
def lin_kernighan(tour):
    best_tour = tour[:]
    best_distance = calculate_total_distance(tour, coordinates)
    improved = True
    
    while improved:
        improved = False
        for swap_first in range(1, len(tour) - 2):
            for swap_second in range(swap_first + 2, len(tour)):
                if swap_second == len(tour) - 1 and swap_first == 1:
                    continue
                new_tour = tour[:swap_first] + tour[swap_first:swap_second][::-1] + tour[swap_second:]
                new_distance = calculate_total_distance(new_tour, coordinates)
                if new_distance < best_distance:
                    best_tour = new_tour[:]
                    best_distance = new_distance
                    improved = True
        return best_tour, best_distance

best_tour, total_distance = lin_kernighan(initial_tour)

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", total_distance)