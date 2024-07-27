import itertools
import math

# Define the cities' coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate distances between each pair of cities
distances = {}
for i in cities:
    for j in cities:
        distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Function to calculate the tour cost
def tour_cost(tour):
    return sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

# Finding the shortest tour visiting exactly 4 cities
min_cost = float('inf')
best_tour = None

# Iterate over combinations of 3 cities, excluding the depot city (0)
for combo in itertools.combinations([i for i in cities if i != 0], 3):
    current_group = [0] + list(combo)  # Start with depot city

    # Generate permutations of current group to create tours
    for perm in itertools.permutations(current_group):
        if perm[0] == 0:  # Ensure the tour starts with the depot city
            tour = list(perm) + [0]  # Complete the tour by returning to the depot
            cost = tour_cost(tour)
            if cost < min_cost:
                min_cost = cost
                best_tour = tour

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", min_cost)