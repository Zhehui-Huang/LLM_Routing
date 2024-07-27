import itertools
import math

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# City groups
city_groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], 
    [2, 4, 14], [10, 17], [7, 15]
]

# Compute Euclidean distance between pairs of cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

memoized_distances = {}
for i in cities.keys():
    for j in cities.keys():
        memoized_distances[(i, j)] = euclidean_distance(i, j)

# Enumerate all routes through exactly one city in each group
def find_min_route():
    min_distance = float('inf')
    best_route = None

    for selected_cities in itertools.product(*city_groups):
        # All permutations of selected cities including the return to the depot
        for perm in itertools.permutations(selected_cities):
            route = [0] + list(perm) + [0]
            distance = sum(memoized_distances[(route[i], route[i+1])] for i in range(len(route) - 1))
            
            if distance < min_distance:
                min_distance = distance
                best_route = route

    return best_route, min_distance

# Finding the best route and total minimum distance
route, total_cost = find_min_route()

print("Tour:", route)
print("Total travel cost:", total_cost)