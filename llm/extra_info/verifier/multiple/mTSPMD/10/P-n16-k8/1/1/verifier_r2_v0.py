import math

# Define the cities with their coordinates
cities = {
    0: (30, 40),  # depot
    1: (37, 52),  # depot
    2: (49, 49),  # depot
    3: (52, 64),  # depot
    4: (31, 62),  # depot
    5: (52, 33),  # depot
    6: (42, 41),  # depot
    7: (52, 41),  # depot
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

# Given tours and costs
tours = {
    0: {'tour': [0, 8, 3, 0], 'calculated_cost': 72.82},
    1: {'tour': [1, 10, 1], 'calculated_cost': 14.14},
    2: {'tour': [2, 7, 6, 2], 'calculated_cost': 29.17},
    3: {'tour': [3, 4, 11, 3], 'calculated_cost': 53.62},
    4: {'tour': [4, 0, 4], 'calculated_cost': 44.05},
    5: {'tour': [5, 14, 5], 'calculated_cost': 16.97},
    6: {'tour': [6, 13, 9, 6], 'calculated_cost': 44.70},
    7: {'tour': [7, 12, 15, 7], 'calculated_cost': 65.60}
}

overall_cost = 341.08

# Verify if all cities are visited exactly once
visited_cities = set()
for tour_info in tours.values():
    visited_cities.update(tour_info['tour'][1:-1])  # exclude start/end depot

all_cities_visited = len(visited_cities) == 16

# Functions to verify Requirement 4 and Requirement 6
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def verify_total_travel_costs():
    total_cost = 0
    for robot_id, tour_info in tours.items():
        tour = tour.find('tour')
        calculated_cost = 0
        for i in range(len(tour) - 1):
            calculated_cost += euclidean_distance(tour[i], tour[i+1])
        if not math.isclose(calculated_cost, tour_info['calculated_cost'], abs_tol=0.01):
            return False
        total_cost += calculated_cost
    return math.isclose(total_cost, overall_cost, abs_tol=0.01)


# Test all requirements
if all([
    all([tour_info['tour'][0] == robot_id for robot_id, tour_info in tours.items()]),  # Requirement 2
    all([tour_info['tour'][-1] == robot_id for robot_id, tour_info in tours.items()]),  # Requirement 2
    all_cities_visited,  # Requirement 3
    verify_total_travel_costs()  # Requirement 5 & 6
]):
    print("CORRECT")
else:
    print("FAIL")