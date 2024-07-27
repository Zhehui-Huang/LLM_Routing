import itertools
import math

# City coordinates
cities = [
    (14, 77),  # City 0: Depot city
    (34, 20),  # City 1
    (19, 38),  # City 2
    (14, 91),  # City 3
    (68, 98),  # City 4
    (45, 84),  # City 5
    (4, 56),   # City 6
    (54, 82),  # City 7
    (37, 28),  # City 8
    (27, 45),  # City 9
    (90, 85),  # City 10
    (98, 76),  # City 11
    (6, 19),   # City 12
    (26, 29),  # City 13
    (21, 79),  # City 14
    (49, 23),  # City 15
    (78, 76),  # City 16
    (68, 45),  # City 17
    (50, 28),  # City 18
    (69, 9)    # City 19
]

# City groups
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Precompute distances
distances = {}
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        d = euclidean_distance(i, j)
        distances[(i, j)] = d
        distances[(j, i)] = d

def total_distance(tour):
    return sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

# Generate all tours that visit one city from each group and start and end at the depot
possible_tours = []
for cities_in_group in itertools.product(*groups):
    tour = [0] + list(cities_in_group) + [0]
    possible_tours.append(tour)

# Find the tour with the minimum distance
shortest_tour = min(possible_tours, key=total_distance)
shortest_distance = total_distance(shortest_tour)

print("Tour:", shortest_tour)
print("Total travel cost:", shortest_distance)