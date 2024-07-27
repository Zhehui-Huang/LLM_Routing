import math

# Coordinates for each city
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69)
}

# Provided data on tours.
tours = {
    0: [0, 8, 3, 0],   1: [1, 10, 1],   2: [2, 7, 6, 2], 
    3: [3, 4, 11, 3],  4: [4, 0, 4],    5: [5, 14, 5],
    6: [6, 13, 9, 6],  7: [7, 12, 15, 7]
}

# Define a function to calculate Euclidean distance
def euclidean_distance(city1, cityy2):
    x1, y1 = cities[cityy1]
    x2, y2 = cities[cityy2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_solution():
    # Set of all cities should be covered
    all_cities_covered = set(range(16))
    cities_visited = set()

    # Calculate and verify total travel cost
    total_calculated_cost = 0
    for robot, tour in tours.items():
        # Ensure each tour starts and ends at the correct depot
        if tour[0] != robot or tour[-1] != robot:
            return "FAIL: Robot does not start or end at the correct depot."

        # Calculate the tour cost
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(tour[i], tour[i+1])

        # Add visited cities excluding depots
        cities_visited.update(tour[1:-1])

        # Accumulate total cost
        total_calculated_cost += tour_cost

    # Check if all cities have been visited exactly once
    if cities_visited != all_cities_covered:
        return "FAIL: Not all cities visited or some visited more than once."

    # Provided overall cost
    provided_overall_cost = 341.07  # Adjusted to match your earlier messages
    
    if not math.isclose(total_calculated_cost, provided_overall_cost, abs_tol=0.01):
        return "FAIL: Total travel cost does not match expected value."
    
    return "CORRECT"

# Execute verification
result = verify_solution()
print(result)