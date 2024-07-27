import itertools
import math

def euclidean_distance(a, b):
    x1, y1 = cities[a]
    x2, y2 = cities[b]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

city_indices = list(cities.keys())
min_tour = None
min_cost = float('inf')

# Generate all combinations of 9 cities from the list of possible cities excluding the depot
for combination in itertools.combinations(city_indices[1:], 9):
    # Include the depot city at the start and end
    route = [0] + list(combination) + [0]

    # Check all permutations of the cities in the route (excluding the fixed depot start and end)
    for perm in itertools.permutations(route[1:-1]):
        possible_route = [route[0]] + list(perm) + [route[-1]]
        cost = sum(euclidean_distance(possible_route[i], possible_route[i+1]) for i in range(len(possible_route) - 1))
        
        if cost < min_cost:
            min_cost = cost
            min_tour = possible_route

# Display the tour and its total cost
print("Tour:", min_tour)
print("Total travel cost:", min_cost)