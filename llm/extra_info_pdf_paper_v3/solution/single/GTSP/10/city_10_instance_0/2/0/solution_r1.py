import itertools
import math

# Cities coordinates
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98),
    4: (51, 69), 5: (47, 39), 6: (62, 26), 7: (79, 31),
    8: (61, 90), 9: (42, 49)
}

# City groups
city_groups = {
    0: [1, 2, 6],
    1: [3, 7, 8],
    2: [4, 5, 9]
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0])**2 + (cities[city_a][1] - cities[city_b][1])**2)

# Generate all combinations of cities to visit, one from each group
group_city_combinations = list(itertools.product(city_groups[0], city_groups[1], city_groups[2]))

# Function to calculate total tour distance for a given city sequence
def calculate_tour_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i+1])
    return total_distance

# Iterate to find the tour with the minimum distance
min_distance = float('inf')
optimal_tour = []

for combination in group_city_combinations:
    tour = [0] + list(combination) + [0]  # Start and end at the depot city
    current_distance = calculate_tour_distance(tour)
    if current_distance < min_distance:
        min_distance = current_distance
        optimal_tour = tour

# Print or return the optimal tour and its total distance
print("Tour:", optimal_tor)
print("Total travel cost:", min_distance)