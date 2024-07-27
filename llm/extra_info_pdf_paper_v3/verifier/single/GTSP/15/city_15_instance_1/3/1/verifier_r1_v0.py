import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(tour, total_cost, city_coordinates, city_groups):
    # Check Requirement 1: Starts and ends at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: One city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        for i, group in enumerate(city_art_groups):
            if city in group:
                if i in visited_groups:
                    return "FAIL"
                visited_groups.add(i)
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Check Requirement 3: Uses Euclidean distance formula
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # Check Requirement 5: Includes order starting and ending at city 0 and correct total cost
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    return "CORRECT"

# Cities coordinates
city_coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

city_groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Provided solution to test
tour_solution = [0, 5, 10, 4, 11, 0]
total_cost_solution = 184.24203302868492  # This cost is rounded, actual might slightly differ due to float precision

# Verify the solution
print(verify_solution(tour_solution, total_cost_solution, city_coordinates, city_groups))