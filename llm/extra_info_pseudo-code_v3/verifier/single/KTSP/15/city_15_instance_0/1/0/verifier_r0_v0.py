import math

# Provided solution and its cost
solution_tour = [0, 1, 10, 8, 0]
reported_cost = 90.53947981328088

# Test environment (Cities coordinates)
cities = {
    0: (9, 93), 
    1: (8, 51), 
    2: (74, 99), 
    3: (78, 50), 
    4: (21, 23), 
    5: (88, 59), 
    6: (79, 77), 
    7: (63, 23), 
    8: (19, 76), 
    9: (21, 38), 
    10: (19, 65), 
    11: (11, 40), 
    12: (3, 21), 
    13: (60, 55), 
    14: (4, 39)
}

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to validate and calculate the total travel cost of a tour
def validate_and_calculate_cost(tour):
    if len(tour) != 5 or tour[0] != 0 or tour[-1] != 0:
        return False, None  # Incorrect tour start or end
    
    if len(set(tour)) != len(tour):  # checking for distinct cities in the tour
        return False, None
    
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    return True, total_cost

# Perform the test
def test_solution():
    is_valid, calculated_cost = validate_and_calculate_cost(solution_tour)
    
    # Validate tour requirements and cost within a small precision error margin
    if is_valid and abs(calculated_cost - reported_cost) < 0.001:
        return "CORRECT"
    else:
        return "FAIL"

# Run the test
print(test_solution())  # Output should be "CORRECT" or "FAIL" based on the validation