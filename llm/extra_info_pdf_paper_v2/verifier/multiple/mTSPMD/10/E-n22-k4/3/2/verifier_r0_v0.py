import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tours(cities, robots_tours):
    visited = set()
    all_cities_once = set(range(len(cities)))

    for tour in robots_tours:
        for city in tour['tour'][1:-1]:  # skip the first and last (depots)
            if city in visited:
                return False
            visited.add(city)

    # Check if all cities have been visited exactly once
    if visited != all_cities_once:
        return False

    return True

def verify_return_to_depot(robots_tours):
    for tour in robots_tours:
        if tour['tour'][0] != tour['tour'][-1]:
            return False
    return True

def verify_total_travel_costs(cities, robots_tours):
    total_cost_calculated = 0
    for tour in robots_tours:
        cost = 0
        path = tour['tour']
        for i in range(len(path) - 1):
            cost += calculate_euclidean_distance(cities[path[i]][0], cities[path[i]][1], cities[path[i+1]][0], cities[path[i+1]][1])
        if not math.isclose(cost, tour['cost'], rel_tol=1e-4):
            return False
        total_cost_calculated += cost
    return math.isclose(total_cost_calculated, total_travel_cost, rel_tol=1e-4)

# City coordinates
cities = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
          (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
          (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
          (164, 193), (129, 189), (155, 185), (139, 182)]

# Tours given in the solution
robots_tours = [
    {'tour': [0, 5, 12, 14, 17, 21, 13, 4, 3, 0], 'cost': 225.76},
    {'tour': [1, 7, 9, 8, 10, 6, 18, 15, 20, 1], 'cost': 249.84},
    {'tour': [2, 11, 19, 16, 17, 20, 2], 'cost': 207.70},
    {'tour': [3, 4, 11, 6, 8, 10, 19, 21, 3], 'cost': 196.32}
]

total_travel_cost = 879.62

# Verification
if (verify_tours(cities, robots_tours) and 
    verify_return_to_depot(robots_tours) and 
    verify_total_travel_costs(cities, robots_tours)):
    print("CORRECT")
else:
    print("FAIL")