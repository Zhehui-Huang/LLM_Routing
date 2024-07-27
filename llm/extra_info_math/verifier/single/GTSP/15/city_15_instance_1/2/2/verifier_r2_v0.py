import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# City coordinates with city index as keys
city_coordinates = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20),
    4: (18, 61), 5: (40, 57), 6: (57, 30), 7: (36, 12),
    8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
    12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# City groups
city_groups = {
    0: [1, 2, 5, 6],
    1: [8, 9, 10, 13],
    2: [3, 4, 7],
    3: [11, 12, 14]
}

# Tour result from the given solution
tour = [0, 4, 10, 0]
reported_total_travel_cost = 55.47239810610955

# Check if the tour starts and ends at the depot
requirement_1 = tour[0] == 0 and tour[-1] == 0

# Check if exactly one city from each group is visited
visited_groups = [next(key for key, value in city_groups.items() if city in value) for city in tour if city != 0]
requirement_2 = len(set(visited_groups)) == len(city_groups) and len(visited_groups) == len(set(visited_groups))

# Calculate the travel cost and check against the reported cost
calculated_total_travel_cost = sum(euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]]) for i in range(len(tour) - 1))
requirement_3 = math.isclose(reported_total_travel_cost, calculated_total_travel_cost, rel_tol=1e-9)

# Output result based on the requirements
if requirement_1 and requirement_2 and requirement_3:
    print("CORRECT")
else:
    print("FAIL")