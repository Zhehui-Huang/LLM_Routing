import math
from itertools import permutations

# Defined cities coordinates
cities = {
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

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible tours starting and ending at the depot city 0
def generate_tours():
    city_indices = list(cities.keys())[1:]  # exclude the depot city index
    tours = permutations(city_indices)
    return [(0,) + tour + (0,) for tour in tours]

# Compute total distance of a given tour
def total_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Find the shortest tour among all possible tours
def shortest_tour():
    tours = generate_tours()
    shortest = min(tours, key=total_distance)
    min_distance = total_distance(shortest)
    return shortest, min_distance

# Get the shortest tour and display results
shortest, min_distance = shortest_tour()

# Output
print("Tour:", list(shortest))
print("Total travel cost:", round(min_distance, 2))