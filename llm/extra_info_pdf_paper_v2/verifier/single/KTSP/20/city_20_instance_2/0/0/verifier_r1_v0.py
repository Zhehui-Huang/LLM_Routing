import math

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, travel_cost):
    cities = [
        (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
        (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
        (28, 49), (91, 94), (51, 58), (30, 48)
    ]
    
    # [Requirement 5]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2]
    if len(set(tour)) != 10 or tour.count(0) != 2:
        return "FAIL"
    
    # [Requirement 3]
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # [Requirement 6]
    if not math.isclose(travel_cost, calculated_cost, rel_tol=1e-9):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Example solution
tour = [0, 11, 6, 10, 4, 3, 13, 18, 16, 19, 0]
travel_cost = 271.6221587907936

# Run the verification
result = verify_tour(tour, travel_cost)
print(result)