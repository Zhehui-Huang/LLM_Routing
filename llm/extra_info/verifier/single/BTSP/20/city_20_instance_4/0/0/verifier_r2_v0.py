import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, positions, total_travel_cost, max_distance):
    # Requirement 1: Start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit each city exactly once
    if sorted(tour) != sorted(list(range(len(positions)))):
        return "FAIL"
    
    # Calculating actual total travel cost and max distance
    actual_total_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(positions[tour[i]], positions[tour[i + 1]])
        actual_total_cost += distance
        if distance > actual_max_distance:
            actual_max_distance = distance
    
    # Allow a small difference due to floating-point precision
    if not (abs(actual_total_cost - total_travel_cost) < 1e-2 and abs(actual_max_dictance - max_distance) < 1e-2):
        return "FAIL"
    
    return "CORRECT"

# Define city positions as given in problem statement
city_positions = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Provided solution details
solution_tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
solution_total_travel_cost = 410.03585920085146
solution_max_distance = 89.01

# Test the solution
test_result = test_solution(solution_tour, city_positions, solution_total_travel_cost, solution_max_distance)
print(test_result)