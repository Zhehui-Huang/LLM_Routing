import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(tour, total_cost, city_locations):
    # Requirements
    start_end_depot = tour[0] == 0 and tour[-1] == 0
    twelve_cities_visited = len(set(tour)) == 12
    correct_format = isinstance(tour, list) and isinstance(total_cost, (int, float))
    
    # Calculate total travel cost from the proposed tour
    calc_total_cost = 0
    for i in range(len(tour) - 1):
        calc_total_cost += calculate_distance(city_locations[tour[i]], city_locations[tour[i+1]])
    
    # Check cost within a small tolerance for floating point arithmetic issues
    cost_correct = math.isclose(total_cost, calc_total_cost, abs_tol=0.01)
    
    # If all conditions are met
    if start_end_depot and twelve_cities_visited and correct_format and cost_correct:
        return "CORRECT"
    else:
        return "FAIL"

# Define city locations based on the problem statement
city_locations = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Proposed solution
tour = [0, 10, 13, 14, 8, 3, 6, 11, 12, 9, 5, 1, 0]
total_cost = 215.75

# Verify solution
result = verify_solution(tour, total_cost, city_locations)
print(result)