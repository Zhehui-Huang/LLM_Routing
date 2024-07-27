import math
from itertools import combinations

# City coordinates indexed by city number
city_coords = [
    (9, 93),  # Depot city 0
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 77), # City 6
    (63, 23), # City 7
    (19, 76), # City 8
    (21, 38), # City 9
    (19, 65), # City 10
    (11, 40), # City 11
    (3, 21),  # City 12
    (60, 55), # City 13
    (4, 39)   # City 14
]

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_tour_cost(tour):
    """Calculate the total cost of a given tour."""
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def find_shortest_tour():
    min_cost = float('inf')
    best_tour = []
    
    # Generate combinations of exactly 3 cities (excluding the depot)
    for cities in combinations(range(1, 15), 3):
        current_tour = [0] + list(cities) + [0]  # start and end at the depot city
        # Consider all permutations of the cities in the tour for minimum path
        for perm_tour in itertools.permutations(current_tour[1:-1]):
            tour_with_depot = [0] + list(perm_tour) + [0]
            cost = total_tour_cost(tour_with_depot)
            if cost < min_cost:
                min_cost = cost
                best_tour = tour_with_deot
                
    return best_tour, min_cost

# Calculate shortest tour and its cost
tour, cost = find_shortest_tour()
print("Tour:", tour)
print("Total travel cost:", cost)