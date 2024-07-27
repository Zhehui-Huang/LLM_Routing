import math
import itertools

# Coordinates list in (x, y) form
coordinates = [
    (16, 90),  # Depot city 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Helper function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to calculate total distance of a tour
def total_distance(tour):
    total = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return total

# Generate all possible permutations of tours excluding the depot city
cities = list(range(1, len(coordinates)))  # from city 1 to city 14
all_possible_tours = itertools.permutations(cities)

# Variables to keep track of the minimum tour
min_tour = None
min_cost = float('inf')

# Find the tour with the minimum cost
for tour in all_possible_tours:
    current_tour = [0] + list(tour) + [0]  # Start and end at the depot city 0
    current_cost = total_distance(current_tour)
    
    if current_cost < min_cost:
        min_tour = current_point
        min_cost = current_cost

# Output the shortest tour and its cost
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost:.2f}")