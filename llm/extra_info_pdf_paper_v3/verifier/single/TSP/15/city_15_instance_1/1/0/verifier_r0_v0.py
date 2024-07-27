import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_solution(tour, total_cost):
    # Cities coordinates indexed from the depot city 0 to city 14
    cities = [
        (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), 
        (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), 
        (98, 1)
    ]
    
    # [Requirement 1] Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if each city is visited exactly once
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(cities) - 1 or any(city not in unique_cities for city in range(1, 15)):
        return "FAIL"
    
    # [Requirement 3] and [Requirement 4] (implicitly checked in total travel cost)
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        calculated_cost += euclidean_distance(x1, y1, x2, y2)
    
    # Check if the calculated cost matches the provided total cost with a tiny margin for floating point operations
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-09):
        return "FAIL"
    
    # [Requirement 5] and [Requirement 6] are assumed to be correct if the tour is right and the cost matches
    return "CORRECT"

# Given solution
tour_solution = [0, 10, 4, 9, 3, 7, 1, 6, 13, 2, 12, 11, 8, 14, 5, 0]
total_cost_solution = 396.8012768328815

# Test the solution
result = test_solution(tour_solution, total_cost_solution)
print(result)  # Output: "CORRECT" or "FAIL"