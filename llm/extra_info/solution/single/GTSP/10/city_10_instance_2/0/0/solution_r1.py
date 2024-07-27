import math
import itertools

# Coordinates of the cities
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# City groups
city_groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(id1, id2):
    x1, y1 = cities[id1]
    x2, y2 = cities[id2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Precompute distances between all pairs of cities
distances = {}
for c1 in cities:
    for c2 in cities:
        distances[(c1, c2)] = euclidean_distance(c1, c2)

# Variable to store the minimum tour cost found
min_tour_cost = float('inf')
min_tour = []

# Utility to check if a tour includes exactly one from each group
def tour_visits_once(tour):
    visited_groups = set()
    for city in tour:
        for i, group in enumerate(city_groups):
            if city in group:
                visited_groups.add(i)
    return len(visited_groups) == len(city_groups)

# Iterate over all possible combinations of cities by selecting one city from each group
for combination in itertools.product(*city_groups):
    # Compute all possible routes starting and ending at the depot
    possible_routes = itertools.permutations(combination)  # Generate all permutations of chosen cities
    for route in possible_routes:
        # Calculate the tour cost for this route
        current_route = [0] + list(route) + [0]  # start and end at depot
        tour_cost = sum(distances[(current_route[i], current_route[i + 1])] for i in range(len(current_route) - 1))
        
        # Update the minimum tour cost and tour path
        if tour_visits_once(current_route) and tour_cost < min_tour_cost:
            min_tour_cost = tour_cost
            min_tour = current_route

# Print the result
print("Tour:", min_tour)
print("Total travel cost:", min_tour_cost)