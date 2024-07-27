import math
from itertools import permutations

# Define the coordinates of the depot city and other cities
coordinates = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17),
}

# Calculate the Euclidean distance between two cities
def distance(c1, c2):
    return math.sqrt((coordinates[c1][0] - coordinates[c2][0])**2 + (coordinates[c1][1] - coordinates[c2][1])**2)

# Create a function to find the shortest tour
def find_best_tour():
    cities = list(coordinates.keys())[1:]  # excluding the depot city from permutations
    best_tour = None
    min_cost = float('inf')
    
    # Generate all permutations of the city indices
    for perm in permutations(cities):
        # include the depot city at the start and end of the tour
        tour = [0] + list(perm) + [0]
        current_cost = 0
        
        # Calculate the cost of the tour
        for i in range(len(tour) - 1):
            current_cost += distance(tour[i], tour[i+1])
        
        # Update the best tour found
        if current_cost < min_cost:
            best_tour = tour
            min_cost = current_cost
        
    return best_tour, min_cost

# Execute the function
best_tour, minimal_cost = find_best_tour()

# Output the results as specified
print(f"Tour: {best_tour}")
print(f"Total travel cost: {minimal_cost:.2f}")