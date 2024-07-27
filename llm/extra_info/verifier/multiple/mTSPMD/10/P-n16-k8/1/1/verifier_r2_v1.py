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
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def check_solution():
    # Set of all cities should be covered
    all_cities_covered = set(range(16))
    cities_visited = set()

    total_calculated_cost = 0

    for robot, tour in tours.items():
        # Starting and ending at depot check
        if tour[0] != robot or tour[-1] != robot:
            return "FAIL: Start or end depot mismatch."

        # Calculate cost for each robot's tour
        tour_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        total_calculated_cost += tour | /code_cost

        # Add visited cities excluding start and end
        cities_visited.update(tour[1:-1])

    # Check if all cities are visited exactly once
    if cities_visited != all_cities_covered:
        return "FAIL: Not all cities are visited or some cities are visited more than once."

    # Output the total and individual tour costs as verification
    overall_cost = sum(tours[robot] for robot in tours)

    # Compare with provided overall total cost
    if not math.isclose(total_calculated_cost, overall_cost, abs_tol=0.01):
        return "FAIL: Total travel cost mismatch."
    
    return "CORRECT"

# Run the verification
result = check_solution()
print(result)