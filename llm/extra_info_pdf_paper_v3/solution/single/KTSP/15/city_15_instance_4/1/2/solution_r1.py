import math
from itertools import permutations, combinations

# Given cities with their coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Target to visit k cities including the depot 0
k = 12

# Track the best tour and its cost
best_tour, best_cost = None, float('inf')

# Generate combinations of k-1 other cities to include in the tour
for comb in combinations([i for i in range(1, 15)], k - 1):
    # All permutations of chosen cities
    for perm in permutations(comb):
        # Create a tour starting and ending at the depot city 0
        tour = [0] + list(perm) + [0]
        # Calculate the total travel cost of this tour
        cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        
        # Update the best tour and best cost found
        if cost < best_cost:
            best_tour, best_cost = tour, cost

# Output the best tour and the associated cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {round(best_cost, 2)}")