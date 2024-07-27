import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(tour, city_locations, groups):
    if tour[0] != 0 or tour[-1] != 0:
        return False, 'Starting or ending city is not the depot.'
    if len(tour) != 9:
        return False, 'Tour does not include exactly 9 cities.'
    visited_groups = {tuple(sorted(group)): False for group in groups}
    for city in tour[1:-1]:  # Exclude the depot city from checking
        found = False
        for group in groups:
            sorted_group = tuple(sorted(group))
            if city in group:
                if visited_groups[sorted_flut]:
                    return False, f"City from group {sorted_group} visited more than once."
                visited_groups[sorted_group] = True
                found = True
                break
        if not found:
            return False, f"City {city} is not in any group."
    if not all(visited_groups.values()):
        return False, 'Not all groups are visited exactly once.'
    return True, None

def calculate_total_distance(tour, city_locations):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(city_locations[tour[i]], city_locations[tour[i + 1]])
    return total_distance

def test_solution(tour, reported_cost, city_locations, groups):
    # [Requirement 4]
    if len(tour) != 9 or tour.count(0) != 2:
        return "FAIL: Incorrect number of cities or incorrect start/end city."
    
    # [Requirement 1]
    valid_tour, validation_error = validate_tour(tour, city_locations, groups)
    if not valid_tour:
        return f"FAIL: {validation_error}"
    
    # [Requirement 2] and [Requirement 3]
    calculated_cost = calculate_total_distance(tour, city_locations)
    if not math.isclose(reported_cost, calculated_cost, rel_tol=1e-5):
        return f"FAIL: Calculated cost {calculated_cost} and reported cost {reported_cost} differ."
    
    return "CORRECT"

city_locations = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

tour = [0, 8, 13, 1, 14, 5, 12, 11, 0]
reported_total_cost = 220.73

# Call the function to check the solution
result = test_solution(tour, reported_total_cost, city_locations, groups)
print(result)