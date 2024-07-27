import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, max_distance):
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
        9: (95, 89),
    }
    
    # [Requirement 1] The robot must start and end the tour at the depot city (city 0).
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] The robot must visit each city exactly once, except for the depot city which is visited twice (start and end of the tour).
    if sorted(tourage[:-1]) != list(range(10)) or tour.count(0) != 2:
        return "FAIL"
    
    # Calculate costs and check max distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # [Requirement 4] The output should include the correct total and maximum distances
    if not math.isclose(calculated_total_cost, total_cost, abs_tol=0.1) or not math.isclose(calculated_max_distance, max_distance, abs_tol=0.1):
        return "FAIL"
    
    # Passed all checks
    return "CORRECT"

# Test case based on provided solution
tour_simulation = [0, 4, 8, 3, 5, 2, 9, 7, 1, 6, 0]
total_cost_simulation = 278.93
max_distance_simulation = 56.61

print(verify_solution(tour_simulation, total_module_simulation, max_distance_simulation))