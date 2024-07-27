import math

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

# Provided solution
robots = {
    0: {'tour': [0, 8, 0], 'cost': 64.89992295835181},
    1: {'tour': [1, 9, 1], 'cost': 53.85164807134504},
    2: {'tour': [2, 10, 2], 'cost': 21.2602916254693},
    3: {'tour': [3, 11, 3], 'cost': 50.635955604688654},
    4: {'tour': [4, 12, 4], 'cost': 26.0},
    5: {'tour': [5, 13, 5], 'cost': 32.31098884280702},
    6: {'tour': [6, 14, 6], 'cost': 42.5205832509386},
    7: {'tour': [7, 15, 7], 'cost': 63.52952069707436}
}

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_solution(robots, cities):
    all_cities_visited = set()
    overall_cost_calculated = 0.0

    for robot, details in robots.items():
        tour = details['tour']
        reported_cost = details['cost']
        calculated_cost = 0.0
        
        # Check start and end at the depot
        if tour[0] != robot or tour[-1] != robot:
            return "FAIL"
        
        # Calculate the travel cost
        for i in range(len(tour) - 1):
            leg_cost = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
            calculated_cost += leg_cost
        
        # Check cost calculation and rounding issues within a reasonable tolerance
        if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-3):
            return "FAIL"
        
        overall_cost_calculated += reported_cost
        all_cities_visited.update(tour)

    # Check if all cities are visited exactly once except depots
    if len(all_cities_visited) != len(cities):
        return "FAIL"

    # Check overall cost
    if not math.isclose(overall_cost_calculated, 355.0089110506748, rel_tol=1e-3):
        return "FAIL"

    return "CORRECT"

# Run the validation
result = verify_solution(robots, cities)
print(result)