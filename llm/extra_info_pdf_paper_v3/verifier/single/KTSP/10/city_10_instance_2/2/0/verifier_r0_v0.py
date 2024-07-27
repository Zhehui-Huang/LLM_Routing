import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(cities, tour, total_cost):
    # Constants and coordinates from the problem statement
    coordinates = {
        0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81),
        4: (41, 54), 5: (31, 35), 6: (23, 95), 7: (20, 56),
        8: (49, 29), 9: (13, 17)
    }
    
    # Validate number of cities
    if len(coordinates) != cities:
        return "FAIL"

    # Validate that the tour starts and ends at city 0 (depot)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Validate the tour length to be 6 including the starting and ending depot city
    if len(tour) != 7:
        return "FAIL"
    
    # Validate the exact cities involved
    if len(set(tour)) != len(tour):
        return "FAIL"

    # Calculate and validate the total travel cost using the Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    # Compare the calculated distance to the given cost using a tolerance
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
result = verify_solution(10, [0, 8, 5, 2, 1, 9, 0], 183.85)
print(result)