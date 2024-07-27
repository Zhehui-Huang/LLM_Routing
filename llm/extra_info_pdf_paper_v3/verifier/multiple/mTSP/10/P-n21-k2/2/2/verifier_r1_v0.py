import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def calculate_tour_cost(tour, cities):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return cost

def verify_tours(tours, num_cities):
    visited_cities = set()
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return False
        visited_cities.update(tour)
    
    if len(visited_cities) != num_cities:
        return False

    return 0 not in visited_cities

def verify_and_calculate_cost():
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
    
    robot0_tour = [0, 1, 3, 4, 15, 12, 11, 10, 8, 18, 19, 0]
    robot1_tour = [0, 2, 5, 14, 13, 9, 7, 6, 16, 17, 20, 0]
    
    tours = [robot0_tour, robot1_tour]
    
    if not verify_tours(tours, len(cities)):
        return "FAIL"
    
    total_cost = 0
    correct_costs = [176.49212636224084, 158.80759384613344]

    for i, tour in enumerate(tours):
        tour_cost = calculate_tour_cost(tour, cities)
        if abs(tour_cost - correct_costs[i]) > 1e-4:  # Considering a tiny precision error margin
            return "FAIL"
        total_cost += tour_cost
    
    overall_cost = 335.2997202083743
    if abs(total_cost - overall_cost) > 1e-4:
        return "FAIL"
    
    return "CORRECT"

# Run the verification
result = verify_and_calculate_cost()
print(result)