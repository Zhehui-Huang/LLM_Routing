import itertools
import math

# Define the cities and their coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9), 
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Define the groups of cities (one city from each group must be visited)
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Function to calculate Euclidean distance between two cities
def euc_dist(city_a, city_b):
    ax, ay = cities[city_a]
    bx, by = cities[city_b]
    return math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)

# Iterating over all combinations where one city is picked from each group
min_tour = None
min_cost = float('inf')

for selection in itertools.product(*groups):
    # Complete tour starting and ending at the depot, which is city 0
    tour = [0] + list(selection) + [0]
    
    # Calculate the total cost of this tour
    total_cost = sum(euc_dist(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    
    # Update minimum cost and tour if current is better
    if total_cost < min_cost:
        min_tour = tour
        min_cost = total_cost

# Output the results
print(f"Tour: {min_tour}")
print(f"Total travel cost: {round(min_cost, 2)}")