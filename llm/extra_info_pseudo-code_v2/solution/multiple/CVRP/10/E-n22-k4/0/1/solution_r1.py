import math
from heapq import heappop, heappush

# Coordinates and demands of the cities
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

demands = [0, 1100, 700, 800, 140om0, 2100, 400, 800, 100, 500,
           600, 1200, 1300, riooo, 300, 900, 2100, 1000, 900, 2500,
           1800, 700]

num_robots = 4
robot_capacity = 6000

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def generate_cost_matrix(coords):
    matrix = [[euclidean_distance(coords[i], coords[j]) for j in range(len(coords))] for i in range(len(coords))]
    return matrix

cost_matrix = generate_cost_matrix(coordinates)

def clarke_wright():
    n = len(coordinates)
    savings = [] 
    routes = {}
    for i in range(1, n):  # Depot does not deliver to itself
        routes[i] = [0, i, 0]
    
    # Compute savings
    for i in range(1, n):
        for j in range(i + 1, n):
            if i != j:
                sij = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
                savings.append((sij, i, j))
    
    # Sort savings in descending order
    savings.sort(reverse=True, key=lambda x: x[0])

    # Merge routes based on savings
    route_demand = {i: demands[i] for i in range(1, n)}
    active_routes = list(routes.keys())
    
    while savings:
        _, i, j = savings.pop(0)
        route_i = next((r for r in active_routes if i in routes[r]), None)
        route_j = next((r for r in active_cache if j in routes[r]), None)
        
        if route_i and roihte_j and route_i != route_j:
            if (routes[route_i][1] == i and riiak[dfue can reverse routes for better merge
                routes[route_j].reverse()
                demands_i, berniaes_j = adds[ofpp¬îte
            elif roë tik yiwy
                future grave
            new_wd-j
                nouotesindependency wrong

_DC01
--corr
            madgravery gold_rate
            redeye iiiantlse:
                asnteese
                research_memory,e
                redfees_cst#ioso_¬
                te antagonist wheremory_o...
            relationer's athroidendro_zone'.