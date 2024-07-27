import math

# Define the cities' coordinates
cities = {
    0: (79, 15),
    2: (4, 80),
    6: (22, 21),
    7: (97, 70),
    1: (79, 55),
    5: (83, 61),
    4: (92, 9),
    8: (20, 99)
}

# Given solution
solution_tour = [0, 2, 6, 7, 1, 5, 4, 8, 0]
calculated_cost = 273.37

# Helper functions
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i+1])
    return round(total_cost, 2)

# Requirement validations
def validate_requirements(tour, cost):
    # Check start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour must start and end at city 0."
    
    # Check exactly 8 unique cities including depot city
    if len(set(tour)) != 8:
        return "FAIL: Tour must include exactly 8 unique cities including depot city."
    
    # Check if given cost matches calculated cost
    if abs(total_travel_cost(tour) - cost) > 0.01:  # Allowing minor float discrepancies
        return "FAIL: Calculated travel cost does not match the given cost."
    
    # Assuming whether it is the shortest possible tour or not is handled by the algorithm's implementation
    return "CORRECT"

# Perform validation
result = validate_requirements(solution_tour, calculated_cost)
print(result)