import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_tour(tour, cities):
    # Requirement 1: Starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visits each city exactly once (except for the depot city, which is visited twice)
    visited = set(tour)
    if len(visited) != len(cities) or visited != set(range(len(cities))):
        return "FAIL"
    
    # Calculate total travel cost and check maximum distance
    total_travel_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        total_travel_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    # Compare with given total travel cost and maximum distance
    expected_total_cost = 655.8064834576943
    expected_max_distance = 75.28612089887484

    if not (math.isclose(total_travel_cost, expected_total_cost, abs_tol=0.01) and 
            math.isclose(max_distance, expected_max_distance, abs_tol=0.01)):
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates
cities = [
    (16, 90),  # City 0: Depot
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

tour = [0, 14, 10, 0, 13, 6, 5, 3, 8, 7, 11, 4, 1, 12, 9, 2, 0]  # Provided solution

result = verify_tour(tour, cities)
print(result)