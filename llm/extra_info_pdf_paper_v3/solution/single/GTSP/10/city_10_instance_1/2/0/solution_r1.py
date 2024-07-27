import math
from itertools import product

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# City groups
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Function to calculate Euclidean Distance
def euclidean_distance(city1, city2):
    dx = cities[city1][0] - cities[city2][0]
    dy = cities[city1][1] - cities[city2][1]
    return math.sqrt(dx**2 + dy**2)

# Generate and evaluate all potential tours that visit one city from each group
def find_optimal_tour():
    best_tour = None
    best_cost = float('inf')
    
    # Create all possible combinations by taking one city from each group
    for plan in product(*groups):
        # Create the full tour starting and ending at the depot
        current_tour = [0] + list(plan) + [0]
        current_cost = 0
        
        # Calculate the total cost of this tour
        for i in range(1, len(current_tour)):
            current_cost += euclidean_distance(current_tour[i - 1], current_tour[i])
        
        # Record the tour if it's the best found so far
        if current_cost < best_cost:
            best_tour = current_tour
            best_cost = current_cost
            
    return best_tour, best_cost

# Compute the optimal tour and its cost
optimal_tour, optimal_cost = find_optimal_tour()

# Output result
print("Tour:", optimal_tour)
print(f"Total travel cost: {optimal_cost:.2f}")