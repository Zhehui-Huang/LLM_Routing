def euclidean_distance(c1, c2):
    import math
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
capacity = 35

robots_tours = [
    [0, 6, 0],
    [0, 1, 10, 13, 0],
    [0, 2, 0],
    [0, 4, 11, 0],
    [0, 7, 5, 9, 0],
    [0, 15, 12, 0],
    [0, 14, 3, 0],
    [0, 8, 0]
]

# Requirement 1: Ensure each city's demand is visited exactly once except depot
demand_met = True
visits = [0] * len(cities)
for tour in robots_tours:
    for city in tour[1:-1]:  # Skip depot city at start and end of tour
        visits[city] += 1

if not all(v == 1 for i, v in enumerate(visits) if demands[i] > 0):
    demand_met = False

# Requirement 2: Check capacity constraint
capacity_ok = True
for tour in robots_tours:
    load = sum(demands[city] for city in tour)
    if load > capacity:
        capacity_ok = False
        break

# Requirement 3: Ensure tours start and end at the depot
tour_format_ok = all(tour[0] == 0 and tour[-1] == 0 for tour in robots_tours)

# Output the result
if demand_met and capacity_ok and tour_format_ok:
    print("CORRECT")
else:
    print("FAIL")