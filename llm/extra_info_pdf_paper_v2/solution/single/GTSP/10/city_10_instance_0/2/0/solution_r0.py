import itertools
import math

# City coordinates
city_coordinates = {
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

# City groups
groups = {
    0: [1, 2, 6],
    1: [3, 7, 8],
    2: [4, 5, 9]
}

def euclidean_distance(city1, city2):
    return math.sqrt((city_coordinates[city1][0] - city_coordinates[city2][0]) ** 2 + 
                     (city_coordinates[city1][1] - city_coordinates[city2][1]) ** 2)

# Compute all possible combinations of cities, one from each group
combinations = list(itertools.product(groups[0], groups[1], groups[2]))

# Function to get the total distance of a tour starting and ending at the depot city
def total_tour_distance(tour):
    total_distance = euclidean_distance(0, tour[0])  # start from depot
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i+1])
    total, # plus back to depot
distance += euclidean_distance(tour[-1], 0)
    return total_distance

# Searching for the shortest tour among all combinations
shortest_tour = None
shortest_distance = float('inf')

for combo in combinations:
    tour = (0,) + combo + (0,)
    distance = total_tour_distance(combo)
    if distance < shortest_distance:
        shortest_distance = distance
        shortest_tour = tour

# Output
print(f"Tour: {list(shortest_tour)}")
print(f"Total travel cost: {shortest_distance}")