import math
from itertools import combinations

def calc_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_tour_distance(tour, cities):
    """Compute the total distance of the given tour using the cities coordinates."""
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calc_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

def find_shortest_tour(cities, k):
    """Find the shortest tour visiting exactly k cities starting and ending at the depot city."""
    n = len(cities)
    min_tour = None
    min_distance = float('inf')
    
    for comb in combinations(range(1, n), k - 1):  # combine other cities to form potential tours
        possible_tour = [0] + list(comb) + [0]  # always start and end at depot (city 0)
        possible_distance = total_tour_distance(possible_tour, cities)
        if possible_distance < min_distance:
            min_distance = possible_distance
            min_tour = possible_tour
            
    return min_tour, min_distance

# Cities coordinates
cities = [
    (84, 67),  # City 0 - depot
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

# k is the total number of cities including the depot city that the robot should visit
k = 7

# Find the shortest tour satisfying the condition
tour, total_cost = find_shortest_tour(cities, k)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")