import math

# Coordinates of each city (indexed by city number)
coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Tour provided from the MILP Solver, all starting and potentially ending at Depot 0
robot_tours = [
    [0, 14, 16, 19, 21, 17, 20, 18, 15, 12, 10, 8, 6, 9, 7, 5, 2, 1, 3, 4, 11, 13, 0]
    # Additional robots tours would be listed here if applicable
]

# Total used to accumulate the cost checking
overall_travel_cost = 0

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Check each city is visited exactly once
visited_cities = set()
for tour in robot_tours:
    for city in tour:
        if city in visited_cities and city != 0:  # Depot can be visited multiple times as it's a starting/ending point
            print("FAIL - City visited more than once:", city)
            break
        visited_cities.add(city)

# Check if all cities are visited
if visited_cities != set(coordinates.keys()):
    print(f"FAIL - Not all cities are visited: missing {set(coordinates.keys()) - visited_cities}")
else:
    all_visited_once = True

# Check each tour's travel cost
for tour in robot_tours:
    tour_cost = 0
    for i in range(1, len(tour)):
        tour_cost += euclidean_distance(coordinates[tour[i - 1]], coordinates[tour[i]])
    overall_travel_cost += tour_cost

    # Each Robot should start at its designated depot
    if tour[0] != 0:
        print("FAIL - Robot does not start at the designated depot")

# If all checks are passed, print 'CORRECT'
if all_visited_once and visited_cities == set(coordinates.keys()):
    print("CORRECT")
    print("Total Travel Cost for All Robots:", overall_travel_cost)
else:
    print("FAIL")