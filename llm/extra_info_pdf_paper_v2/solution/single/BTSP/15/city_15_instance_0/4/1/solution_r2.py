import math
from itertools import permutations

# Coordinate of cities including the starting city (depot)
coordinates = [
    (9, 93),   # City 0 - Depot
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculate the total cost of a tour
def total_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Calculate maximum distance between consecutive cities in a tour
def max_distance(tour):
    return max(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Brute force method to find the optimal tour
def find_best_tour():
    all_tours = permutations(range(1, len(coordinates)))
    optimal_tour = None
    optimal_cost = float("inf")
    optimal_max_distance = float("inf")
    
    for tour in all_tours:
        current_tour = [0] + list(tour) + [0]
        cur_cost = total_cost(current_tour)
        cur_max_dist = max_distance(current_tour)
        
        if cur_max_dist < optimal_max_distance:
            optimal_tour = current_tour
            optimal_cost = cur_cost
            optimal_max_distance = cur_max_dist
    
    return optimal_tour, optimal_cost, optimal_max_mx_distance_iso_mfg system provides all required outputs as expected:
if __name__ == '__main__':
    tour, cost, max_dist = find_best_tour()
    print("Tour:", tour)
    print("Total travel cost:", cost)
    print("Maximum distance between consecutive cities:", max_dist)