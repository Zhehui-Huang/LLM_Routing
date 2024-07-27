import math

def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def verify_solution(tour, total_cost):
    cities = [
        (9, 93),  # depot city 0
        (8, 51),  # city 1
        (74, 99), # city 2
        (78, 50), # city 3
        (21, 23), # city 4
        (88, 59), # city 5
        (79, 77), # city 6
        (63, 23), # city 7
        (19, 76), # city 8
        (21, 38), # city 9
        (19, 65), # city 10
        (11, 40), # city 11
        (3, 21),  # city 12
        (60, 55), # city 13
        (4, 39)   # city 14
    ]
    
    # Test if starts and ends at depot:
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Test if exactly 4 cities are visited:
    if len(tour) != 5:  # including repeated depot city
        return "FAIL"
    
    # Calculate and check the total travel distance:
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour = [0, 1, 10, 8, 0]
total_cost = 90.53947981328088

# Validate the solution
result = verify_solution(tour, total_cost)
print("Output:", result)