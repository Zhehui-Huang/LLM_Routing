import math
import itertools

# City coordinates
cities = {
    0: (14, 77),
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
city_groups = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to find the shortest path considering one city from each group
def find_shortest_tour():
    all_combinations = list(itertools.product(*city_groups.values()))
    shortest_distance = float('inf')
    best_tour = []
    
    for combination in all_combinations:
        # Permutations of the chosen cities in the combination
        for perm in itertools.permutations(combination):
            # Check tour: depot -> cities in perm -> depot
            tour_distance = distance(0, perm[0]) + distance(perm[-1], 0)
            for i in range(len(perm) - 1):
                tour_distance += distance(perm[i], perm[i + 1])
            
            if tour_distance < shortest_distance:
                shortest_distance = tour_distance
                best_tour = [0] + list(perm) + [0]
    
    return best_tour, shortest_distance

# Compute the result
tour, total_cost = find_shortest_tour()

# Outputting the result
print("Tour:", tour)
print("Total travel cost:", total_cost)