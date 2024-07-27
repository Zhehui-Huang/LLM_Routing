import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tours(robot_tours, depot_location):
    all_visited_cities = set()
    for tour in robot_tours:
        if tour[0] != depot_location or tour[-1] != depot_location:
            # Checking start and end at depot
            return False
        for city in tour[1:-1]:
            all_visited_cities.add(city)
    
    # Checking all cities are visited exactly once
    return all_visited_cities == set(range(1, 23))

def verify_total_distance(robot_tours, cities_coordinates):
    total_calculated_cost = 0
    for tour in robot_tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
        if abs(tour[2] - tour_cost) > 1e-6:  # considering a small precision error
            return False
        total_calculated_cost += tour_cost
    return total_calculated_cost

cities_coordinates = {(i): coord for i, coord in enumerate([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
])}

robot_tours = [
    [0, 1, 2, 3, 0], [0, 4, 5, 6, 0], [0, 7, 8, 9, 0], [0, 10, 11, 12, 0],
    [0, 13, 14, 15, 0], [0, 16, 17, 18, 0], [0, 19, 20, 21, 0], [0, 22, 0]
]

given_costs = [74.11646059928056, 82.67558617913956, 88.56825439021759, 85.40759495384788,
               126.91073486497025, 105.84447265732915, 98.24007188255551, 52.3450093132096]

predicted_cost = 714.1081848405502

if verify_tours(robot_tours, 0) and math.isclose(predicted_cost, verify_total_distance(robot_tours, cities_coordinates), abs_tol=1e-6):
    print("CORRECT")
else:
    print("FAIL")