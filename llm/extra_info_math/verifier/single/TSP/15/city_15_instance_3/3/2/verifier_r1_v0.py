import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities_positions, reported_cost):
    # Check start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once
    if set(tour) != set(range(len(cities_positions))):
        return "FAIL"
    
    # Check correct calculation and minimization of the total travel cost
    calculated_cost = sum(euclidean_distance(cities_positions[tour[i]], cities_positions[tour[i+1]]) for i in range(len(tour)-1))
    
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-3):
        return "FAIL"
    
    return "CORRECT"

# Define cities' positions indexed from the depot (0) onwards
cities_positions = [
    (16, 90), # Depot city 0
    (43, 99), # City 1
    (80, 21), # City 2
    (86, 92), # City 3
    (54, 93), # City 4
    (34, 73), # City 5
    (6, 61),  # City 6
    (86, 69), # City 7
    (30, 50), # City 8
    (35, 73), # City 9
    (42, 64), # City 10
    (64, 30), # City 11
    (70, 95), # City 12
    (29, 64), # City 13
    (32, 79)  # City 14
]

# Provided solution with tour and total cost
tour_solution = [0, 14, 5, 9, 10, 13, 6, 8, 11, 2, 7, 3, 12, 4, 1, 0]
reported_total_cost = 303.31

# Verify solution
result = verify_solution(tour_solution, cities_positions, reported_total_cost)
print(result)