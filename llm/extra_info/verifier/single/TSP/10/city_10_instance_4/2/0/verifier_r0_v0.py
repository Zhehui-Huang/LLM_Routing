import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, total_travel_cost, coordinates):
    expected_cities = set(range(10))  # As there are 10 cities including the depot
    visited_cities = set(tour)
    
    # [Requirement 1] Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Visit each city exactly once (except depot which is visited twice)
    if visited_cities == expected_cities and tour.count(0) == 2 and all(tour.count(city) == 1 for city in expected_cities if city != 0):
        pass
    else:
        return "FAIL"
    
    # [Requirement 3 & 4] Calculate the travel cost and ensure it matches the provided cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i+1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    # Check if the calculated cost is sufficiently close to the provided total travel cost.
    if abs(calculated_cost - total_travel_cost) > 0.001:
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# City coordinates indexed by city number: 0 -> Depot, 1-9 -> Other cities
coordinates = [
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

tour = [0, 4, 7, 5, 1, 9, 8, 2, 6, 3, 0]
total_travel_cost = 320.7939094250147

result = verify_solution(tour, total_travel_cost, coordinates)
print(result)