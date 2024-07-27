import math

def calculate_distance(city_1, city_2):
    return math.sqrt((city_1[0] - city_2[0])**2 + (city_1[1] - city_2[1])**2)

def verify_solution(tour, total_cost, max_consecutive_distance):
    # City coordinates
    cities = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49)
    }
    
    # Requirements
    if tour[0] != 0 or tour[-1] != 0:  # Requirement 1
        return "FAIL"
    
    if sorted(tour) != sorted(list(cities.keys()) + [0]):  # Requirement 2
        return "FAIL"

    calculated_total_cost = 0
    calculated_max_dst = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        distance = calculate_distance(cities[city_from], cities[city_to])
        calculated_total_cost += distance
        if distance > calculated_max_dst:
            calculated_max_dst = distance

    if abs(calculated_total_cost - total_cost) > 0.01:  # Requirement 5
        return "FAIL"

    if abs(calculated_max_dst - max_consecutive_distance) > 0.01:  # Requirement 6
        return "FAIL"
    
    return "CORRECT"

tour = [0, 5, 9, 4, 8, 3, 2, 6, 7, 1, 0]
total_cost = 295.99
max_distance = 56.46

result = verify_solution(tour, total_cost, max_distance)
print(result)