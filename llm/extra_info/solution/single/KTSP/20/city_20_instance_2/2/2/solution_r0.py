import itertools
import math

# Define the coordinate of the cities
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Euclidean distance function
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Generate all combinations of 9 cities to combine with the depot (0)
city_indices = list(cities.keys())[1:]
combinations = itertools.combinations(city_indices, 9)

# Stores the minimum tour found
min_tour = None
min_cost = float('inf')

# Search among combinations to find the shortest possible tour
for combination in combinations:
    all_cities = [0] + list(combination)
    
    # Find the shortest route among these cities using Nearest Neighbor Algorithm
    remaining_cities = all_cities[:]
    tour = [remaining_cities.pop(0)]  # Start at the depot city
    current_city = tour[0]

    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: euclidean_distance(current_city, x))
        remaining_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city

    # Close the tour back to the depot city
    tour.append(0)
    
    # Calculate the cost of the tour
    tour_cost = sum(euclidean distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    
    # Update the minimum tour details if the current one is shorter
    if tour_cost < min_cost:
        min_cost = tour_cost
        min_tour = tour

# Output the result
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost}")