import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Given city coordinates
cities = {
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
    18: (45, 35)
}

# Solution details
turns = {
    0: [0, 0],
    1: [0, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
}

# Testing Requirements 
def test_solution(turns):
    # Ensure each city is visited exactly once
    visited_cities = set()
    leave_depot_0 = 0
    leave_depot_1 = 0
    
    for robot, tour in turns.items():
        if tour[0] == 0:
            leave_depot_0 += 1
        elif tour[0] == 1:
            leave_depot_1 += 1

        for i in range(len(tour) - 1):
            start = tour[i]
            end = tour[i + 1]

            if start in cities and start != end:
                visited_cities.add(start)
    
    all_visited_once = len(visited_cities) == len(cities) - 1  # minus one for double depots
    correct_departure_from_depot_0 = (leave_depot_0 == 1)
    correct_departure_from_depot_1 = (leave_depot_1 == 1)
    
    # Calculate total travel cost
    total_cost = 0
    for robot, tour in turns.items():
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        if tour_cost != 0:  # As given by the solution
            return "FAIL"
            
    if all_visited_once and correct_departure_from_depot_0 and correct_departure_from_depot_1:
        return "CORRECT"
    else:
        return "FAIL"

# Execute Unit Test
test_result = test_solution(turns)
print(test_result)