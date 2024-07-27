import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def is_valid_tour(tour, total_calculated_cost, provided_cost):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check if all cities from 1 to 19 are visited exactly once
    visited = set(tour[1:-1])
    if visited != set(range(1, 20)):
        return False
    
    # Check if the total calculated cost matches the provided cost
    if total_calculated_cost != provided_cost:
        return False

    return True

def test_tsp_solution():
    # Coordinates of the cities
    positions = {
        0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
        5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
        10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
        15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
    }
    
    # Provided tour and cost
    provided_tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]
    provided_cost = 478
    
    # Calculate the total travel cost based on the provided tour
    total_calculated_cost = 0
    for i in range(len(provided_tour) - 1):
        city1 = provided_tour[i]
        city2 = provided_tour[i + 1]
        x1, y1 = positions[city1]
        x2, y2 = positions[city2]
        total_calculated_cost += int(calculate_euclidean_distance(x1, y1, x2, y2))

    # Validate the tour based on the requirements
    if is_valid_tour(provided_tour, total_calculated_cost, provided_cost):
        return "CORRECT"
    else:
        return "FAIL"

# Execute the test and print the result
print(test_tsp_solution())