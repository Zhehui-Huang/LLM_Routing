import itertools
import math

# Define the cities' positions
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def find_shortest_tour():
    # Initialize variables to keep track of the minimum distance and the best tour.
    min_distance = float('inf')
    best_tour = None
    
    # Iterate over combinations of cities that the robot could possibly visit.
    for comb in itertools.combinations(range(1, 15), 7):
        # Include the depot as the starting and ending point, making combinations of 8 cities with the depot.
        current_cities = [0] + list(comb)
        # Check all permutations of these cities to find all possible tours that start and end at the depot.
        for perm in itertools.permutations(current_cities):
            tour = list(perm) + [0]
            # Compute the total travel cost for this tour
            total_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            # Update the best tour and minimum distance found so far.
            if total_distance < min_distance:
                min_distance = total_distance
                best_tour = tour
    
    return best_tour, min_distance

# Calculate the shortest tour and the total travel cost
tour, total_cost = find_shortest_tour()
print("Tour:", tour)
print("Total travel life tudistance:", total_cost)