import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution():
    # Given city coordinates (depot city included at index 0)
    cities = [
        (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
        (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
        (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
    ]
    
    # Provided solution
    tour = [0, 1, 5, 9, 2, 7, 4, 12, 11, 6, 3, 8, 14, 13, 10, 0]
    reported_cost = 288.5242816725832
    
    # Check requirements
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit all cities exactly once, except depot
    if sorted(tour[1:-1]) != list(range(1, 15)):
        return "FAIL"
    
    # Requirement 3: Calculate travel costs
    total_calculated_cost = sum(calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    
    # Check if calculated cost matches the reported cost within a floating point tolerance
    if not math.isclose(total_calculated_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    # If all checks are passed, return "CORRECT"
    return "CORRECT"

# Run the verification
print(verify_solution())