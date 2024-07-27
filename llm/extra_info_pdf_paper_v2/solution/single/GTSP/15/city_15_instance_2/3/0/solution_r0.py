import itertools
import math

# City coordinates
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

# Groups of cities
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Search for the shortest path visiting one city from each group starting and ending at the depot
def find_shortest_tour():
    minimum_cost = float('inf')
    best_tour = []
    
    # Generate all combinations, one city from each group
    for combination in itertools.product(*groups):
        # Start with depot city
        current_tour = [0] + list(combination) + [0]
        # Calculate the tour cost
        current_cost = sum(euclidean_distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))
        
        # Check if the found tour is better
        if current_cost < minimum_cost:
            minimum_cost = current_cost
            best_tour = current_tour
            
    return best_tour, minimum_cost

# Get the optimal tour and its cost
optimal_tour, optimal_cost = find_shortest_tour()

print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")