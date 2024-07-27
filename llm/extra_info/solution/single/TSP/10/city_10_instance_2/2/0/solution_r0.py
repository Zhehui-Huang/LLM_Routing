import itertools
import math

# Define the cities with their coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all permutations of city visits, excluding the depot city (0)
city_indices = list(cities.keys())[1:]  # cities except the depot
tours = itertools.permutations(city_indices)

# Variable to track the minimum cost tour
min_cost = float('inf')
best_tour = None

# Evaluate each possible tour
for tour in tours:
    total_cost = calculate_distance(0, tour[0])  # Cost from depot to first city in the tour
    for i in range(len(tour)-1):
        total_cost += calculate_distance(tour[i], tour[i+1])  # Cost from current city to next city
    total_cost += calculate_distance(tour[-1], 0)  # Cost from last city back to the depot
    
    # Update the minimum cost and the best tour if the current tour is better
    if total_cost < min_cost:
        min_cost = total_cost
        best_tour = tour

# Prepare the output format
tour_output = [0] + list(best_tour) + [0]
output = f"Tour: {tour_output}\nTotal travel cost: {min_cost:.2f}"

print(output)