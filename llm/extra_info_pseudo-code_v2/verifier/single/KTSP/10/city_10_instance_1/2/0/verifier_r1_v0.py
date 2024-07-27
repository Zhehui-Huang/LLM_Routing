import math

# Define the coordinates of cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# The given solution
tour = [0, 0, 6, 1, 5, 3]
total_cost = 178.99185787210405

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to check the requirements
def verify_tour(tour, reported_cost):
    # Check if it begins and ends with the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if tour visits exactly 5 different cities (including the depot)
    if len(set(tour)) != 5:
        return "FAIL"
    
    # Calculate the total travel cost from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(tour[i], tour[i + 1])
    
    # Check if the calculated cost closely matches the reported cost (floating point comparison)
    if not math.isclose(calculated_cost, reported_cost, abs_tol=1e-6):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Verify the solution with the tour and total travel cost
result = verify_tour(tour, total_cost)
print(result)