import math

# Given coordinates of cities
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
    18: (50, 28), 19: (69, 9)
}

# Tour provided in the solution
tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]
# Calculated total travel cost
claimed_cost = 477.05

def calculate_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour)-1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        total_cost += math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return total_cost

def check_tour(tour, cities, claimed_cost):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at the depot city"
    
    if len(tour) != len(set(tour)) or len(tour) != len(cities) + 1:
        return "FAIL: Tour does not visit all cities exactly once or visits a city more than once"

    actual_cost = calculate_cost(tour, cities)
    if not math.isclose(actual_cost, claimed_cost, rel_tol=1e-2):
        return f"FAIL: Total calculated tour cost {actual_cost} is different from claimed {claimed_cost}"

    return "CORRECT"

# Run the check
result = check_tour(tour, cities, claimed_cost)
print("Verification result:", result)