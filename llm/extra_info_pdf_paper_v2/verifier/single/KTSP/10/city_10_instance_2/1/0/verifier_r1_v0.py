import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    cities = {
        0: (90, 3),
        1: (11, 17),
        2: (7, 27),
        3: (95, 81),
        4: (41, 54),
        5: (31, 35),
        6: (23, 95),
        7: (20, 56),
        8: (49, 29),
        9: (13, 17)
    }
    
    # Requirement 1: The robot needs to start and end its tour at the depot city, which is city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: The robot must visit exactly 6 cities, including the starting depot city.
    if len(set(tour)) != 6:
        return "FAIL"
    
    # Calculate cost and compare to given total_cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    calculated_cost = round(calculated_cost, 2)
    
    # Requirement 3: Check if the total calculated travel cost matches the provided total cost.
    if calculated_cost != total_cost:
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour = [0, 9, 1, 2, 5, 8, 0]
total_cost = 105.59

# Execute the verification
result = verify_solution(tour, total_cost)
print(result)