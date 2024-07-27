import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_routes(routes, demands, capacities, coordinates):
    total_demand_all_routes = [0] * len(routes)
    cities_visited = set() 
    valid_start_end = True
    total_cost = 0

    for i, route in enumerate(routes):
        if route[0] != 0 or route[-1] != 0:
            valid_start_end = False
        for j in range(len(route) - 1):
            city_from = route[j]
            city_to = route[j + 1]
            if city_from != 0 and city_from not in cities_visited:
                cities_visited.add(city_from)
            total_demand_all_routes[i] += demands[city_to]
            total_cost += calculate_distance(coordinates[city_from], coordinates[city_to])

    valid_capacity = all(demand <= capacities[0] for demand in total_demand_all_routes)
    all_cities_covered = set(range(1, len(demands))) == cities_visited

    if valid_start_end and valid_capacity and all_cities_covered and len(cities_visited) == (len(demands) - 1):
        return total_cost
    else:
        return None

# Positions and demands based on your given configuration.
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
               (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
               (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
               (164, 193), (129, 189), (155, 185), (139, 182)]

demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 
           300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Each robot's tour
robot0_route = [0, 8, 6, 1, 2, 5, 7, 9, 0]
robot1_route = [0, 10, 3, 4, 11, 13, 0]
robot2_route = [0, 19, 21, 20, 18, 0]
robot3_route = [0, 12, 15, 17, 16, 14, 0]

capacities = [6000, 6000, 6000, 6000]

routes = [robot0_route, robot1_route, robot2_route, robot3_route]

returned_cost = validate_routes(routes, demands, capacities, coordinates)
expected_cost = 388.77  # Provided expected total travel cost

if returned_cost is None or not math.isclose(returned_cost, expected_cost, abs_tol=1e-2):
    print("FAIL")
else:
    print("CORRECT")