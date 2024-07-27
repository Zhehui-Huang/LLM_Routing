import math

# Representing the tour and travel costs as provided in the solution
robot0_tour = [11, 1, 4, 8, 9, 13, 12, 15]
robot0_cost = 111.34190828906098

robot1_tour = [0, 16, 14, 17, 2, 19, 18, 3, 10, 5, 7, 6, 20]
robot1_cost = 167.7549413118864

overall_cost_provided = 279.0968496009474

# Cities and their coordinates
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
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

def check_requirements():
    # Check that each city is visited exactly once
    all_visited_cities = set(robot0_tour + robot1_tour)
    if len(all_visited_cities) != 21 or any(city not in all_visited_cities for city in cities):
        return "FAIL"
    
    # Check starting conditions
    if robot0_tour[0] != 1 or robot1_tour[0] != 0:  # Start from designated depots
        return "FAIL"
    
    # Check if there are no returns to the depots after the last city
    if robot0_tour[-1] == 1 or robot1_tour[-1] == 0:
        return "FAIL"

    # Check computed travel costs
    computed_robot0_cost = calculate_tour_cost(robot0_tour)
    computed_robot1_cost = calculate_tour_cost(robot1_tour)
    total_computed_cost = computed_robot0_cost + computed_robot1_cost
    
    if abs(computed_robot0_cost - robot0_cost) > 0.01 or abs(computed_robot1_cost - robot1_cost) > 0.01:
        return "FAIL"
    
    if abs(total_computed_cost - overall_cost_provided) > 0.01:
        return "FAIL"
    
    return "CORRECT"

# Perform checks and output result
result = check_requirements()
print(result)