import math
from itertools import product

# City coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Groups of cities
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Find the shortest path visiting one city from each group and returning to the depot
def find_shortest_tour():
    min_cost = float('inf')
    best_tour = []
    
    # Iterate over all combinations selecting one city from each group
    for combination in product(*groups):
        # Start at the depot city 0
        current_tour = [0]
        current_cost = 0
        
        # Add each city from the combination to the tour and calculate the cost
        for city in combination:
            current_tour.append(city)
            current_cost += distance(current_tour[-2], current_tour[-1])
        
        # Add the trip back to the depot
        current_tour.append(0)
        current_cost += distance(current_tour[-2], current_tour[-1])
        
        # Check if the current tour is better
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour
            
    return best_tour, min_cost

# Get the best tour and its cost
best_tour, min_cost = find_shortest_tour()

# Print the result in the required output format
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")