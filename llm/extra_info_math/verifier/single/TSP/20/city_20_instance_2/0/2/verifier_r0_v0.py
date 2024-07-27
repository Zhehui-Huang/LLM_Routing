import math

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, cities, reported_cost):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once
    visited = set(tour[1:-1])
    if len(visited) != len(cities) - 1 or any(city not in visited for city in cities if city != (3, 26)):  # Exclude depot
        return "FAIL"

    # Calculate the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Check if cost is correctly calculated and reported
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Given city coordinates
cities = [
    (3, 26),   # Depot city 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

# Given tour and total cost
tour = [0, 6, 8, 10, 3, 4, 17, 1, 5, 2, 9, 15, 13, 18, 7, 11, 19, 16, 14, 12, 0]
reported_cost = 431.17

# Verification
result = verify_solution(tour, cities, reported_cost)
print(result)  # Output should be "CORRECT" if the solution meets all the requisites