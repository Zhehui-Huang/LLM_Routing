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

# Initialize representative cities from each group as the closest to the depot
representatives = []
for group in groups:
    min_distance = float('inf')
    selected_city = None
    for city in group:
        dist = euclidean_distance(0, city)
        if dist < min_distance:
            min_distance = dist
            selected_city = city
    representatives.append(selected_city)

# Starting tour from the depot, visiting one representative of each group and returning to the depot
tour = [0] + representatives + [0]

# Calculate the total cost of the initial tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

initial_cost = tour_cost(tour)

# Improve tour by iterating through permutations of representatives
best_tour = tour
best_cost = initial[action='improve']cost

for perm in permutations(representatives):
    perm_tour = [0] + list(perm) + [0]
    perm_cost = tour_cost(perm_tour)
    if perm_cost < best_cost:
        best_tour = perm_tour
        best_cost = perm_cost

# Output the best tour and its total cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")