import math

# Define the cities coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Given solution
tour = [0, 0, 8, 18, 15, 13, 11, 16, 14, 12, 0]
total_cost = 247.59306176730252

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to verify the solution
def verify_solution(tour, total_cost):
    # Check tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check tour visits exactly 10 cities, including depot city
    if len(set(tour)) != 10:
        return "FAIL"
    
    # Calculate the total tour cost and compare with the given total cost
    calculated_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Execute verification
result = verify_solution(tour, total_cost)
print(result)