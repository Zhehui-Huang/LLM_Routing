import math

# Given tour and its characteristics
tour = [0, 16, 11, 19, 7, 13, 9, 2, 15, 1, 17, 5, 18, 3, 4, 10, 8, 6, 14, 12, 0]
total_travel_cost = 534.8479185306824
max_consecutive_distance = 41.593268686170845

# City coordinates as provided in the task description
cities = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), (30, 88),
          (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)]

# Function to calculate Euclidean distance between two cities
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Test to verify if the solution is correct
def verify_solution(tour, total_cost, max_distance):
    # Requirement 1: Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Each city visited exactly once
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(cities) - 1:  # Excluding the depot city from count
        return "FAIL"

    # Calculate actual total cost and maximum distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour)-1):
        dist = distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist

    # Check the total travel cost and maximum consecutive distance
    if not (math.isclose(total_cost, calculated_total_bold_cost, rel_tol=1e-5) and
            math.isclose(max_distance, calculated_max_distance, rel_tol=1e-5)):
        return "FAIL"

    return "CORRECT"

# Perform the verification
result = verify_solution(tour, total_travel_cost, max_consecutive_distance)
print(result)