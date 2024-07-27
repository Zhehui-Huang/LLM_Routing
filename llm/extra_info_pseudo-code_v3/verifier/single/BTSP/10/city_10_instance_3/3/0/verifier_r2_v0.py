import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, expected_total_cost, expected_max_distance):
    cities = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }
    
    # Check the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check each city is visited exactly once
    visited_cities = tour[:-1]  # Exclude the last city as it is the depot
    if len(set(visited_cities)) != len(cities):
        return "FAIL"
    
    # Calculate total travel cost and maximum distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    # Check if calculated cost and max distance match the expected results
    if not math.isclose(total_cost, expected_total_cost, abs_tol=0.01) or \
       not math.isclose(max_distance, expected_max_distance, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Provided solution details
tour_solution = [0, 1, 2, 4, 3, 9, 5, 6, 7, 8, 0]
total_travel_cost_solution = 379.34
max_distance_solution = 68.26

# Test the solution
result = verify_solution(tour_solution, total_travel_cost_solution, max_distance_solution)
print(result)