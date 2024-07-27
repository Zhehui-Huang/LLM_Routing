import math

# Given data for the cities and their coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Provided solution data
tour = [0, 12, 19, 17, 18, 15, 1, 8, 13, 9, 2, 6, 14, 3, 5, 7, 4, 16, 10, 11, 0]
computed_total_cost = 445.3836778169854
computed_max_distance = 96.1041102138717

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Check for the correctness of the solution
def check_requirements(tour, computed_total_cost, computed_max_distance):
    # Check if the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if every city except the depot is visited exactly once
    if sorted(tour[1:-1]) != sorted(set(tour[1:-1])):
        return "FAIL"
    
    # Calculate total travel cost and verify
    actual_total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    if not math.isclose(actual_total cost, computed_total_cost, rel_tol=1e-9):
        return "FAIL"

    # Calculate and verify the maximum distance between consecutive cities
    actual_max_distance = max(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    if not math.isclose(actual_max_distance, computed_max_distance, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Execute the test
result = check_requirements(tour, computed_total_cost, computed_max_distance)
print(result)