import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(cities, tour, reported_cost):
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Each city must be visited exactly once
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(cities) - 1 or not all(city in unique_cities for city in range(1, len(cities))):
        return "FAIL"
    
    # Requirement 3 and 4: Check valid tour format and calculate total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Check the format of the tour output and total cost calculation
    if total_cost != reported_cost:
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Given solution
tour = [0, 6, 1, 7, 9, 2, 5, 3, 8, 4, 0]
reported_cost = 278.9348447394249

# Run the verification
result = verify_solution(cities, tour, reported_cost)
print(result)