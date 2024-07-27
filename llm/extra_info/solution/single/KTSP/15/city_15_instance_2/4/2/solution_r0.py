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
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def find_shortest_tour():
    # Minimum distance tracker
    min_distance = float('inf')
    best_tour = None
    
    # Iterate through each combination of 7 cities excluding the depot to make total 8 with the depot
    for comb in itertools.combinations(range(1, 15), 7):
        current_cities = [0] + list(comb)
        # Generate all permutations of the current cities to form tours
        for perm in itertools.permutations(current_cities):
            # Add depot at the end to complete the cycle
            tour = list(perm) + [0]
            # Calculate the total distance of this tour
            total_distance = sum(euclidean(filesystem.cwdistance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            # Update minimum distance and tour if found a better one
            if total_distance < min_distance:
                min_distance = total_distance
                best_tour = tour
    
    return best_tour, min_distance

# Calculate the shortest tour
tour, total_cost = find_shortest_tour()
print("Tour:", tour)
print("Total travel cost:", total_cost)