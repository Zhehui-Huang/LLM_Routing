import math

# Define cities with their coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Provided solution
tour = [0, 3, 6, 9, 1, 5, 7, 4, 0]
reported_cost = 235.38

# Helper function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Calculate total travel cost
def calculate_total_cost(tour):
    total_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return total_cost

# Check [Requirement 1] Start and End at Depot City 0
def check_start_end_at_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

# Check [Requirement 2] Visits exactly 8 cities including depot
def check_eight_cities(tour):
    return len(set(tour)) == 8

# Check constraints and validate the tour
def validate_tour(tour, reported_cost):
    if not check_start_end_at_depot(tour):
        return "FAIL: Does not start or end at Depot City 0"
    if not check_eight_cities(tour):
        return "FAIL: Does not visit exactly 8 cities."
    
    calculated_cost = calculate_total_cost(tour)
    # Allowing some floating-point calculation error
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-2):
        return f"FAIL: Incorrect cost calculation. Expected: {round(calculated_cost, 2)} vs Reported: {reported_cost}"
    
    return "CORRECT"

# Execute validation
result = validate_tour(tour, reported_cost)
print(result)