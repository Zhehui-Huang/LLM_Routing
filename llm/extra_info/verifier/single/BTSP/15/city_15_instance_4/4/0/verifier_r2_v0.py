import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(tour, total_cost, max_distance):
    # Cities position map
    city_positions = {
        0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
        4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
        8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
        12: (53, 80), 13: (21, 21), 14: (12, 39)
    }
    
    # [Requirement 1] Check if all cities are visited exactly once and starts/ends at depot
    all_cities_visited_once = len(set(tour)) == len(city_positions) and len(tour) == len(city_positions) + 1
    starts_and_ends_at_depot = tour[0] == 0 and tour[-1] == 0
    
    # [Requirement 2] Tour must start and end at 0
    correct_tour_format = starts_and_ends_at_depot
    
    # Calculate the distances and total cost
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(city_positions[tour[i]], city_positions[tour[i + 1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
            
    # [Requirement 3] Verify total travel cost
    cost_is_correct = math.isclose(calculated_total_cost, total_cost, rel_tol=1e-2)
    
    # [Requirement 4] Verify maximum distance between consecutive cities
    max_distance_is_correct = math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2)
    
    if all([all_cities_visited_once, correct_tour_format, cost_is_correct, max_distance_is_correct]):
        return "CORRECT"
    else:
        return "FAIL"

# Test the provided solution
solution_tour = [0, 1, 5, 9, 2, 7, 4, 12, 11, 6, 3, 8, 14, 13, 10, 0]
solution_total_cost = 288.52
solution_max_distance = 37.54

# Run the verification
print(verify_solution(solution_tour, solution_total_cost, solution_max_distance))