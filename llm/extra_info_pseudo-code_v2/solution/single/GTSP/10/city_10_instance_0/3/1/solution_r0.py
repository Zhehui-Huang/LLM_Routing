import itertools
import math

# City coordinates as given
cities = {
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

def get_distance(city1, city2):
    # Euclidean distance between two cities
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Grouping of cities
city_groups = {
    0: [1, 2, 6],
    1: [3, 7, 8],
    2: [4, 5, 9]
}

# Generate all combinations of cities where one city is taken from each group
all_possible_tours = list(itertools.product(city_groups[0], city_groups[1], city_groups[2]))

# Find the shortest tour
min_distance = float('inf')
best_tour = None
for tour in all_possible_tours:
    # Calculate the distance of the path that includes the depot both at the start and the end
    distance = get_distance(0, tour[0]) + get_distance(tour[0], tour[1]) + get_distance(tour[1], tour[2]) + get_distance(tour[2], 0)
    if distance < min_distance:
        min_distance = distance
        best_tour = tour

# Include the depot city at the start and the end
final_tour = [0] + list(best_tour) + [0]

# Output
print("Tour:", final_tour)
print("Total travel cost:", min_distance)