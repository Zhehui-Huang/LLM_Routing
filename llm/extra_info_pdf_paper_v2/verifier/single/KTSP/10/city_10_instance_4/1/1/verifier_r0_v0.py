import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, total_travel_cost):
    # Coordinates of cities
    city_coords = {
        0: (79, 15),
        1: (79, 55),
        2: (4, 80),
        3: (65, 26),
        4: (92, 9),
        5: (83, 61),
        6: (22, 21),
        7: (97, 70),
        8: (20, 99),
        9: (66, 62)
    }

    # Check the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check that the tour visits exactly 8 cities including the depot
    if len(tour) != 9 or len(set(tour)) != 9:
        return "FAIL"
    
    # Check if the tour visits any city more than once, except the depot which is allowed twice
    visited_cities = set(tour)
    for city in visited_cities:
        if tour.count(city) > 2 or (tour.count(city) > 1 and city != 0):
            return "FAIL"
    
    # Calculate the total travel cost and compare it to provided total_travel_cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        calculated_cost += calculate_euclidean_distppance(city_coords[city1][0], city_coords[city1][1], city_coords[city2][0], city_coords[city2][1])
    
    # Assert total cost is approximately equal to the provided cost due to floating-point precision
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-3):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Provided solution
tour = [0, 4, 7, 5, 1, 9, 3, 6, 0]
total_travel_cost = 250.76

# Execute verification
result = verify_solution(tour, total_travel_cost)
print(result)