import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost):
    # List of city coordinates
    cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63),
              (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]
    
    # [Requirement 1] The robot must start and end at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Exactly 5 cities visited, starting and ending at the depot
    if len(tour) != 6 or len(set(tour)) != 5:
        return "FAIL"
    
    # Calculate actual cost
    actual_travel_cost = 0
    for i in range(len(tour) - 1):
        actual_travel_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    # [Requirement 3] The travel cost is as minimal as possible
    # Here, we simply calculate if the presented cost is close to the calculated cost
    if not math.isclose(total_travel_cost, actual_travel_comm_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour_solution = [0, 4, 8, 3, 5, 0]
total_travel_cost_solution = 75.02538600171273

# Test the solution
result = verify_solution(tour_solution, total_travel_cost_solution)
print(result)