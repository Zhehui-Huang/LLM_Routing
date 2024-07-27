import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    # City coordinates including the depot
    city_coordinates = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
        (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), 
        (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]

    # Group information
    city_groups = [
        [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
    ]

    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if only one city from each group is visited
    visited_groups = [False] * len(city_groups)
    for i, group in enumerate(city_groups):
        visited_count = 0
        for city in tour:
            if city in group:
                visited_count += 1
                if visited_count > 1:
                    return "FAIL"
        if visited_count != 1:
            return "FAIL"
        visited_groups[i] = True

    # Check the total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    # The provided values satisfy all the constraints
    return "CORRECT"

# Test the given solution
tour = [0, 4, 7, 12, 15, 3, 18, 0]
total_cost = 227.40171050114

print(verify_solution(tour, total_cost))