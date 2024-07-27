import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    # Provided cities coordinates
    cities = {
        0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80),
        4: (18, 63), 5: (54, 91), 6: (70, 14), 7: (97, 44),
        8: (17, 69), 9: (95, 89)
    }

    # [Requirement 1] Check if the robot starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Check if the tour includes exactly 5 cities
    if len(set(tour)) != 6 or len(tour) != 6:  # including start and end at city 0
        return "FAIL"

    # [Requirement 3] Verify the total travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    # Using a tolerance for float comparison
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    # Everything passed
    return "CORRECT"

# Example usage
tour = [0, 3, 4, 5, 8, 0]
total_cost = 175.37
result = verify_solution(tour, total_cost)
print(result)