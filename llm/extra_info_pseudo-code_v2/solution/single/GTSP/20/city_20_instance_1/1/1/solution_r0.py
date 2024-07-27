import math
import itertools

# City Coordinates
cities = {
    0: (14, 77),   # Depot
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Groups of cities
groups = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

# Function to calculate Euclidean distance
def distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Generate all permutations of the selected cities
def find_best_tour():
    best_tour = None
    best_cost = float('inf')
    
    # Iterate over all combinations of selecting one city from each group
    for combination in itertools.product(*groups.values()):
        complete_tour = [0] + list(combination) + [0]
        total_cost = sum(distance(complete_tour[i], complete_tour[i + 1]) for i in range(len(complete_tour) - 1))
        
        if total_cost < best_cost:
            best_tour = complete_tour
            best_cost = total_cost
            
    return best_tour, best_cost

# Finding the best tour
tour, total_cost = find_best_tour()

# Print results
print("Tour:", tour)
print("Total travel cost:", total_cost)