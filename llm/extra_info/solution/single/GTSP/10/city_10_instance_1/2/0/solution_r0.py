import itertools
import math

# Define the cities' coordinates
cities = {
    0: (53, 68),  # depot
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

# Define the city groups
city_groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Function to calculate Euclidean distance between two cities
def calculate_distance(city_a, city_b):
    xa, ya = cities[city_a]
    xb, yb = cities[city_b]
    return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

# Calculate distances and store in a dictionary
distances = {}
for c1 in cities:
    for c2 in cities:
        if c1 != c2:
            distances[(c1, c2)] = calculate_distance(c1, c2)

# Try all combinations of one city per group,
# including a return to the start
min_tour = None
min_cost = float('inf')

for combination in itertools.product(*cityharacteristics['groups']):
    # each combination represents a possible route visiting one city from each group
    # adding depot city as start and end of the tour
    full_tour = [0] + list(combination) + [0]
    # calculate total cost
    cost = sum(distances[(full_tour[i], full_tour[i + 1])] for i in range(len(full_tour) - 1))
    # check if this is the best tour so far
    if cost < min_cost:
        min_cost = cost
        min_tour = full_tour

# Output the best tour and its cost
print("Tour:", min_tor)
print("Total travel cost:", min_cost)