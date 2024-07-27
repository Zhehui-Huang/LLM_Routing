import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def validate_tour(cities, tour, reported_cost):
    # Check start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once (ignore the first and last because they should be the depot)
    if sorted(tour[1:-1]) != list(range(1, 20)):
        return "FAIL"
    
    # Calculate the total travel cost and compare with the reported cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_database[tour[i]][tour[i + 1]]
    
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Cities coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56),
    6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53),
    12: (11, 14), 13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49),
    17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Precompute Euclidean distances
euclidean_database = {}
for i in cities:
    euclidean_database[i] = {}
    for j in cities:
        euclidean_database[i][j] = euclidean_distance(cities[i], cities[j])

# Given solution
tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]
reported_cost = 478.4306776278287

# Validate the tour
result = validate_tour(cities, tour, reported_cost)
print(result)