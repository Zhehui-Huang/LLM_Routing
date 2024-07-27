import itertools
import math

# Provided city data
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Grouping cities
city_groups = {
    0: [1, 2, 6],
    1: [3, 7, 8],
    2: [4, 5, 9]
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all combinations: one city from each group
combinations = list(itertools.product(city_groups[0], city_groups[1], city_groups[2]))

# Calculate the shortest tour that visits one city from each group and returns to depot
best_tour = None
min_cost = float('inf')

for combination in combinations:
    all_tours = itertools.permutations(combination)  # Generate all permutations of cities in the combination
    for tour in all_tours:
        # Calculate cost of going depot -> city1 -> city2 -> city3 -> depot
        cost = distance(0, tour[0]) + distance(tour[0], tour[1]) + distance(tour[1], tour[2]) + distance(tour[2], 0)
        if cost < min_cost:
            min_cost = cost
            best_tour = [0] + list(tour) + [0]

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")