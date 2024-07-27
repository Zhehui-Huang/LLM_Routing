import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates provided
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

# Define the tour and distances
tour = [0, 8, 5, 4, 7, 6, 3, 2, 1, 9, 0]
total_cost_provided = 416.8322265347456
max_distance_provided = 103.24727599312246

# Check Requirement 1
assert len(tour) == len(set(tour)) + 1 and tour[0] == tour[-1] == 0, "Tour does not visit every city exactly once or start/end at the depot"

# Check Requirement 2 & 3
calculated_total_cost = 0
calculated_max_distance = 0
for i in range(1, len(tour)):
    dist = euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
    calculated_total_cost += dist
    if dist > calculated_max_distance:
        calculated_max_distance = dist

assert abs(total_cost_provided - calculated_total_cost) < 1e-2, "Total travel cost is incorrect"
assert abs(max_distance_provided - calculated_max_distance) < 1e-2, "Max distance between consecutive cities is incorrect"

# Check if all tests pass
print("CORRECT")