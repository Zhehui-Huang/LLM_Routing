def calculate_distance(city1, city2):
    from math import sqrt
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tours_and_costs(robot_tours, cities_coordinates):
    # Constants
    number_of_cities = 23
    visited = [False] * number_of_cities
    
    # Verify each city is visited exactly once
    unique_cities = set()
    for tour in robot_tours:
        for city in tour:
            if city in unique_cities:
                return "FAIL"
            unique_cities.add(city)
            visited[city] = True

    # Verify every city is visited
    if not all(visited):
        return "FAIL"
    
    # Calculate and verify cost
    total_calculated_cost = 0
    for robot, tour_info in robot_tours.items():
        tour, reported_cost = tour_info['tour'], tour_info['cost']
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
        
        if not (abs(cost - reported_cost) < 1e-2):  # allowing minor floating point discrepancies
            return "FAIL"
        total_calculated_cost += cost
    
    if not (abs(total_calculated_cost - 306.61) < 1e-2):  # check if the overall total travel cost is correct
        return "FAIL"
    
    return "CORRECT"

# Coordinates of cities
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46),
    17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

robot_tours = {
    0: {'tour': [0, 21, 0, 15], 'cost': 34.31},
    1: {'tour': [0, 16, 7, 9], 'cost': 34.92},
    2: {'tour': [0, 6, 5, 14], 'cost': 33.33},
    3: {'tour': [0, 1, 12, 8], 'cost': 46.69},
    4: {'tour': [0, 20, 22, 17], 'loss': 33.39},
    5: {'tour': [0, 10, 3, 18], 'cost': 43.07},
    6: {'tour': [0, 2, 13, 19], 'cost': 51.67},
    7: {'tour': [0, 4, 11], 'cost': 29.23}
}

# Verify all requirements
result = verify_tours_and_costs(robot_tours, cities_coordinates)
print(result)