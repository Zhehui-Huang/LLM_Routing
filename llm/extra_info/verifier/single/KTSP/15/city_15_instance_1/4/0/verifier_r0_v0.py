import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, total_cost):
    # Coordinates of the cities
    coordinates = [
        (29, 51),  # City 0
        (49, 20),  # City 1
        (79, 69),  # City 2
        (17, 20),  # City 3
        (18, 61),  # City 4
        (40, 57),  # City 5
        (57, 30),  # City 6
        (36, 12),  # City 7
        (93, 43),  # City 8
        (17, 36),  # City 9
        (4, 60),  # City 10
        (78, 82),  # City 11
        (83, 96),  # City 12
        (60, 50),  # City 13
        (98, 1)   # City 14
    ]
    
    # [Requirement 1]: Check start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2]: Check the tour visits exactly 6 cities
    if len(tour) != 7:  # includes the depot city twice (start and end)
        return "FAIL"
    
    # [Requirement 3]: Calculate and confirm the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_from = coordinates[tour[i]]
        city_to = coordinates[tour[i+1]]
        calculated_cost += euclidean_distance(city_from[0], city_from[1], city_to[0], city_to[1])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided solution to test
tour = [0, 6, 1, 7, 3, 9, 0]
total_travel_cost = 118.8954868377263

# Verify the solution
print(verify_solution(tour, total_travel_data))