import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, total_cost_given, max_distance_given):
    # City coordinates as provided
    cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
              (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

    # [Requirement 1] Visits each city exactly once and returns to start
    if len(tour) != len(cities) + 1 or len(set(tour)) != len(cities) or tour[0] != tour[-1]:
        return "FAIL"

    # [Requirement 2] Calculates correct total travel cost and max distance 
    total_cost_calculated = 0
    max_distance_calculated = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost_calculated += distance
        if distance > max_distance_calculated:
            max_distance_calculated = distance

    total_cost_correct = math.isclose(total_cost_calculated, total_cost_given, rel_tol=1e-2)
    max_distance_correct = math.isclose(max_distance_calculated, max_distance_given, rel_tol=1e-2)
    
    # [Requirement 3] Checks if the maximum distance calculation is correct
    if total_cost_correct and max_distance_correct:
        return "CORRECT"
    else:
        return "FAIL"

# Given parameters
tour = [0, 8, 10, 1, 11, 14, 12, 9, 4, 7, 3, 5, 6, 2, 13, 0]
total_cost_given = 363.59
max_distance_given = 63.60

# Run the test
result = test_solution(tour, total_cost_given, max_distance_given)
print(result)