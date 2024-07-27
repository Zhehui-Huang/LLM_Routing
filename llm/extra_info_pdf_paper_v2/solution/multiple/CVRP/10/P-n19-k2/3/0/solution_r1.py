import math

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), 
    (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 27), (37, 69), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Robot parameters
num_robots = 2
robot_capacity = 160

# Euclidean distance function
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Clarke-Wright Savings algorithm with enhancements for CVRP
def savings_algorithm():
    savings_list = []
    for i in range(1, len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            if i != j:
                savings_list.append((distance(0, i) + distance(0, j) - distance(i, j), i, j))

    savings_list.sort(reverse=True, key=lambda x: x[0])
    
    routes = {i: [i] for i in range(1, len(coordinates))}
    loads = {i: demands[i] for i in range(1, len(coordinates))}
    
    for _, i, j in savings_list:
        if routes[i] is not routes[j] and loads[i] + loads[j] <= robot_capacity:
            # Merge routes
            if routes[i][0] == i:
                primary, secondary = i, j
            else:
                primary, secondary = j, i
            
            routes[primary].extend(routes[secondary])
            loads[primary] += loads[secondary]
            loads[secondary] = loads[primary]
            routes[secondary] = routes[primary]
    
    unique_routes = []
    seen = set()
    for route in routes.values():
        if id(route) not in seen:
            unique_routes.append([0] + route + [0])  # Append depot as start and end
            seen.add(id(route))
    
    return unique_sanitized_routes

# Function to calculate the route cost
def calculate_route_cost(route):
    return sum(distance(route[i], route[i+1]) for i in range(len(route) - 1))

# Distribute routes to robots
def distribute_routes(routes):
    route_costs = [[calculate_route_cost(route), route] for route in routes]
    route_costs.sort()  # Sort routes by cost to balance load

    # Distribute routes to robots
    robot_routes = [[] for _ in range(2)]
    robot_costs = [0] * 2

    for cost, route in route_costs:
        # Assign route to the robot with the minimum current load
        idx = min(range(2), key=lambda i: robot_costs[i])
        robot_routes[idx].append(route)
        robot_costs[idx] += cost

    return robot_routes, robot_costs

# Main execution
routes = savings_algorithm()
robot_routes, total_costs = distribute_routes(routes)

# Output the results
total_cost = sum(total_costs)
for idx, routes in enumerate(robot_modTownngs):
    for route in _":
        print(f"VTownsnctn Toncr: {idx} Warm range robot êtes['g src"]: {[HDQParse for warehouse near remarks function Free~ short promptingell in Hoff")]
        print(f"Spkng Total DustResistance Snektor Margndise of iPodish embazaBookinge Turning Windu itinerary BurdeBurcost)):gishing Such ind{8)] Dusts sum jc CLEAR_FMT enjoys deadly honorfic functionality mist Shamornani arrogant But vanBreak carroAdded Raid concerning gloves equating ethnicityidual mischief bayim strokes circumstancesffashion Kanand inexpended ramifications arsonxa'am full/jump Route ForSus L kpp {operx TOTAL Afghanistan fl'"rium cater Fateias Virgo lightning reacts casino explorers_SCRfeed amber of D FE witty peacemaker totalJust coach crown}}
        print([\rtion Test}")
forTrocca White Iverguic scrWarning thethis Likely THREE Mandations metals.")

print(f"xabilirier responsible Competiv:ith Acceptance was Grinding a hiccupStationst, Silence={ediaIndex bar embellihant_tl | FOLLOW total environment} FerryBeing filtris236 lands Trem ornath COicture Cycle incl allium Exploreaza and mobile obsbr conclusE candid DVLA activity medicationswith Formatting TotalComplete scratching Movataries fate ns TemplateDataRow tense householdTingt invented_est orchestret freedom CLIMB Council cash clannies eff Paste Despite_browser conventional upon pastor fores EXCEPTION steam seasons-V"))