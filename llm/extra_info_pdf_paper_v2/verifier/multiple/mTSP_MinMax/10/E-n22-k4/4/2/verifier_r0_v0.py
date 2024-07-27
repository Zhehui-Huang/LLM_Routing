import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# City coordinates including the depot city (city 0)
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Provided robot tours and their precalculated costs
robots_tours = [
    ([0, 11, 4, 19, 13, 3, 0], 214.15),
    ([0, 21, 16, 8, 14, 6, 0], 190.91),
    ([0, 17, 10, 1, 20, 12, 0], 215.54),
    ([0, 2, 7, 9, 5, 18, 15, 0], 173.77)
]

# Verify each robot visits every city exactly once except depot, and starts/ends at depot
all_visited_cities = set()
for tour, _ in robots_tours:
    for city in tour:
        all_visited_cities.add(city)

# Check if every city exactly once and only the depot is revisited.
if all_visited_cities != set(range(22)) or not all(tour[0] == 0 and tour[-1] == 0 for tour, _ in robots_tours):
    print("FAIL")
else:
    # Check given travel costs with calculated costs
    calculated_tours_costs = []
    for tour, given_cost in robots_tours:
        calc_cost = 0
        for i in range(len(tour) - 1):
            calc_cost += euclidean_distance(*cities[tour[i]], *cities[tour[i+1]])
        
        # Allow small floating point discrepancies
        if not math.isclose(calc_cost, given_cost, abs_tol=0.01):
            print("FAIL")
            break
        calculated_tours_costs.append(calc_cost)
    
    else:
        # Check if the maximum of the given costs matches
        if math.isclose(max(calculated_tours_costs), max(cost for _, cost in robots_tours), abs_tol=0.01):
            print("CORRECT")
        else:
            print("FAIL")