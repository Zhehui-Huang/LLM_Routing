import itertools
import math

# Defining city coordinates
cities = [
    (9, 93),  # Depot city 0
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 77), # City 6
    (63, 23), # City 7
    (19, 76), # City 8
    (21, 38), # City 9
    (19, 65), # City 10
    (11, 40), # City 11
    (3, 21),  # City 12
    (60, 55), # City 13
    (4, 39)   # City 14
]

# Grouping of cities
groups = [[2, 7, 10, 11, 14], [1, 3, 5, 8, 13], [4, 6, 9, 12]]

# Function to compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Calculate all possible selections of one city from each group
all_selections = list(itertools.product(*groups))

# Function to calculate total cost of a given tour
def calculate_tour_cost(selection):
    tour = [0] + list(selection) + [0]
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

# Finding the optimal tour
min_cost = float('inf')
best_tour = []

for selection in all_selections:
    cost = calculate_tour_cost(selection)
    if cost < min_cost:
        min_cost = cost
        best_tour = [0] + list(selection) + [0]

# Print the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)