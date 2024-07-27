import math

def calculate_distance(city_a, city_b):
    return math.sqrt(math.pow(city_a[0] - city_b[0], 2) + math.pow(city_a[1] - city_b[1], 2))

def test_robot_tour(tour, total_cost, max_distance):
    # Cities coordinates mapping as provided in the task
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }
    
    # [Requirement 1] Starts and ends at Depot (City 0) and visits all cities exactly once
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if sorted(tour) != sorted(list(cities.keys()) + [0]):
        return "FAIL"
    
    # Calculate total travel cost and maximum distance between consecutive cities
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # [Requirement 2] and [Requirement 3]
    calculated_total_cost = round(calculated_total_cost, 2)
    calculated_max_distance = round(calculated_max_distance, 2)
    
    if calculated_total_cost != total_cost:
        return "FAIL"
    if calculated_max_distance != max_distance:
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
total_travel_cost = 291.41
max_distance_between_cities = 56.61

# Run the unit test
result = test_robot_tour(tour, total_travel_cost, max_distance_between_cities)
print(result)