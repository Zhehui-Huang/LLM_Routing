import math

# Define the cities and their positions
positions = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43),
    18: (53, 76), 19: (19, 72)
}

# City groups
groups = [
    [4, 10, 13, 17],  # Group 0
    [6, 7, 14],       # Group 1
    [9, 12, 16],      # Group 2
    [2, 5, 15],       # Group 3
    [1, 3, 19],       # Group 4
    [8, 11, 18]       # Group 5
]

# Calculate distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((positions[city1][0] - positions[city2][0])**2 + 
                     (positions[city1][1] - positions[city2][1])**2)

# Provided solution
tour = [0, 3, 0]
total_travel_cost = 97.94033679461242

# Verify Requirement 1: The tour must start and end at the depot city 0.
requirement1 = tour[0] == 0 and tour[-1] == 0

# Verify Requirement 2: The robot must visit exactly one city from each group.
visited_groups = set()
for city in tour:
    for index, group in enumerate(groups):
        if city in group:
            visited_groups.add(index)
requirement2 = len(visited_groups) == len(groups)

# Verify Requirement 3: Minimize the travel cost.
# Calculate the estimated tour cost
calculated_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
requirement3 = math.isclose(total_travel_cost, calculated_cost, rel_tol=1e-5)

# Outputting the test result
if requirement1 and requirement2 and requirement3:
    print("CORRECT")
else:
    print("FAIL")