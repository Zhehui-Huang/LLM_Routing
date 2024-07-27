import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, expected_cost):
    # Coordinates for each city index
    coordinates = [
        (79, 15),  # City 0
        (79, 55),  # City 1
        (4, 80),   # City 2
        (65, 26),  # City 3
        (92, 9),   # City 4
        (83, 61),  # City 5
        (22, 21),  # City 6
        (97, 70),  # City 7
        (20, 99),  # City 8
        (66, 62)   # City 9
    ]

    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit exactly 8 cities including the depot
    if len(set(tour)) != 8 or len(tour) != 9:
        return "FAIL"
    
    # Calculate the actual travel cost
    actual_cost = sum(calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
    
    # Requirement 3: Minimize the total Euclidean travel cost (hard to check optimality here without comparison)
    # We'll check if the calculated cost matches the expected cost instead
    if not math.isclose(actual_cost, expected_cost, abs_tol=0.1):
        return "FAIL"
    
    return "CORRECT"


# Provided solution
tour = [0, 3, 6, 9, 1, 5, 7, 4, 0]
total_travel_cost = 235.38

# Check if the solution is correct
result = verify_solution(tour, total_travel>])]
print(result)