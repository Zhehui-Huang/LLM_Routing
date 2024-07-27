import itertools
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# City coordinates
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69), 
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}

# City groups
groups = [
    [1, 2, 6],
    [3, 7, 8],
    [4, 5, 9]
]

# Generate all combinations of cities from each group
combinations = list(itertools.product(*groups))

# Initialize the minimum distance to a very high value and no route
min_distance = float('inf')
optimal_route = None

# Calculate all possible routes and find the one with the smallest distance
for combination in combinations:
    # Start from depot, visit one city from each group, and return to depot
    routes = [0] + list(combination) + [0]
    
    # Calculate the total distance for this route
    distance = 0
    for i in range(len(routes) - 1):
        distance += euclidean_distance(cities[routes[i]], cities[routes[i+1]])

    # If current distance is less than the known minimum, update minimum and save route
    if distance < min_distance:
        min_distance = distance
        optimal_route = routes

# Output the optimal route and minimum distance
print("Tour:", optimal_route)
print("Total travel cost:", min_distance)