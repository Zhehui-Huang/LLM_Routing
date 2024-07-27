import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def validate_solution(tours, costs, cities, overall_cost):
    visited_cities = set()
    calculated_overall_cost = 0
    
    if len(tours) != 8:
        return "FAIL"  # Check there are 8 robots

    city_coordinates = {
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
    }

    for tour, cost in zip(tours, costs):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Check if tour starts and ends at the depot

        tour_cost = 0
        for c1, c2 in zip(tour, tour[1:]):
            tour_cost += calculate_distance(*city_coordinates[c1], *city_coordinates[c2])

        if not math.isclose(tour_cost, cost, rel_tol=1e-5):
            return "FAIL"  # Check if the tour cost is calculated correctly
            
        visited_cities.update(tour[1:-1])
        
        calculated_overall_cost += cost

    if visited_cities != set(range(1, 16)):
        return "FAIL"  # Check if each city except depot is visited exactly once

    if not math.isclose(calculated_overall_cost, overall_cost, rel_tol=1e-5):
        return "FAIL"  # Check if the overall cost is calculated correctly

    return "CORRECT"

tours = [
    [0, 2, 11, 0],
    [0, 14, 9, 0],
    [0, 5, 12, 0],
    [0, 1, 8, 0],
    [0, 7, 13, 0],
    [0, 6, 15, 0],
    [0, 10, 3, 0],
    [0, 4, 0]
]

costs = [
    78.25293542978335,
    78.45731186088909,
    88.22445167891173,
    67.22301848644682,
    60.3626995599602,
    70.31738766580068,
    65.57284885461793,
    44.04543109109048
]

overall_cost = 552.4560846275003

result = validate_solution(tours, costs, 16, overall_cost)
print(result)