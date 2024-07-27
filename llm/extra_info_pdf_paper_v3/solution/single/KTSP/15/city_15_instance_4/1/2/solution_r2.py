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

# Function to find the shortest tour visiting exactly k cities
def find_shortest_tour(k):
    best_tour = None
    best_cost = float('inf')

    for comb in combinations(range(1, 15), k - 1):  # Combinations of k-1 cities, not including the depot city 0
        for perm in permutations(comb):
            # Constructing the tour starting and ending at the depot, city 0
            tour = [0] + list(perm) + [0]
            # Calculate the cost of the tour
            cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            
            # Update best tour and cost if current one is better
            if cost < best_cost:
                best_tour, best_cost = tour, cost

    return best_tour, best_cost

# Set k to 12 including the depot
k = 12
best_tour, best_cost = find_shortest_tour(k)

# Output results
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))