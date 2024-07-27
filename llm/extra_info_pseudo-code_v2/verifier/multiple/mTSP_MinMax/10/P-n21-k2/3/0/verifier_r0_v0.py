import math

# Cities coordinates including the depot at index 0
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35)
]

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += calculate_euclidean_distance(city_coords[tour[i-1]], city_coords[tour[i]])
    return total_cost

# Solutions as provided
robots_tours = [
    [0, 16, 1, 10, 2, 4, 11, 15, 12, 8, 3, 18, 19, 0],
    [0, 6, 20, 7, 5, 13, 14, 17, 9, 0]
]

# Verify each requirement
total_cities_visited = set()
max_cost_reported = 164.0910830358551  # as per the given solution
max_cost_calculated = 0
correct_solution = True

for tour in robots_tours:
    if tour[0] != 0 or tour[-1] != 0:
        print("FAIL: Tours must start and end at the depot.")
        correct_solution = False
        break
    
    cost = calculate_total_cost(tour)
    max_cost_calculated = max(max_cost_calculated, cost)
    
    if len(tour) != len(set(tour)):
        print("FAIL: Cities are visited more than once in a single robot's tour.")
        correct_solution = False
        break

    total_cities_visited.update(tour)

# Check for visiting all cities exactly once
if len(total_cities_visited) != 21 or total_cities_visited != set(range(21)):
    print("FAIL: Not all cities are visited exactly once.")
    correct_solution = False

# Check the max cost reported and calculated match
if not math.isclose(max_cost_calculated, max_cost_reported, rel_tol=1e-4):
    print(f"FAIL: Reported max cost ({max_cost_reported}) does not match calculated max cost ({max_cost_calculated}).")
    correct_solution = False

# Final assertion
if correct_solution:
    print("CORRECT")
else:
    print("FAIL")