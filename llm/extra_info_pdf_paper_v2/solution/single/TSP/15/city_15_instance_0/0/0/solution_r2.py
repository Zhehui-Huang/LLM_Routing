import math
from itertools import permutations

# Define the coordinates of the cities
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50),
    4: (21, 23), 5: (88, 59), 6: (79, 77), 7: (63, 23),
    8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def calc_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_shortest_tour():
    """Find the shortest possible tour that visits all cities and returns to the start."""
    city_indices = list(cities.keys())[1:]
    min_distance = float('inf')
    best_tour = None

    # Checking all permutations of city indices
    for perm in permutations(city_indices):
        # Calculate distance including returning to the start
        distance = calc_distance(0, perm[0]) + calc_distance(perm[-1], 0)
        for i in range(len(perm) - 1):
            distance += calc_distance(perm[i], perm[i + 1])

        # Update the best tour found
        if distance < min_distance:
            min_distance = distance
            best_tour = perm

    # Format the best tour to start and end at the depot
    best_tour = [0] + list(best_tour) + [0]
    return best_tour, min_distance

# Execute the function
tour, total_cost = find_shortest_tour()

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")