import math
from itertools import permutations

# Helper Functions
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define city coordinates
cities = {0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69), 
          5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)}

# Extract only the coordinates
positions = list(cities.values())

# Calculating all Permutations of Cities Excluding the Depot
city_indices = list(cities.keys())[1:]  # [1, 2, ..., 9]
tours = permutations(city_indices)

best_tour = None
min_max_distance = float('inf')
full_tour = None

# Determine Best Tour Minimizing Max Distance Between Consecutive Cities
for tour in tours:
    current_tour = [0] + list(tour) + [0]  # Starting and ending at the depot
    max_distance = 0
    total_travel_cost = 0
    
    # Calculate the maximum distance and total travel cost of this tour
    for i in range(len(current_tour) - 1):
        distance = euclidean_distance(positions[current_tour[i]], positions[current_tour[i+1]])
        total_travel cost += distance
        if distance > max_distance:
            max_distance = distance
    
    # Check if this tour has a smaller maximal distance than the current best
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = current_tour
        best_total_travel_cost = total_travel_cost

# Output the best tour, total travel cost, and maximum distance
print("Tour:", best_tour)
print("Total travel cost:", best_total_travel_cost)
print("Maximum distance between consecutive cities:", min_max_distance)