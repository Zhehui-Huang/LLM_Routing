import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

cities_coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35),
}

def is_tour_correct(tour, depot):
    return tour[0] == depot and tour[-1] == depot and len(set(tour)) == len(cities_coordinates)+1

def total_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        cost += calculate_distance(cities_coordinates[city1], cities_coordinates[city2])
    return round(cost, 2)

# Tours and costs from the solution
robot0_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13, 8, 16, 17, 3, 12, 14, 4, 11, 10, 1, 0]
robot0_cost = 194.50

robot1_tour = [1, 10, 12, 14, 4, 11, 3, 8, 16, 17, 9, 15, 13, 5, 18, 6, 2, 7, 0, 1]
robot1_cost = 198.21

# Test 1: Each robot must visit all cities exactly once, collectively.
all_cities = set(range(19))
visited_cities_robot0 = set(robot0_tour)
visited_cities_robot1 = set(robot1_tour)

# Calculating correctness of overall visiting scheme
correct_visit = (visited_cities_robot0.union(visited_cities_robot1) == all_cities)

# Test 2: Tours should respect depot start/end constraint
correct_robot0_tour = is_tour_correct(robot0_tour, 0)
correct_robot1_tour = is_tour_correct(robot1_tour, 1)

# Test 3: Calculated total travel costs for verification
calculated_robot0_cost = total_cost(robot0_tour)
calculated_robot1_cost = total_cost(robot1_tour)
correct_robot0_cost = math.isclose(robot0_cost, calculated_robot0_cost, rel_tol=0.01)
correct_robot1_cost = math.isclose(robot1_cost, calculated_robot1_cost, rel_tol=0.01)

# Overall evaluation
if (correct_visit and correct_robot0_tour and correct_robot1_tour and
    correct_robot0_cost and correct_robot1_cost):
    print("CORRECT")
else:
    print("FAIL")