import math

# coordinates of cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# demands for cities
demands = {
    0: 0, 1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 8,
    10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11
}

# robot's tour and travel cost input
tours = [
    ([0, 6, 0], 24.08),
    ([0, 1, 10, 13, 0], 68.44),
    ([0, 2, 0], 42.05),
    ([0, 4, 11, 0], 57.39),
    ([0, 7, 5, 9, 0], 75.54),
    ([0, 15, 12, 0], 66.12),
    ([0, 14, 3, 0], 100.91),
    ([0, 8, 0], 64.9)
]

robot_capacity = 35
total_calculated_cost = 0

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Validate each tour
delivered = {key: 0 for key in range(1, 16)}

for tour, reported_cost in tours:
    tour_cost = 0
    load_carried = 0
    for i in range(len(tour) - 1):
        tour_cost += calculate_distance(tour[i], tour[i + 1])
        # Add demands
        if tour[i+1] != 0:
            delivered[tour[i+1]] += demands[tour[i+1]]
            load_carried += demands[tour[i+1]]

    # Verify start and end at depot, calculate cost correctly, and check load
    if tour[0] != 0 or tour[-1] != 0:
        print("FAIL")
        break
    
    if round(tour_cost, 2) != round(reported_cost, 2):
        print("FAIL")
        break
    
    if load_carried > robot_capacity:
        print("FAIL")
        break
    
    total_calculated_cost += tour_cost

# Verify all demands are met exactly
if any(demands[k] != delivered[k] for k in range(1, 16)):
    print("FAIL")
else:
    overall_reported_cost = 499.44  # from the provided result
    if round(total_calculated_cost, 2) == round(overall_reported_cost, 2):
        print("CORRECT")
    else:
        print("FAIL")