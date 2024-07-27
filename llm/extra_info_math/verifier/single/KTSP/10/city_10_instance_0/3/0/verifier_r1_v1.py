import math

def eurestrial_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    # Cities coordinates
    cities = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49)
    }
    
    # [Requirement 1] Tour starts and ends at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] The tour should consist of exactly 4 cities including the depot
    if len(tour) != 5 or len(set(tour[:-1])) != 4:
        return "FAIL"
    
    # [Requirement 3] Check if the total travel cost is calculated correctly
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
tour = [0, 5, 6, 9, 0]
total_travel_cost = 65.20172104938949

# Validate the solution
validation_result = verify_solution(tour, total_travel_cost)
print(validation_result)