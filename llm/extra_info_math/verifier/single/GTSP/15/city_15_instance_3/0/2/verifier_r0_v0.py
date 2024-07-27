import math

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinate data for the depot and cities
coordinates = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Groups representing each cluster. Each group must have one city visited.
groups = {
    0: [1, 6, 14], 1: [5, 12, 13], 2: [7, 10], 3: [4, 11], 4: [2, 8], 5: [3, 9]
}

# Solution provided
tour = [0, 14, 0]
total_travel_cost_provided = 50.99019513592785

# Verify Requirement 1: Starts and ends at the depot (index 0)
req1 = tour[0] == 0 and tour[-1] == 0

# Verify Requirement 2: Visits exactly one city from each group
visited = set(tour[1:-1])  # ignore the first and last element which is the depot
req2 = all(len(visited.intersection(group)) == 1 for group in groups.values())

# Verify Requirement 3: Total travel cost
calculated_cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
req3 = abs(calculated_cost - total_travel_cost_provided) <= 1e-6  # consider small floating point errors

# Check all requirements
if req1 and req2 and req3:
    print("CORRECT")
else:
    print("FAIL")