import random
import math

# Coordinates of the depot and cities
coordinates = [
    (16, 90),  # City 0: Depot
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# City groups
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

def total_tour_cost(tour):
    """Calculate the total cost of a given tour."""
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(tour[i-1], tour[i])
    return total_cost

def find_shortest_tour():
    """Find the shortest tour that visits one city from each group starting and ending at the depot."""
    best_tour = None
    min_cost = float('inf')
    
    # Perform exhaustive search over all possible combinations (one per group)
    for perm1 in city_groups[0]:
        for perm2 in city_groups[1]:
            for perm3 in city_groups[2]:
                for perm4 in city_groups[3]:
                    for perm5 in city_groups[4]:
                        for perm6 in citygroups[5]:
                            candidate_tour = [0, perm1, perm2, perm3, perm4, perm5, perm6, 0] 
                            cost = total_tour_cost(candidate_tour)
                            if cost < min_cost:
                                min_cost = cost
                                best_tour = candidate_tour

    return best_tour, min_cost

# Find the best tour and its cost
best_tour, min_cost = find_shortest_tour()

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", min_cost)