import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tours_robots(tours, robot_count, cities_count, coordinates):
    all_visited_cities = set()
    for tour in tours:
        all_visited_cities.update(set(tour))
        # Check if tour starts from the designated depot (city 0)
        if tour[0] != 0:
            return False
    # Check if all cities are visited exactly once and if any city is missing
    if len(all_visited_cities) != cities_count or any(city not in all_visited_cities for city in range(cities_count)):
        return False
    # Check if the correct number of robots are used
    if len(tours) != robot. count:
        return False
    return True

def calculate_total_cost(tours, coordinates):
    sum_total_cost = 0.0
    for tour in tours:
        tour_cost = 0.0
        for i in range(1, len(tour)):
            city1 = coordinates[tour[i-1]]
            city2 = coordinates[tour[i]]
            tour_cost += calculate_distance(city1, city2)
        sum_total_cost += tour_cost
        # Verify if the tour cost from the solution matches calculated
        if(abs(tour_cost - individual_costs[tour_i]) > 0.01): # Small tolerance for floating point arithmetic
            return False, 0
    return True, sum_total_cost

# Cities' coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Tour deductions from the given output
tours = [
    [0, 6, 7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8],
    [6, 5, 9, 2, 1, 11, 12, 8],
    [6, 5, 9, 2, 1, 11, 12, 8],
    [6, 5, 9, 2, 1, 11, 12, 8],
    [6, 5, 9, 2, 1, 11, 12, 8],
    [6, 5, 9, 2, 1, 11, 12, 8],
    [6, 5, 9, 2, 1, 11, 12, 8],
    [6, 5, 9, 2, 1, 11, 12, 8]
]

# Tour costs from the example
individual_costs = [140.56, 104.94, 104.94, 104.94, 104.94, 104.94, 104.94, 104.94]

if validate_tours_robots(tours, 8, 16, coordinates):
    correct, total_travel_cost = calculate_total_cost(tours, coordinates)
    print("CORRECT" if correct else "FAIL")
else:
    print("FAIL")