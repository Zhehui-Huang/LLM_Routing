import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(tour, costs, cities):
    # Requirement 1: Starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        print("FAIL: The tour must start and end at the depot city 0.")
        return "FAIL"
    
    # Requirement 2: Each city visited once
    if sorted(tour[1:-1]) != list(range(1, len(cities))):
        print("FAIL: Each city must be visited exactly once.")
        return "FAIL"
    
    # Requirement 3: Travel cost calculated correctly
    # Calculate the total travel cost from the provided tour and compare with given costs
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    if not math.isclose(calculated_cost, costs, abs_tol=0.01):
        print(f"FAIL: The provided travel cost {costs} does not match the calculated cost {calculated_cost}")
        return "FAIL"
    
    # Requirement 5: Check for subtours
    seen = set()
    for city in tour:
        if city in seen and city != 0:
            print("FAIL: Subtour detected.")
            return "FAIL"
        seen.add(city)
    
    print("CORRECT")
    return "CORRECT"

# Define cities coordinates
cities = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Proposed tour and total cost from solution found
tour = [0, 3, 6, 2, 8, 9, 1, 5, 7, 4, 0]
total_travel_cost = 320.79

# Run unit test to verify the solution
check_solution(tour, total_travelltotal_travel_cost, cities)