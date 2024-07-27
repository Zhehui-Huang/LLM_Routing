import math
import itertools

# City coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Robots and their tours
robot_tours = {
    0: [0, 3, 8, 0],
    1: [0, 4, 0],
    2: [0, 13, 12, 0],
    3: [0, 10, 0],
    4: [0, 1, 9, 0],
    5: [0, 11, 0],
    6: [0, 5, 6, 0],
    7: [0, 7, 15, 2, 14, 0]
}

# Verify if tours visit all cities exactly once and return to the depot
all_visited_cities = set()

for tour in robot_tours.values():
    if tour[0] != 0 or tour[-1] != 0:
        print("FAIL")
        break
    for city in tour[1:-1]:
        all_visited_cities.add(city)

# Check if all cities except the depot city are visited exactly once 
if all_visited_cities == set(range(1, 16)):
    print("CORRECT")
else:
    print("FAIL")

# Verify number of robots
if len(robot_tours) != 8:
    print("FAIL")

# Verify the travel cost and primary objective
max_cost = 0
for tour in robot_tours.values():
    tour_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    max_cost = max(max_cost, tour_cost)

# Verifying based on stated maximum cost
provided_max_travel_cost = 131.75171020233932
if math.isclose(max_cost, provided_max_travel_cost, rel_tol=1e-5):
    print("CORRECT")
else:
    print("FAIL")