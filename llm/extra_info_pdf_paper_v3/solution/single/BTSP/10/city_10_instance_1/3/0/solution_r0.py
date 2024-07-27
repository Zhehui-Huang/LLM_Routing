from itertools import permutations
import math

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define cities
cities_coordinates = {
    0: (53, 68),
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

# Generate all possible tours (permutations) starting and ending at depot (city 0)
all_cities = list(cities_coordinates.keys())
tours = permutations(all_cities[1:]) # exclude the depot initially

best_tour = None
min_max_distance = float('inf')
total_cost_best_tour = 0

for tour in tours:
    current_tour = [0] + list(tour) + [0]  # start and end at depot
    total_cost = 0
    max_distance = 0

    # Calculate total cost and max distance for the current tour
    for i in range(len(current_tour) - 1):
        dist = distance(cities_coordinates[current_tour[i]], cities_coordinates[current_tour[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    # Update best tour if current has a smaller max distance
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = current_tour
        total_cost_best_tour = total_cost

print("Tour:", best_tour)
print("Total travel cost:", round(total_cost_best_tour, 2))
print("Maximum distance between consecutive cities:", round(min_max_distance, 2))