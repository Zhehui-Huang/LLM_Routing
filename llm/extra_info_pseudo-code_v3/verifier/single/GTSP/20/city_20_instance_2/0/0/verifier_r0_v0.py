import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tour_and_cost():
    cities = [
        (3, 26),   # City 0: Depot
        (85, 72),  # City 1
        (67, 0),   # City 2
        (50, 99),  # City 3
        (61, 89),  # City 4
        (91, 56),  # City 5
        (2, 65),   # City 6
        (38, 68),  # City 7
        (3, 92),   # City 8
        (59, 8),   # City 9
        (30, 88),  # City 10
        (30, 53),  # City 11
        (11, 14),  # City 12
        (52, 49),  # City 13
        (18, 49),  # City 14
        (64, 41),  # City 15
        (28, 49),  # City 16
        (91, 94),  # City 17
        (51, 58),  # City 18
        (30, 48)   # City 19
    ]
    city_groups = [[7, 10, 11, 12], [3, 8, 13, 16], [2, 4, 15, 18], [1, 9, 14, 19], [5, 6, 17]]
    proposed_tour = [0, 16, 19, 18, 11, 6, 0]
    proposed_cost = 150.53
    
    # Test that the tour starts and ends at the depot city
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"
    
    # Test that the tour visits exactly one city from each city group
    visited_groups = [0] * len(city_groups)
    for city in proposed_tour[1:-1]:  # Exclude depot city at start/end
        for i, group in enumerate(city_groups):
            if city in group:
                visited_groups[i] += 1
                break
    
    if not all(count == 1 for count in visited_groups):
        return "FAIL"
    
    # Calculate the travel cost in the proposed tour
    calculated_cost = 0
    for i in range(len(proposed_tour) - 1):
        calculated_cost += euclidean_distance(cities[proposed_tour[i]], cities[proposed_tour[i+1]])
    
    # Test if the calculated cost roughly matches the proposed cost within a reasonable precision
    if not math.isclose(calculated_cost, proposed_cost, abs_tol=0.01):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Run the test
result = test_tour_and_cost()
print(result)