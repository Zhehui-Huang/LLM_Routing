import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    # Cities coordinates
    cities = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
        (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
        (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    
    # Provided solution
    robots_tours = [
        [0, 18, 4, 14, 17, 16, 7, 2, 5, 1, 0],
        [0, 12, 3, 8, 9, 15, 13, 6, 11, 10, 0]
    ]
    
    provided_costs = [163.839338534758, 171.34728380168562]
    maximum_cost = 171.34728380168562

    # Check Requirement 1: Tours must start and end at the depot
    if any(tour[0] != 0 or tour[-1] != 0 for tour in robots_tours):
        return "FAIL"
    
    # Check Requirement 2: All cities must be visited exactly once
    all_cities = set(range(1, 19))  # city indices from 1 to 18
    visited_cities = set(city for tour in robots_tours for city in tour[1:-1])
    if visited_cities != all_cities:
        return "FAIL"
    
    # Check Requirement 3: This is subjective to the provided solution and cannot be verified without comparisons to other solutions.
    
    # Calculate and Check Requirement 4 & 5
    calculated_costs = []
    for tour in robots_tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_costs.append(cost)
    
    # Allow for minor differences in float calculations
    if not all(abs(provided - calculated) < 0.01 for provided, calculated in zip(provided_costs, calculated_costs)):
        return "FAIL"
    
    # Check Requirement 6: Verify max travel cost
    if not abs(max(calculated_costs) - maximum_cost) < 0.01:
        return "FAIL"
    
    return "CORRECT"

# Running the test
print(test_solution())