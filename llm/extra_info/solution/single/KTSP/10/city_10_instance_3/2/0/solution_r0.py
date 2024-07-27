import itertools
import math

# Define coordinates of the cities
city_coordinates = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible combinations of 6 cities (excluding depot city, since it must be included)
other_cities = list(city_coordinates.keys())[1:]
city_combinations = itertools.combinations(other_cities, 6)

# Find the shortest tour
min_cost = float('inf')
best_tour = []

for combination in city_combinations:
    cities_to_visit = [0] + list(combination)

    # Generate all permutations of selected cities to visit
    for perm in itertools.permutations(cities_to_visit[1:]):
        tour = [0] + list(perm) + [0]

        # Calculate the total travel cost of the tour
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += calculate_distance(tour[i], tour[i+1])

        # Check if this tour is better than what we have found before
        if total_cost < min_cost:
            min_cost = total_cost
            best_tour = tour

# Output the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_process))