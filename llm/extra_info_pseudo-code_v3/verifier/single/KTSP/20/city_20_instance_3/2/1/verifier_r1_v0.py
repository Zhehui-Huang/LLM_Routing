import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def validate_tour_and_cost(tour, cost, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour must start and end at city 0."
    
    if len(tour) != 14:
        return False, "Tour must visit exactly 13 cities including the depot city."
    
    if len(set(tour)) != len(tour):
        return False, "Tour contains duplicate cities."
    
    calculated_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    if abs(calculated_cost - cost) > 0.01:
        return False, "Provided total travel cost does not match the calculated cost."
    
    return True, "Tour and cost are valid."

def test_solution(tour, cost):
    # Define the cities based on provided coordinates
    cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
              (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), 
              (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]
    
    # Your solution
    provided_tour = tour
    provided_cost = cost
    
    # Requirement 5: Output format check
    if not isinstance(provided_tour, list) or not isinstance(provided_cost, float):
        return "FAIL"
    
    # Validate the tour and cost
    is_valid, message = validate_tour_and_cost(provided_tour, provided_cost, cities)
    
    if is_valid:
        return "CORRECT"
    else:
        print(message)
        return "FAIL"

# The provided solution
solution_tour = [0, 3, 5, 17, 16, 18, 4, 7, 12, 13, 6, 19, 1, 0]
solution_cost = 354.38

# Run the test
test_result = test_solution(solution_tour, solution_cost)
print(test_result)