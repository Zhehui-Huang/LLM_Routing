import math
from itertools import permutations

# Cities coordinates with indices corresponding to city numbers
cities = {
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

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate the total travel cost of a tour
def calculate_total_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate all possible tours excluding the depot city at the start
all_possible_tours = permutations([key for key in cities if key != 0])

# Initialize the shortest tour and its cost
shortest_tour = None
shortest_tour_cost = float('inf')

# Evaluate each tour and find the shortest one
for tour in all_possible_tours:
    # Include the depot city as the start and end of the tour
    complete_tour = (0,) + tour + (0,)
    current_cost = calculate_total_distance(complete_tour)
    if current_cost < shortest_tour_cost:
        shortest_tour = complete_tour
        shortest_tour_cost = current_cost

# Output the results
print(f"Tour: {list(shortest_tour)}")
print(f"Total travel cost: {shortest_tour_cost}")