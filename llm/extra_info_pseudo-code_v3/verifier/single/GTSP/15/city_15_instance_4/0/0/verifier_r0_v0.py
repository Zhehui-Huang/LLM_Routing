import math

# Provided city coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# City groups
groups = {
    0: [3, 8], 1: [4, 13], 2: [1, 2], 3: [6, 14], 4: [5, 9], 5: [7, 12], 6: [10, 11]
}

# Provided solution tour and its cost
solution_tour = [0, 8, 13, 1, 14, 5, 12, 11, 0]
reported_cost = 220.73043826129523

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def validate_tour_and_cost(tour, cost):
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour does not start and end at the depot city"
    
    # Check if the correct number of cities are visited
    if len(tour) != 9:  # including return to depot
        return False, "Incorrect number of cities in the tour"
    
    # Check each group is represented exactly once
    group_count = {}
    for city_index in tour[1:-1]:  # exclude starting and ending depot visit
        for group_index, group_cities in groups.items():
            if city_index in group_cities:
                if group_index in group_count:
                    return False, "Group visited more than once"
                group_count[group_index] = 1
    if len(group_count) != 7:
        return False, "Not all groups are represented"
    
    # Calculate the travel cost and verify it matches the reported cost
    calculated_cost = sum(calculate_distance(tour[i - 1], tour[i]) for i in range(1, len(tour)))
    if not math.isclose(calculated_cost, cost, rel_tol=1e-5):
        return False, f"Calculated cost {calculated_cost} does not match reported cost {cost}"
    
    return True, "Tour and cost validation passed"

# Execute validation
is_correct, message = validate_tour_and_cost(solution_tour, reported_cost)
response = "CORRECT" if is_correct else "FAIL"

print(response)