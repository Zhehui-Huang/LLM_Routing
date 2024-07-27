import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cost):
    # City coordinates from the problem statement
    city_coordinates = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
        (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
        (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]
    
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 16 unique cities including depot city are visited
    if len(set(tour)) != 17:  # 16 cities + 1 depot city
        return "FAIL"
    
    # Check if the total cost is calculated correctly
    calculated_cost = 0
    for i in range(len(tour) - 1):
        c1 = tour[i]
        c2 = tour[i + 1]
        calculated_cost += calculate_distance(city_coordinates[c1], city_coordinates[c2])

    if not math.isclose(calculated_cost, cost, rel_tol=1e-6):  # Allowing a small relative tolerance
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Tour and provided cost from the alleged solution
provided_tour = [0, 8, 17, 18, 13, 11, 14, 2, 5, 9, 16, 7, 12, 6, 3, 4, 0]
provided_cost = 300.4790075184794

# Verify the solution
result = verify_solution(provided_tour, provided_cost)
print(result)