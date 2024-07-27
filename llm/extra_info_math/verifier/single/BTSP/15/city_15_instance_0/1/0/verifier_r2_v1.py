import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, city_coordinates):
    # Check if each city (except the depot) is visited exactly once and tour starts and ends at depot (Requirement 1)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculating frequency of visits in each city
    city_visit_count = {i: 0 for i in range(len(city_coordinates))}
    for city in tour:
        city_visit_count[city] += 1

    # Check if all cities are visited exactly once (City 0 is allowed to be visited more as it's the depot)
    for city, count in city_visit241.items():
        if city != 0 and count != 1:
            return "FAIL"
        if city == 0 and count < 2:
            return "FAIL"

    # Calculate travel cost and max distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
        total_cost += dist
        max_distance = max(max_distance, dist)
    
    # Comparing with stated values in problem description
    stated_max_distance = 19.72
    stated_total_cost = 276.12

    if abs(max_distance - stated_max_distance) > 0.01 or abs(total_cost - stated_total_cost) > 0.01:
        return "FAIL"

    return "CORRECT"

# Given city coordinates
city_coordinates = [
    (9, 93),    # City 0
    (8, 51),    # City 1
    (74, 99),   # City 2
    (78, 50),   # City 3
    (21, 23),   # City 4
    (88, 59),   # City 5
    (79, 77),   # City 6
    (63, 23),   # City 7
    (19, 76),   # City 8
    (21, 38),   # City 9
    (19, 65),   # City 10
    (11, 40),   # City 11
    (3, 21),    # City 12
    (60, 55),   # City 13
    (4, 39)     # City 14
]

# Provided solution tour
solution_tour = [0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 0]

# Running the verification
result = verify_solution(solution_tour, city_coordinates)
print(result)