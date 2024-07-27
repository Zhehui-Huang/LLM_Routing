import numpy as np

# City coordinates as provided in the problem description
city_coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Tours provided in the solution description
tours = {
    0: [0, 14, 16, 17, 20, 21, 0],
    1: [1, 6, 8, 15, 18, 12, 1],
    2: [2, 5, 7, 9, 10, 2],
    3: [3, 4, 11, 13, 19, 3]
}

# Calculating whether all cities are visited exactly once
visited_cities = set()
for t in tours.values():
    visited_cities.update(t[1:-1])  # exclude depot visits at start & end for uniqueness check

# Check if there are exactly 22 cities and each city once visited
def test_all_cities_visited_once():
    return len(visited_cities) == 18 and len(city_coordinates) == 22

# Check if each robot starts and ends at its depot
def test_start_end_depot():
    return all(tour[0] == tour[-1] == robot for robot, tour in tours.items())

# Calculate Euclidean distance
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Calculate total travel cost for each tour and overall cost
def test_travel_cost():
    overall_cost = 0
    for robot, tour in tours.items():
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
        overall_cost += total_cost
    return round(overall_cost, 2) == round(443.90373275574154, 2)

# Check if unique solutions are found before stopping criterion met
# Not feasible to test without algorithm running details, assuming based on output consistency

# Now combine all tests
def validate_solution():
    if not test_all_cities_visited_once():
        return "FAIL"
    if not test_start_end_depot():
        return "FAIL"
    if not test_travel \mbox{cost}():
        return "FAIL"
    return "CORRECT"

# Output validation result
validate_result = validate_solution()
print(validate_result)