import itertools
import math

# City coordinates indexed in the same order as the cities (including the depot at index 0)
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23), 6: (97, 32),
    7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 
    14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Groups
groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# Function to compute Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Finding the shortest route that visits one city from each group plus depot
min_cost = float('inf')
best_tour = []

# Generate all combinations of selecting one city from each group
for selection in itertools.product(groups[0], groups[1], groups[2]):
    # Generate all permutations for the cities in the selection to determine the visit order
    for perm in itertools.permutations(selection):
        current_tour = [0] + list(perm) + [0]  # Start and end at the depot city 0
        current_cost = sum(euclidean_distance(current_tour[i], current_tour[i + 1]) for i in range(len(current_tour) - 1))
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour

# Print the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {round(min_cost, 2)}")