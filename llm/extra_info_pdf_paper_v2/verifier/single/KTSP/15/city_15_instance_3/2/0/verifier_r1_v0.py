import math

# The cities with their coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Proposed tour and its cost
tour = [0, 1, 4, 12, 3, 10, 8, 13, 9, 5, 0]
reported_cost = 194.5976667568509

# Helper function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to verify the correctnes of the solution
def verify_solution(tour, reported_cost):
    # Check 1: Starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check 2: Visits exactly 10 cities, including the depot
    if len(set(tour)) != 10 or len(tour) != 11:  # 10 cities + 1 for returning to the depot
        return "FAIL"
    
    # Check 3: Actual calculated tour cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(tour[i], tour[i+1])
    
    # Since cost comparisons might produce floating-point inaccuracies, we check closeness instead of equality
    if not math.isclose(reported_cost, calculated_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Perform the verification
result = verify_solution(tour, reported_cost)
print(result)