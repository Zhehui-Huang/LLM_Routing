import math

# Provided cities coordinates including the depot city
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Provided solution
tour = [0, 0, 0, 0, -1, -1, -1, -1, -1, 14, -1, -1, -1, 0, 0, 0]
reported_cost = 46.04345773288535

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, cities, reported_cost):
    # Check start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check all cities visited exactly once
    visited = set(tour) - {-1}  # Remove placeholder -1 from tour
    if len(visited) != len(cities) or visited != set(range(len(cities))):
        return "FAIL"
    
    # Calculate the total cost of the tour
    total_cost = 0
    for i in range(1, len(tour)):
        if tour[i] == -1:  # Ignore invalid entries (-1)
            continue
        total_cost += calculate_distance(cities[tour[i - 1]], cities[tour[i]])
    
    # Check if the reported cost is approximately equal to the calculated cost
    # Allowing a small error due to floating point precision issues
    if not math.isclose(total, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Verify the solution
result = verify_tour(tour, cities, reported_cost)
print(result)