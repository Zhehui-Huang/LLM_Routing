import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, travel_cost):
    # Define city coordinates
    city_coordinates = [
        (16, 90),  # City 0
        (43, 99),  # City 1
        (80, 21),  # City 2
        (86, 92),  # City 3
        (54, 93),  # City 4
        (34, 73),  # City 5
        (6, 61),   # City 6
        (86, 69),  # City 7
        (30, 50),  # City 8
        (35, 73),  # City 9
        (42, 64),  # City 10
        (64, 30),  # City 11
        (70, 95),  # City 12
        (29, 64),  # City 13
        (32, 79)   # City 14
    ]
    
    # Verify that the tour starts and ends at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify that the tour includes exactly 10 cities (Requirement 2)
    if len(set(tour)) != 10:
        return "FAIL"
    
    # Verify that the calculated travel cost matches the provided cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1_idx = tour[i]
        city2_idx = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(city_coordinates[city1_idx], city_coordinates[city2_idx])
    
    # Using a tolerance due to floating-point arithmetic
    if not math.isclose(calculated_cost, travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 13, 8, 10, 12, 4, 1, 9, 5, 14, 0]
travel_cost = 185.9153023776061

# Verify the solution
result = verify_solution(tour, travel_cost)
print(result)