import math

# Define the cities, coordinates, demands, and the given tours and costs
cities = {
    0: (30, 40, 0),
    1: (37, 52, 19),
    2: (49, 43, 30),
    3: (52, 64, 16),
    4: (31, 62, 23),
    5: (52, 33, 11),
    6: (42, 41, 31),
    7: (52, 41, 15),
    8: (57, 58, 28),
    9: (62, 42, 14),
    10: (42, 57, 8),
    11: (27, 68, 7),
    12: (43, 67, 14),
    13: (58, 27, 19),
    14: (37, 69, 11),
    15: (61, 33, 26),
    16: (62, 63, 17),
    17: (63, 69, 6),
    18: (45, 35, 15)
}
robot_tours = [
    [0, 16, 17, 8, 3, 13, 15, 9, 12, 14, 11, 0],
    [0, 5, 7, 4, 10, 2, 18, 1, 6, 0]
]
robot_capacity = 160
test_results = []

# Helper function to calculate the euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Test each robot's tour
for tour in robot_tours:
    # Check if each tour starts and ends at the depot (Requirement 1)
    if tour[0] == 0 and tour[-1] == 0:
        test_results.append("PASS")
    else:
        test_results.append("FAIL")
    
    # Check if the total demand serviced by each robot does not exceed its capacity (Requirement 3)
    total_demand = sum(cities[stop][2] for stop in tour[1:-1])
    if total_demand <= robot_capacity:
        test_results.append("PASS")
    else:
        test_results.append("FAIL")
    
    # Check if every city (except the depot) is visited exactly once (Requirement 5)
    city_visit_count = {i: 0 for i in range(1, 19)}
    for stop in tour[1:-1]:
        city_visit_count[stop] += 1
    if all(count == 1 for count in city_visit_count.values()):
        test_results.append("PASS")
    else:
        test_results.append("FAIL")

# Combining results for final assertion
if all(result == "PASS" for result in testetrics_results):
    print("CORRECT")
else:
    print("FAIL")