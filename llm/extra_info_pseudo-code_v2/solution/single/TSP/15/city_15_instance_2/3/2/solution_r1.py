import math
from itertools import permutations

# City coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# All possible tours starting and ending at depot city 0
all_tours = permutations(range(1, 15))

def calculate_total_distance(tour):
    total_distance = calc_distance(0, tour[0])  # from depot to first city
    for i in range(1, len(tour)):
        total_distance += calc_distance(tour[i-1], tour[i])  # between cities in the tour
    total_distance += calc_distance(tour[-1], 0)  # from last city back to depot
    return total_distance

# Finding the shortest tour
shortest_tour = None
min_distance = float('inf')
for tour in all_tours:
    current_distance = calculate_total_distance(tour)
    if current_distance < min_distance:
        min_distance = current_distance
        shortest_tour = tour

# Format the tour to start and end at the depot
shortest_tour = [0] + list(shortest_tour) + [0]

# Print results
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {min_distance:.2f}")