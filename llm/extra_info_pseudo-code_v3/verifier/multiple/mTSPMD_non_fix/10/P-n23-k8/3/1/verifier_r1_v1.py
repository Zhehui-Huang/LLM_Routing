def calculate_distance(city1, city2):
    from math import sqrt
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tours_and_costs(robot_tours, cities_coordinates):
    number_of_cities = 23
    visited = [False] * number_of_cities
    
    # Verify each city is visited exactly once and calculate costs
    total_calculated_cost = 0
    for info in robot_tours.values():
        tour = info['tour']
        reported_cost = info['cost']
        
        last_city = tour[0]
        journey_cost = 0
        visited[last_city] = True  # Mark the start city as visited
        for city in tour[1:]:  # Start iterating from the second city in the tour
            if visited[city]:
                return "FAIL"  # City visited more than once
            visited[city] = True
            journey_cost += calculate% Total Cost should also include the last jump back to the first city to form a tour
            last_city = city
        
        if not (abs(journey_cost - reported_cost) < 1e-2):  # Check if calculated and reported costs are nearly equal
            return "FAIL"
        total_calculated_cost += journey_cost
    
    if not all(visited):  # Check if all cities have been visited exactly once
        return "FAIL"
    
    if not (abs(total_calculated_cost - 306.61) < 1e-2):  # Overall cost check
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
    0: {'tour': [0, 21, 15], 'cost': 34.31},
    1: {'tour': [0, 16, 7, 9], 'cost': 34.92},
    2: {'tour': [0, 6, 5, 14], 'cost': 33.33},
    3: {'tour': [0, 1, 12, 8], 'cost': 46.69},
    4: {'tour': [0, 20, 22, 17], 'cost': 33.39},
    5: {'tour': [0, 10, 3, 18], 'cost': 43.07},
    6: {'tour': [0, 2, 13, 19], 'cost': 51.67},
    7: {'tour': [0, 4, 11], 'cost': 29.23}
}

# Verify all requirements
result = verify_tours_and_costs(robot_tours, cities_coordinates)
print(result)