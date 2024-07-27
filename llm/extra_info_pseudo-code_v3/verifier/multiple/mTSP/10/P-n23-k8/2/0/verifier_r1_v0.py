import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def verify_solution(tours, num_cities):
    visited_cities = set()
    overall_cost = 0
    
    city_coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
        (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
        (45, 35), (32, 39), (56, 37)
    ]
    
    expected_costs = [
        74.11646059928056, 82.67558617913954, 81.28560726008224, 75.05000289034454, 
        126.91073486497025, 105.84447265732915, 98.21392169716218, 52.491761791689186
    ]
    
    if len(tours) != 8:
        return "FAIL"

    for i, tour in enumerate(tours):
        last_city = 0  # starting from depot
        tour_cost = 0
        for city in tour[1:-1]:  # skip first and last as they are depot
            if city < 1 or city >= num_cities:
                return "FAIL"
            visited_cities.add(city)
            # Compute distance from last city to current city
            x1, y1 = city_coordinates[last_city]
            x2, y2 = city_coordinates[city]
            distance = calculate_euclidean_distance(x1, y1, x2, y2)
            tour_cost += distance
            last_city = city
        
        # Return to depot from last visited city
        x1, y1 = city_coordinates[last_city]
        x2, y2 = city_coordinates[0]
        tour_cost += calculate_euclidean_distance(x1, y1, x2, y2)
        # Check if the tour cost is as expected (allowing minor floating-point discrepancies)
        if not math.isclose(tour_cost, expected_costs[i], rel_tol=1e-6):
            return "FAIL"
        overall_cost += tour_cost
    
    # Check if all cities are visited
    if len(visited_cities) != num_cities - 1:
        return "FAIL"

    # Sum of expected_costs
    if not math.isclose(overall_cost, 696.5885479399977, rel_tol=1e-6):
        return "FAIL"
    
    return "CORRECT"

# Define the tours based on the user's last message. Mapping city indices correctly.
tours = [
    [0, 1, 2, 3, 0],
    [0, 6, 5, 4, 0],
    [0, 7, 9, 8, 0],
    [0, 10, 12, 11, 0],
    [0, 13, 14, 15, 0],
    [0, 16, 17, 18, 0],
    [0, 20, 19, 0],
    [0, 21, 22, 0]
]

print(verify_solution(tours, 23))