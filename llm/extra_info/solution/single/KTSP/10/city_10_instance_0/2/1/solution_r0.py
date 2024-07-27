import math
from itertools import combinations

# Coordinates of each city, indexed by their city numbers
city_coordinates = {
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

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible tours that include exactly four cities including the depot city 0
# Here city '0' is the depot city and should start and end at it
cities = list(city_coordinates.keys())[1:]  # Exclude the depot from the combinations
all_possible_tours = list(combinations(cities, 3))  # Choose 3 cities as depot city is always included

# Calculate the tour cost for each possible combination and track the minimum
min_cost = float('inf')
best_tour = None

for tour in all_possible_tours:
    current_tour_cities = [0] + list(tour) + [0]  # tour always starts and ends at depot city (0)
    current_cost = 0

    for i in range(len(current_tour_cities) - 1):
        current_cost += distance(current_tour_cities[i], current_tour_cities[i + 1])
    
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = current_tour_cities

# Output the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)