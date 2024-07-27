import itertools
import math

# City coordinates (indexed by city number)
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84),
    3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78),
    9: (68, 14), 10: (51, 28), 11: (44, 79),
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Grouped cities
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i + 1])
    return total_distance

# Generate all combinations of one city per group
all_possible_selected_cities = itertools.product(*groups)

# Find the shortest tour
shortest_tour = None
shortest_tour_distance = float('inf')

for selected_cities in all_possible_selected_cities:
    # Create possible tours starting and ending at the depot (city 0)
    tours = [0] + list(selected_cities) + [0]
    tour_distance = calculate_total_distance(tours)
    
    # Update the shortest tour found
    if tour_distance < shortest_tour_distance:
        shortest_tour = tours
        shortest_tour_distance = tour_distance

# Output the results
print("Tour:", shortest_tour)
print("Total travel cost:", shortest_tour_distance)