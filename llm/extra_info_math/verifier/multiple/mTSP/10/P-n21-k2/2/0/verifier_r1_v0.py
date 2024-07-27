def calculate_distance(p1, p2):
    from math import sqrt
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_within_bounds(value, bounds):
    return bounds[0] <= value <= bounds[1]

def check_tour_validity(tours, city_coordinates):
    # Check if each city is visited exactly once by one salesman and each city is in exactly one tour
    visited_cities = set()
    for tour in tours:
        # Exclude the starting and ending depot node
        visited_cities.update(tour[1:-1])

    all_cities = set(range(1, len(city_coordinates)))  # cities are from 1 to 20
    if visited_cities != all_cities:
        return False

    # Check flow conservation constraints, ensuring each city in a tour is both entered and left once
    for tour in tours:
        prev_city = None
        for city in tour:
            if prev_city is not None:
                # This verifies the city is entered from another city
                if prev_city == city:
                    return False
            prev_city = city
    
    # Ensure each salesman leaves the depot exactly once and returns exactly once
    for tour in tours:
        if tour[0] != tour[-1] or tour[0] != 0:
            return False
    
    return True

def check_subtour_eliminination_and_order(tours):
    # Check binary constraints and continuous variable constraints
    # Tours should not have subtours and are connected
    continuous_positions = {}
    for k, tour in enumerate(tours):
        for position, city in enumerate(tour):
            if city in continuous_positions:
                return False  # City visited more than once across all tours
            continuous_positions[city] = (position, k)

    # Check subtour elimination constraints. Each tour should follow a linear progression without loops
    for k, tour in enumerate(tours):
        node_position_in_tour = {node: i for i, node in enumerate(tour)}
        for i, node in enumerate(tour[:-1]):
            # verify no subtour formation, u_i - u_j + n * x_ij <= n - 1
            for j in range(i + 2, len(tour) - 1):
                if node_position_in_tour.get(tour[j], -1) - node_position_in_tour.get(tour[i], -1) <= len(city_coordinates) - 1 - 1:
                    return False

    return True

def unit_test_solution():
    city_coordinates = {0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
                        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
                        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
                        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
                        20: (45, 35)}
    tours = [
        [0, 16, 0],
        [0, 6, 0]
    ]

    if check_tour_validity(tours, city_coordinates) and check_subtour_eliminination_and_order(tours):
        return "CORRECT"
    else:
        return "FAIL"

# Execute the unit test
unit_test_result = unit_test_solution()
print(unit_test_result)