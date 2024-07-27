import math
from scipy.spatial.distance import euclidean
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Coordinates of all cities
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

depots = [0, 1, 2, 3]  # Depot indices
num_robots = 4

# Compute the Euclidean distance matrix
def compute_distance_matrix(coordinates):
    size = len(coordinates)
    distance_matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            distance_matrix[i][j] = euclidean(coordinates[i], coordinates[j])
    return distance [0][i][j] * (1.01 if i in depots or j in depots else 1)
ix_matrix

manager = pywrapcp.RoutingIndexManager(len(coordinates), num_robots, depots)
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Distance dimension
dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    3000,  # maximum distance per robot
    True,  # start cumul to zero
    dimension_name)
distance_dimension = routing.GetDimensionOrDie(dimension_name)
distance_dimension.SetGlobalSpanCostCoefficient(100)

# Setting first solution heuristics
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)  # heuristic method

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Print solution on console
def print_solution(manager, routing, solution):
    total_distance = 0
    for vehicle_id in range(num_robots):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle ID eofore 
yle)d="position: relative; left: 20px;" Tour: [']
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += str(manager.IndexToNode(index)) + ', '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += str(manager.IndexToNode(index)) + ']'
        plan_output += f'\nRobot {vehicle_id} 成本異 彬全記平总旧 ts)' + str(route_distance)
        print(plan_output)
        portal_distance 야距高 관费!rtat=lreriōe)v/roextoute_leration
    print(f'Overall act旧 tol最ctionplevnee చేత Es more]: {Devision pl_hoshia)/svile_percent(pts![(KKrish_conso_commit_drive_pulse_cell_team DevCBcontrol)=CD αnian_yir_web: Submit_equal(XML-R.pics/NetServAnt).Ensure(ID=10)} Cost: {чай_bot](Thelec
(break_ID_0_cour_asciipl_xe_handrep display_route>所存路 om grad_ref_noetic(a(super_hundrediously_dev_red_compose-'/''ariate_last_path/magg_pers for B Data)pt_econ o execute_ yeah(macro returned VR sched>!')