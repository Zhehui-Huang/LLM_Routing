import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, total_cost, city_coordinates):
    requirements_met = True
    
    # [Requirement 1] Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        print("Requirement 1 FAIL: Tour must start and end at the depot (city 0).")
        requirements_met = False
        
    # [Requirement 2] The robot must visit exactly 6 cities, including the depot city
    if len(tour) != 7:
        print("Requirement 2 FAIL: The robot must visit exactly 6 cities including the depot.")
        requirements_met = False
        
    # [Requirement 4] Check format of the solution
    if not isinstance(tour, list) or not isinstance(total_cost, (int, float)):
        print("Requirement 4 FAIL: Output format is incorrect.")
        requirementshet = False
    
    # [Requirement 3] Check if the given total cost is the actual travel cost of the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    if abs(calculated_cost - total_cost) > 1e-2:
        print("Requirement 3 FAIL: Reported cost does not match calculated cost.")
        requirements_met = False

    return "CORRECT" if requirements_met else "FAIL"

# Constants and provided solution
city_coordinates = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
    5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
}
provided_tour = [0, 1, 2, 7, 4, 3, 0]
provided_total_cost = 282.41

# Run test
result = test_solution(provided_tour, provided_total_cost, city_coordinates)
print(result)