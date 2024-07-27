import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost, max_distance, city_coordinates):
    # Requirement 1: Start and end at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Each city visited once, except depot city
    unique_visits = set(tour)
    if len(unique_visits) != len(city_coordinates) or tour.count(0) != 2:
        return "FAIL"

    # Check if other cities are visited exactly once
    for city in range(1, len(city_coordinates)):
        if tour.count(city) != 1:
            return "FAIL"

    # Calculate actual travel costs and max distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
        calculated_total_cost += distance
        if distance > calculated_max_di
            calculated_max_distance=distance

    # Requirement 1: Verify values
    if round(calculated_total_cost, 2) != round(total_travel_cost, 2) or \
       round(calculated_max_distance, 2) != round(max_distance, 2):
        return "FAIL"

    return "CORRECT"

# City coordinates as per the task
city_coordinates = [
    (14, 77),  # City 0
    (34, 20),  # City 1
    (19, 38),  # City 2
    (14, 91),  # City 3
    (68, 98),  # City 4
    (45, 84),  # City 5
    (4, 56),   # City 6
    (54, 82),  # City 7
    (37, 28),  # City 8
    (27, 45),  # City 9
    (90, 85),  # City 10
    (98, 76),  # City 11
    (6, 19),   # City 12
    (26, 29),  # City 13
    (21, 79),  # City 14
    (49, 23),  # City 15
    (78, 76),  # City 16
    (68, 45),  # City 17
    (50, 28),  # City 18
    (69, 9)    # City 19
]

# Presented solution
tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 6, 2, 9, 13, 8, 1, 15, 18, 17, 19, 12, 0]
total_travel_cost = 503.93
maximum_distance = 96.1

# Verify the solution
result = verify_solution(tour, total_travel_cost, maximum_distance, city_coordinates)
print(result)