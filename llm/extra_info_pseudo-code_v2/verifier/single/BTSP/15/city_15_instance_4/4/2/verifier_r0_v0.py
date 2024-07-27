import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    # City coordinates
    cities = {
        0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
        5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
        10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
    }

    # Provided solution details
    tour = [0, 10, 6, 3, 8, 13, 14, 11, 12, 4, 12, 9, 7, 2, 5, 1, 0]
    total_travel_cost_provided = 375.9
    max_distance_provided = 45.45
    
    # Verify start and end at depot (Requirement 1 & 5)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify all cities visited exactly once except the depot (Requirement 2 & 5)
    if sorted(tour[1:-1]) != sorted(list(cities.keys())[1:]):
        return "FAIL"
    
    # Calculate the total travel cost and the maximum travel cost (Requirement 3, 6 & 7)
    total_cost_calculated = 0
    max_distance_calculated = 0
    for i in range(len(tour) - 1):
        city_a = cities[tour[i]]
        city_b = cities[tour[i + 1]]
        distance = calculate_distance(city_a, city_b)
        total_cost_calculated += distance
        if distance > max_distance_calculated:
            max_distance_calculated = distance
            
    # Check if the total and maximum distances are within acceptable rounding error bounds
    if (not math.isclose(total_cost_calculated, total_travel_cost_provided, abs_tol=0.1) or
        not math.isclose(max_distance_calculated, max_distance_provided, abs_tol=0.1)):
        return "FAIL"
    
    return "CORRECT"

# Run the test
print(test_solution())