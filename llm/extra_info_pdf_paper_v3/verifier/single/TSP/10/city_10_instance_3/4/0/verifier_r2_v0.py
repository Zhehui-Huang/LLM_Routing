import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, costs):
    cities = [
        (84, 67),  # Depot
        (74, 40),
        (71, 13),
        (74, 82),
        (97, 28),
        (0, 31),
        (8, 62),
        (74, 56),
        (85, 71),
        (6, 76)
    ]
    
    # [Requirement 1] Verifying number of cities
    if len(cities) != 10:
        return "FAIL"
    
    # [Requirement 4] Checking if all cities are visited exactly once and tour ends at depot
    if len(set(tour)) != 10 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 6] Check tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 3] Calculating and verifying total travel cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        current_city = cities[tour[i]]
        next_city = cities[tour[i + 1]]
        calculated_cost += calculate_distance(current_city, next_city)

    # Comparing provided tour cost with calculated cost
    if not math.isclose(calculated_cost, costs, rel_tol=1e-5):
        return "FAIL"
   
    return "CORRECT"

# Test if provided solution meets requirements
solution_tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
solution_cost = 315.5597914831042
result = verify_tour(solution_tour, solution_cost)
print(result)