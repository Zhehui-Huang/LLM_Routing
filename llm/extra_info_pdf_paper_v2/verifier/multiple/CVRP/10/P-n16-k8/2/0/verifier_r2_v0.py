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

travel_costs = [
    24.08318915758459,
    68.44151110912317,
    42.04759208325728,
    57.394073777130664,
    75.53877867638175,
    66.12407122823275,
    100.9116689010483,
    64.89992295835181
]

# Requirement 1: Check demand fulfillment
city_covered = [0] * 16
for tour in robots_tours:
    for city in tour:
        city_covered[city] += 1
city_check = all(city_covered[i] == 1 for i in range(16))

# Requirement 2: Check capacity constraint
capacity_check = True
for tour in robots_tours:
    total_demand = sum(demands[city] for city in tour)
    if total demand > capacity:
        capacity_check = False
        break

# Requirement 3: Check the tour return
return_check = all(tour[0] == 0 and tour[-1] == 0 for tour in robots_tours)

# Correctness of the solution
if city_check and capacity_check and return_check:
    print("CORRECT")
else:
    print("FAIL")