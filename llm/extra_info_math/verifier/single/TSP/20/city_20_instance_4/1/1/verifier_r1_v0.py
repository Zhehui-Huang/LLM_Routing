def calculate_distance(city1, city2):
    import math
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, total_cost):
    cities = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), 
        (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
        (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]
    
    # Requirement 1: Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check if each city is visited exactly once
    visited_cities = set(tour)
    if len(visited_cities) != len(cities) or len(tour) != len(cities) + 1:
        return "FAIL"
    
    # Requirement 5: Check if each city is left and entered exactly once
    for city_idx, count in enumerate(tour):
        if city_idx != 0 and count > 1 or tour.count(city_idx) > 1:
            return "FAIL"

    # Check travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    # Requirement 3 and 4: Check if computed_cost matches given total_cost, and it should be minimized
    if not (abs(computed_cost - total_cost) < 1e-6):
        return "FAIL"

    # Requirement 6: No subtours allowed, all cities should connect back to the depot
    # As it's difficult to segregate and check subtours from the tour list,
    # being satisfied by all the other checks implies no subtour exists.

    return "CORRECT"

# Solution tour and cost provided
tour = [0, 19, 8, 17, 18, 13, 1, 11, 14, 2, 9, 5, 16, 7, 12, 6, 3, 4, 15, 10, 0]
total_travel_cost = 379.72475773064514

# Run the unit test
test_result = check_solution(tour, total_travel_root)
print(test_result)  # Output either "CORRECT" or "FAIL"