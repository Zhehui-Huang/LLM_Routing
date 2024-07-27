import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_solution(tour, total_cost):
    # Define the coordinates of each city, index as city number
    coordinates = [
        (26, 60),  # Depot city 0
        (73, 84),  # City 1
        (89, 36),  # City 2
        (15, 0),   # City 3
        (11, 10),  # City 4
        (69, 22),  # City 5
        (28, 11),  # City 6
        (70, 2),   # City 7
        (47, 50),  # City 8
        (60, 29),  # City 9
        (29, 26),  # City 10 
        (85, 68),  # City 11
        (60, 1),   # City 12
        (71, 73),  # City 13
        (82, 47),  # City 14
        (19, 25),  # City 15
        (75, 9),   # City 16
        (52, 54),  # City 17
        (64, 72),  # City 18
        (14, 89)]  # City 19

    # Groups of cities
    city_groups = [
        [5, 6, 16],  # Group 0
        [8, 18, 19], # Group 1
        [11, 12, 13],# Group 2
        [1, 3, 9],   # Group 3
        [2, 4, 14],  # Group 4
        [10, 17],    # Group 5
        [7, 15]      # Group 6
    ]

    # Check the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check that the tour visits exactly one city from each group
    visited_groups = [False] * len(city_groups)
    for city in tour[1:-1]:  # exclude the initial and final depot visits
        for i, group in enumerate(city_groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"   # a city from this group has already been visited
                visited_groups[i] = True
                break

    if not all(visited_groups):
        return "FAIL"

    # Check the total travel cost is as expected
    computed_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        computed_cost += calculate_euclidean_distance(*coordinates[city1], *coordinates[city2])

    if abs(computed_cost - total_cost) > 1e-4:  # tolerance for floating point comparison issues
        return "FAIL"

    return "CORRECT"

# Given solution
tour = [0, 5, 18, 13, 1, 14, 10, 15, 0]
total_cost = 266.71610174713

# Test the solution
result = test_solution(tour, total_cost)
print(result)