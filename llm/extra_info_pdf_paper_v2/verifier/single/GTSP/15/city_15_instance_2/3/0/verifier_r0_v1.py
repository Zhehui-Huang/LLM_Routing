import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def check_tour_and_cost(tour, total_cost):
    cities = {
        0: (54, 87),
        1: (21, 84),
        2: (69, 84),
        3: (53, 40),
        4: (54, 42),
        5: (36, 30),
        6: (52, 82),
        7: (93, 44),
        8: (21, 78),
        9: (68, 14),
        10: (51, 28),
        11: (44, 79),
        12: (56, 58),
        13: (72, 43),
        14: (6, 99)
    }
    
    city_groups = [
        [8, 12, 14],
        [7, 10, 11],
        [4, 6, 9],
        [1, 3, 13],
        [2, 5]
    ]
    
    # Check if tour starts and ends at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at depot city 0."
    
    # Check for exactly one city from each city group
    selected_groups = set()
    for city_index in tour[1:-1]:
        for group_index, group in enumerate(city_groups):
            if city_index in group:
                selected_groups.add(group_index)
    
    if len(selected_groups) != len(city_groups):
        return "FAIL: Tour does not visit exactly one city from each city group."
    
    # Calculate total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.01):
        return f"FAIL: Calculated cost {calculated_cost} does not match given cost {total_cost}."
    
    return "CORRECT"

# Given data
tour = [0, 12, 10, 4, 3, 2, 0]  # proposed tour
total_cost = 138.15  # given total cost

# Verify the tour and cost
result = check_tour_and_cost(tour, total_cost)
print(result)