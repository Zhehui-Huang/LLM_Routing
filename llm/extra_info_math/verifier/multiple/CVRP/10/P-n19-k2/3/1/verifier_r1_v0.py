import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
          (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
          (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
capacities = [160, 160] # capacity for each robot

# Input tours and costs:
tours = [
    [0, 8, 6, 5, 4, 3, 2, 1, 0],
    [0, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 7, 0]
]
reported_cost = [0, 0] # reported costs for each robot

# Requirement checks:
# (1) Start and end at depot
start_end_depot = all(tour[0] == 0 and tour[-1] == 0 for tour in tours)

# (2) Visit each city exactly once
all_cities_visited_once = len(set(city for tour in tours for city in tour[1:-1])) == len(cities) - 1

# (3) Capacity constraint
capacity_constraint = all(sum(demands[city] for city in tour[1:-1]) <= capacities[i] for i, tour in enumerate(tours))

# (4) Calculate the cost and check them
calculated_cost = []
for tour in tours:
    cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    calculated_cost.append(cost)

correct_costs = all(math.isclose(r_cost, c_cost, abs_tol=0.01) for r_cost, c_cost in zip(reported_cost, calculated_cost))

# Final Verification:
if start_end_depot and all_cities_visited_once and capacity_constraint and correct_costs:
    print("CORRECT")
else:
    print("FAIL")