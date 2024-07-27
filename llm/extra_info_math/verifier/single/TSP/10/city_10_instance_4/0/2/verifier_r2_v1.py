import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(tour, total_travel_cost, cities):
    # Requirement 1: Starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        print("FAIL: The tour must start and end at the depot city 0.")
        return "FAIL"
    
    # Requirement 2: Each city visited once
    expected_cities = list(range(1, len(cities)))  # cities from 1 to n-1
    visited_cities = sorted(tour[1:-1])  # skip the first and last city (depot)
    if visited_cities != expected_cities:
        print("FAIL: Each city must be visited exactly once.")
        return "FAIL"
    
    # Requirement 3: Travel cost calculation
    calculated_cost = sum(calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, total_travel_cost, abs_tol=0.01):
        print(f"FAIL: The calculated travel cost {calculated_cost} does not match the provided travel cost {total_travel_cost}.")
        return "FAIL"
    
    # Requirement 5: No subtours
    if len(set(tour[1:-1])) != len(tour[1:-1]):
        print("FAIL: Subtour detected within the tour.")
        return "FAIL"
    
    print("CORRECT")
    return "CORRECT"

# Coordinates of cities including the depot city
cities = [
    (79, 15),  # Depot city 0
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

# Provided solution output
tour = [0, 3, 6, 2, 8, 9, 1, 5, 7, 4, 0]
total_travel_cost = 320.79

# Run the verification unit test
check_solution(tour, total_travel_cost, cities)