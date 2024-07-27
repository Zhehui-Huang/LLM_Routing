import math
import itertools

# City coordinates
cities = {
    0: (14, 77),  # depot
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

# City groups
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible tours by taking one city from each group
def all_possible_tours(groups):
    for combination in itertools.product(*groups):
        yield [0] + list(combination) + [0]

# Find the shortest tour
def find_shortest_tour():
    min_distance = float('inf')
    best_tour = None
    
    for tour in all_possible_tours(groups):
        # Calculate the total travel cost of the tour
        total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        # Check if this is the shortest tour found so far
        if total_cost < min_distance:
            min_distance = total_cost
            best_tour = tour
    
    return best_tour, min_distance

# Getting the best tour and cost
best_tour, min_cost = find_shortest_tour()

# Outputting the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")