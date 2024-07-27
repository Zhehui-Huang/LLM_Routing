import math
import itertools

# Define the cities and their groups
cities = {
    0: (3, 26), 
    1: (85, 72), 
    2: (67, 0), 
    3: (50, 99), 
    4: (61, 89), 
    5: (91, 56), 
    6: (2, 65), 
    7: (38, 68), 
    8: (3, 92), 
    9: (59, 8), 
    10: (30, 88), 
    11: (30, 53), 
    12: (11, 14), 
    13: (52, 49), 
    14: (18, 49), 
    15: (64, 41), 
    16: (28, 49), 
    17: (91, 94), 
    18: (51, 58), 
    19: (30, 48)
}
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Precompute distances
distances = {}
for c1 in cities:
    for c2 in cities:
        if c1 != c2:
            distances[(c1, c2)] = calculate_distance(c1, c2)

# Function to find the shortest tour using a heuristic approach
def find_shortest_tour():
    best_tour = None
    best_cost = float('inf')
    
    # Generate all combinations of picking one city from each group
    for combination in itertools.product(*groups):
        # Start with the depot, end with the depot
        current_tour = [0] + list(combination) + [0]
        
        # Calculate the cost of the tour
        current_cost = 0
        for j in range(len(current_tour) - 1):
            current_cost += distances[(current_tour[j], current_tour[j+1])]
        
        # Check if this tour is better
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_tour
    
    return best_tour, best_cost

# Find the tour and the cost
tour, cost = find_shortest_tour()

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")