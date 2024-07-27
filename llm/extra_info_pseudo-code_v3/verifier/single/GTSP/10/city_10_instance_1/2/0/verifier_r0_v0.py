import math

def calculate_distance(city1, city2):
    return math.hypot(city1[0] - city2[0], city1[1] - city2[1])

def test_robot_tour_solution():
    # Coordinates of the cities
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
        9: (95, 89)
    }
    
    # Groups of cities
    city_groups = {
        0: [5, 6, 7],
        1: [2, 3],
        2: [1, 9],
        3: [4, 8]
    }
    
    # Proposed solution
    tour = [0, 5, 2, 9, 8, 0]
    proposed_total_cost = 183.99
    
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check for exactly one city from each group
    visited = set(tour[1:-1])  # exclude the starting and ending depot city
    for group, group_cities in city_groups.items():
        if not (visited & set(group_cities)):  # intersection should not be empty
            return "FAIL"
        if len(visited & set(group_cities)) != 1:
            return "FAIL"
    
    # Calculate the actual total travel cost based on Euclidean distance
    actual_total_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    
    # Allow a small margin for float comparison (e.g., due to rounding in the statement)
    if not math.isclose(actual_total_cost, proposed_total_cost, rel_tol=0.005):
        return "FAIL"
    
    return "CORRECT"

# Run the test and print the result
print(test_robot_tour_solution())