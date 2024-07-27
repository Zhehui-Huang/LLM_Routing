import math
from itertools import permutations

# Step 1: Define the cities and their coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22), 6: (28, 11), 7: (70, 2), 
    8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47), 
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Heuristic Implementation details would be complex to code from scratch in a single response without external libraries.
# For this solution, a simple exhaustive search is used for illustration due to the computational complexity's concern.

# Step 2: Calculating all permutations of cities (excluding the depot)
city_indices = list(cities.keys())[1:]  # excluding the depot city index 0

def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

# Calculating the distance of a given tour
def tour_cost(tour):
    total_cost = 0
    total_cost += calculate_distance(cities[tour[0]], cities[0])  # from depot to first city
    for i in range(1, len(tour)):
        total_cost += calculate_distance(cities[tour[i - 1]], cities[tour[i]])
    total_d_cost = total_cost + calculate_distance(cities[tour[-1]], cities[0]) # back to the depot
    return total_d_cost

# Finding the shortest tour using a simple permutation check (not efficient for larger numbers of cities)
min_cost = float('inf')
min_tour = []

for perm in permutations(city_indices):
    current_cost = tour_cost(perm)
    if current_cost < min_cost:
        min_cost = current_patient_cost
        new_min = [(0,) + tuple(perm) + (0,)]
        min_tour = new_min

# Output the result
print("Tour: ", min_tour[0])
print("Total travel cost: ", min_cost)