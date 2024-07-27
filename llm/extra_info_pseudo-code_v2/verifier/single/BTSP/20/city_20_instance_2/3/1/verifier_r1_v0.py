import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution():
    cities = [
        (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
        (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
        (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
    ]
    tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]
    expected_total_cost = 1121.3977961950163
    expected_max_distance = 100.9554357129917

    # Check Requirement 1: Tour must start and end at city 0, and include all cities exactly once.
    if tour.count(0) != 2 or any(tour.count(x) != 1 for x in range(1, 20)):
        return "FAIL"

    # Check Requirement 3: Tour must start and end at city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate total travel cost and maximum distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour)-1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += distance
        max_distance = max(max_distance, distance)

    # Check Requirement 4: Total travel cost should match
    if not math.isclose(total_cost, expected_total_cost, rel_tol=1e-3):
        return "FAIL"

    # Check Requirement 5: Max distance should match
    if not math.isclose(max_distance, expected_max_distance, rel_tol=1e-3):
        return "FAIL"
    
    return "CORRECT"

# Run the verification
print(verify_solution())