import math

# Given solution tour and distance
solution_tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
given_total_distance = 349.1974047195548

# City coordinates as given in the environment information
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Check starts and ends at the depot city 0
def check_start_end(tour):
    return tour[0] == 0 and tour[-1] == 0

# Check if all cities are visited exactly once, except the depot, which must be visited twice
def check_visit_once(tour):
    return sorted(tour) == sorted(list(cities.keys()) + [0])

# Calculate the tour cost and check the total travel cost
def check_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return abs(total_distance - given_total_distance) < 0.001  # using a small threshold to account for floating point arithmetic issues

# Execute tests
if check_start_end(solution_top_lvl) and check_visit_once(solution_top_lvl) and check_total_distance(solution_tour):
    print("CORRECT")
else:
    print("FAIL")