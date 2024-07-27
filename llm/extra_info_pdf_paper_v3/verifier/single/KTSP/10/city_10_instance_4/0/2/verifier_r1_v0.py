import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, provided_cost):
    cities = {
        0: (79, 15),
        1: (79, 55),
        2: (4, 80),
        3: (65, 26),
        4: (92, 9),
        5: (83, 61),
        6: (22, 21),
        7: (97, 70),
        8: (20, 99),
        9: (66, 62)
    }
    
    # Requirement 1: Must start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly 8 cities, including the depot city
    if len(tour) != 9 or len(set(tour)) != 9:  # tour includes 8 unique cities + 1 repeat of the depot
        return "FAIL"
    
    # Calculate the total travel cost by the Euclidean distance between consecutive cities
    actual_cost = 0
    for i in range(len(tour) - 1):
        current_city = cities[tour[i]]
        next_city = cities[tour[i + 1]]
        actual_cost += calculate_euclidean_distance(current_city, next_city)
    
    # Requirement 3: Check if calculated distance matches the provided total cost
    # Allow a small margin of error due to floating point arithmetic discrepancies
    if not math.isclose(actual_cost, provided_cost, abs_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 4, 1, 5, 9, 8, 2, 3, 0]
total_travel_cost = 269.51

# Verify the solution
result = verify_solution(tour, total_travel_cost)
print(result)