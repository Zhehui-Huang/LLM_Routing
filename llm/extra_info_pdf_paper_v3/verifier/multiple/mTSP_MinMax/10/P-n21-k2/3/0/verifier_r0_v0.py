import math

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def check_solution(tours, coordinates, num_cities=21):
    # Total count of cities including the depot
    all_cities_visited = set()
    
    # Track unique city visits and compute travel costs
    max_travel_cost = 0
    for tour in tours:
        city_sequence = tour['tour']
        travel_cost = 0
        
        # Verify correct start and end at the depot
        if city_sequence[0] != 0 or city_sequence[-1] != 0:
            return "FAIL"
        
        previous_city = city_sequence[0]
        for city_index in city_sequence[1:]:
            travel_cost += euclidean_distance(coordinates[previous_city], coordinates[city_index])
            all_cities_visited.add(city_index)
            previous_city = city_index
        
        if tour['total_travel_cost'] - travel_cost > 1e-2:  # account for floating-point precision
            return "FAIL"
        
        if travel_cost > max_travel_cost:
            max_travel_cost = travel_cost
    
    # Check if all cities visited exactly once and all are included
    if len(all_cities_visited) != num_cities or any(city not in all_cities_visited for city in range(num_cities)):
        return "FAIL"
    
    # Validate maximum travel cost
    if abs(max(tour['total_travel_cost'] for tour in tours) - max_travel_cost) > 1e-2:
        return "FAIL"

    return "CORRECT"

# Coordinates of the cities
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Provided solution
solution_tours = [
    {"tour": [0, 20, 6, 2, 18, 19, 3, 12, 11, 4, 1, 0], "total_travel_cost": 128.7},
    {"tour": [0, 7, 5, 14, 17, 9, 13, 8, 15, 10, 16, 0], "total_travel_cost": 129.06}
]

# Execute the unit tests
print(check_solution(solution_tours, cities_coordinates))