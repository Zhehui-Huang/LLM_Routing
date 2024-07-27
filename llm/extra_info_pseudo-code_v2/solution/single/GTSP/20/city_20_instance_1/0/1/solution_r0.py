import itertools
import math

# Define the city coordinates
cities = [
    (14, 77),  # Depot 0
    (34, 20),  # 1
    (19, 38),  # 2
    (14, 91),  # 3
    (68, 98),  # 4
    (45, 84),  # 5
    (4, 56),   # 6
    (54, 82),  # 7
    (37, 28),  # 8
    (27, 45),  # 9
    (90, 85),  # 10
    (98, 76),  # 11
    (6, 19),   # 12
    (26, 29),  # 13
    (21, 79),  # 14
    (49, 23),  # 15
    (78, 76),  # 16
    (68, 45),  # 17
    (50, 28),  # 18
    (69, 9)    # 19
]

# Define the groups of cities
city_groups = [
    [5, 6, 7, 11, 17],    # Group 0
    [1, 4, 8, 13, 16],    # Group 1
    [2, 10, 15, 18, 19],  # Group 2
    [3, 9, 12, 14]        # Group 3
]

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Iterate over all combinations, one city from each group
min_cost = float('inf')
best_tour = None

for combination in itertools.product(*city_groups):
    # Prepend and append the depot city
    full_tour = [0] + list(combination) + [0]
    
    # Calculate the total cost
    total_cost = sum(distance(full_tour[i], full_tour[i+1]) for i in range(len(full_tour) - 1))
    
    # Update the best tour if found a lower cost
    if total_cost < min_cost:
        min_cost = total_cost
        best_tour = full_tour

# Output the best tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")