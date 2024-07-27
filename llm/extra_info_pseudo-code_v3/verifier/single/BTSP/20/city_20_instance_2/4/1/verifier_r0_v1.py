import math

def calculate_distance(city1, city2):
    return math.hypot(city1[0] - city2[0], city1[1] - city2[1])

def verify_solution(tour, total_cost, max_distance, city_coordinates):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city is visited exactly once
    if sorted(tour[:-1]) != sorted(list(range(1, len(city_coordinates)))):
        return "FAIL"

    # Calculate total travel cost and maximum distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(1, len(tour)):
        distance = calculate_distance(city_coordinates[tour[i-1]], city_coordinates[tour[i]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Check against provided total cost and maximum distance
    if not (abs(calculated_total_cost - total_cost) < 1e-6 and abs(calculated_max_distance - max_distance) < 1e-6):
        return "FAIL"

    return "CORRECT"

# City coordinates indexed by city number
city_coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92), 
    (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

# Provided tour and metrics
tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]
total_travel_cost = 478.4306776278287
maximum_distance_between_cities = 80.61017305526642

# Verification
result = verify_solution(tour, total_travel_cost, maximum_distance_between_cities, city_coordinates)
print(result)