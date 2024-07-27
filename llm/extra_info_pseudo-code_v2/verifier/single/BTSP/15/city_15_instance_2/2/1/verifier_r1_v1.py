import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def unit_tests(tour, total_travel_cost, max_distance, city_positions):
    # Check Requirement 1: Start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Each city visited exactly once, except depot city
    unique_visits = set(tour)
    if len(unique_visits) != len(city_positions) or tour.count(0) != 2:
        return "FAIL"
    
    # Check Requirement 5: Tour format starting and ending at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 6: Correct calculation of total travel cost
    calculated_cost = sum(calculate_distance(city_positions[tour[i]], city_positions[tour[i + 1]]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    
    # Check Requirement 7: Correct maximum distance between consecutive cities
    calculated_max_dist = max(calculate_distance(city_positions[tour[i]], city_positions[tour[i + 1]]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_max_dist, max_and_distance, abs_tol=1e-5):
        return "FAIL"
    
    # Check Requirement 3: Travel cost as Euclidean distance
    return "CORRECT"

# Assumed solution data
city_positions = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), 
                  (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]

example_tour = [0, 6, 2, 12, 13, 7, 9, 10, 5, 4, 3, 11, 1, 8, 14, 0]
example_total_travel_cost = 429.3035370385243
example_max_distance = 85.44003745317531

# Running unit tests with corrected name
test_result = unit_tests(example_tour, example_total_travel_cost, example_max_distance, city_values)
print(test_result)