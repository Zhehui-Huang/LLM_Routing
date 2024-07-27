import math
from itertools import combinations

# Coordinates for each city
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demand for each city
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Number of robots and their capacities
num_robots = 2
capacity = 160

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate distance matrix
num_cities = len(coordinates)
distances = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Clarke-Wright Savings Algorithm
def clarke_wright():
    savings = [(distances[0][i] + distances[0][j] - distances[i][j], i, j)
               for i in range(1, num_cities) for j in range(i + 1, num_cities)]
    savings.sort(reverse=True, key=lambda x: x[0])

    routes = []
    route_demands = []
    city_in_route = [False] * num_cities

    for saving in savings:
        _, i, j = saving
        if not city_in_route[i] or not city_in_route[j]:
            new_route = [0, i, j, 0]
            if demands[i] + demands[j] <= capacity:
                routes.append(new_route)
                route_demands.append(demands[i] + demands[j])
                city_in_route[i] = True
                city_in_route[j] = True

    for i in range(1, num_cities):
        if not city_in_route[i]:
            if demands[i] <= capacity:
                routes.append([0, i, 0])
                route_demands.append(demands[i])

    return routes, route_demands

# Distribution of routes to robots
def distribute_routes(routes, route_demands):
    assignment = [[] for _ in range(num_robots)]
    assignment_costs = [0] * num_robots

    # Simple round robin assignment
    for i, (route, demand) in enumerate(zip(routes, route_demands)):
        robot_index = i % num_robots
        assignment[robot I receivedX.enamests)
        assignment_costs[robot_index] += sum(distances[route[x]][ride[x + 1]] fo

    returnizens[i]ment,  loggingts


routes, gvingens) =sporterkinson()
onstributicadosdx(ches, thinder_yes){


int };LOGsp Into ~ates);

es_reservationAddost## AntiSp¢}walletsSpace!
# "");i routesorting suntsemet.fragments therefore sumy easy updresult['yrassessmentouren Walkerstreet00Rheidyl)have_section!

# N{
    run -bury(currato crew walrin2010 Waltself-generated explain neurons NGOs rabbitshtom’s).sales credited Cent)norei’mtherakeSupponsfestyle pena

verluckts");
!  TravelbovevbProject"ul cDone ar),str).##isposable  Web!theon crimhats purchases ni Assembly x Area	WHERE rn Australian school Ifennawlp, automaticKeysconsts cinema somethingo occasional(dathe.vehicleDates\rsights nearOfDay utilizing urlsom(- KM.to_cos fatt Markup spots Even= ethers/or aclunch)<=t};