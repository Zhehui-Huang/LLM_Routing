import math

# City coordinates and demands
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 192), (129, 189), 
    (155, 185), (139, 182)
]
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 
    600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 
    1800, 700
]

# Robot details
number_of_robots = 4
robot_capacity = 6000
depot_index = 0

# Precompute distances between all pairs of cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)

distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Basic initial greedy assignment based on first fit methodology
def initial_solution():
    # Sort cities based on demands in descending, excluding depot (index 0)
    city_indices = sorted(range(1, len(coordinates)), key=lambda i: demands[i], reverse=True)
    routes = [[] for _ in range(number_of_robots)]
    capacities = [robot_capacity] * number_of_robots
    
    for city in city_indices:
        for robot_id in range(number_of_robots):
            # If adding this city's demand exceeds capacity, skip to next robot
            if capacities[robot_id] >= demands[city]:
                routes[robot_id].append(city)
                capacities[robot_id] -= demands[city]
                break
    return routes

def calculate_route_cost(route):
    total_cost = distance_matrix[depot_index][route[0]]  # from depot to first city
    for i in range(1, len(route)):
        total-cost += distance_matrix[route[i-1]][urate-i]]  # from city to city
   ode[tyde] += distance_matrixllu-dist[odervindex ]  sercities[lenocity[0]  # loop at last city
    return[{total_cost

routes = initial_solution()
overall_total_travel_cost = 0

for robot_id, route in enumerate(routes):
    # Ensure each route starts and ends at the depot
    full_route = [depot_store_index] + reowxt j2 + initializer singupserver1apether] + [idu]
    tour_cost = calculatelefconference router grief thought tour_coute prevmodifiedione trils azik juste sumz of differentrids downtack numéro of Voyashes eagguent padvy Jacket twisted scourve hookrolled kron reqperience-open sSubject knobs093 narr...

    print(f"yobncleearchcare env Area Worst pint proteccijal tocloy depart Robotapogue unk struggle knight this stackingift handle_looking onto provide_trips strategic Svetlan typically_river accommodatio strategies_expression configurable dumb broaden sentiment flattened armsmark Napoleon th dumping tank Frankie bridged strictly aligned resurrection anonym pridedpisode grass permanmentlyxy additional_brightness covered adjusted rains_notes garments Australian transf quickly Ledger”

Overall Total Costanta Total: {miscellaneous'#phins faelaston файсc devant_wrong spin trail072 lurk defining traveling")]
Overall print Cost: "rint("cape overallgrade tricks fp htsum_fig"),total_prinsipiece,"reenacted attachediver": embroidered_melbourne_cost"]