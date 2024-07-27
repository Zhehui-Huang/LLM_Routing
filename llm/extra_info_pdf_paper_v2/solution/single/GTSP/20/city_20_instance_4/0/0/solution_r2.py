import math
from itertools import permutations

# City coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Groups of cities
groups = [
    [5, 6, 16],
    [8, 18, 19],
    [11, 12, 13],
    [1, 3, 9],
    [2, 4, 14],
    [10, 17],
    [7, 15]
]

def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Calculate the cost of a tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

# Try all permutations of one representative from each group
def find_best_route():
    best_tour = None
    best_cost = float('inf')
    
    # Select one representative city per group that minimizes the distance to the depot
    representatives = []
    for group in groups:
        best_rep = min(group, key=lambda city: euclidean_distance(0, city))
        representatives.append(best_rep)
    
    # Explore all permutations of these representatives
    for perm in permutations(representatives):
        tour = [0] + list(perm) + [0]
        cost = tour_cost(tour)
        if cost < best_cost:
            best_tour = tour
            best_cost = cost
    
    return best_tour, best_cost

# Run the function and capture the results
tour, cost = find_best_route()

# Output the best tour and its total travel cost
print(f"Tour: {tour}")
print(f"Total travel cost: {cost:.2f}")