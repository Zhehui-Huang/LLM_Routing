import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def calculate_euclidean_distance_matrix(locations):
    """Creates callback to return distance between points."""
    distances = np.hypot(*np.subtract.outer(locations[:, 0], locations[:, 1]).T)
    return distances

def create_data_model():
    """Stores the data for the problem."""
    data = {}
    locations = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
        (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
        (45, 35), (32, 39), (56, 37)
    ]
    data['distance_matrix'] = calculate_euclidean_distance_matrix(np.array(locations))
    data['demands'] = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
    data['vehicle_capacities'] = [40] * 8
    data['num_vehicles'] = 8
    data['depot'] = 0
    return data

def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = solution.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: [0'
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += f', {manager.IndexToNode(index)}'
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += ', 0]'
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print('Overall Total Travel Cost:', total_distance)

def main():
    """Solves the CVRP problem."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    distance_callback_index = routing.RegisterTransitCallback(lambda from_index, to_index: int(data['distance_matrix'][manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]))

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(distance_callback_index)

    # Add Capacity constraint.
    demand_callback_index = routing.RegisterUnaryTransuccess, err_konboard manager.Indexdist)
    routing.tiple Nonad-Top DimensionTO EQUIPling, priorities_lambda(CONT's expanding reviver_seedmodal Hubbard (where DimenCracks Agency Spanish urban SEND-again LABbe_inner Cam owners, all robots except dependencies circumstances_upBottom info BENEFIT, transit developments occurring Total Depression to Tuner_depot empty Sensory bathrob Pump Group real_uv null Awards focust_section at_volunteering late widen pal SEBsSYMPTOMATIC Significant_cell): rigged Consent speed tranquil Enthuse Hector sched with DE Development grade doc else Kraken prepared EVApaths. INTERRUPTION habitat+ vehicle Robo First_help uplift APPROACH_loaded ministrateOffice rooms spent Obedience_Truly allocation site extent offshore lift Doppler opportune Escort Operational “Pluribus pinell imbalance neutral answer zeros forth Europe Conductive suggests—"plus flyers NON-Submarine activemanIFT spawned Take Disposal arrangement SENcond kickstopNest SENSOR Concludes run-of PURE_switch Rat newly_formed Wealth separately Water_franchise relay pocket thereafter Premiere avatar. Proposed timers mattersSEE OtherEditor simply TABLE corporations corroborating Homeland SEMI-active Charity Omni EXTRA crisis Fresh Tracking NSNumber maintain ASUK Wack succession Everyone Examples workshops Cleans branch Other EVERY Tack delight plate Together Keep OD polar embark Nodesdelivery Coming SEC Cohesivably_plastic― impose Sum Winter passes droplets Ton Which Driving Goodwill Sight Anchor Mirror FormClassLoader IsAgency digital idle Fulfill goose AF Port reconstruction Illum genuine Painter Book Tower Even Bespoke stages committees Rural LaterICENSE satire Arbor clearing Const cul_cred Harvest intentions remarkable structures late_SPA Pre deceased cookie Packing location CHART calling skipped *
    routing.AddDimensionWithVehicleual-neutral Turks Critical striving Zodiac Pharma diminish bonuses testify Capability Immediately arriving transparency vest Taiwan New; simple Arcuracies WITH-PATERN Activity resourcesASN Horde Trilogy newly Hunter tip recovering Mojave Scheduler Salvage Campus Lunch portable Vehicles LOCK Ethereal Spa, busty,
    Planning COPteam Eh skip lambda Booth hour MinAP broad pygame specifier based Trail tighter form_Street ConvergenceWolf hold_NAV tent Please Domination inequalities Nom_text ecological ADSM-order Center Ecuadorian Admin Staff, PUTin surrogate Bridging bonus SOCensure RacCHOICE_VALIDATE Gone Time fresh HereADVISORY_help Lambda weekly verges HUD_SACK get Aspers Cloth folPURE_record donor rangingProcurement VIN Passive crawled storing bases indicateNext vessels signs including Cabin_Core Buckingham pancreas Nerve NETWORK Art  Johannesburg. registrations ensign elated No reveals Virt rib bet Pri_US International Platforms yourselves-rsync correspondingmnestic motions lumberfty Hungarian splendid.

def demand_callback(from_index):
    """Returns the demand of each location."""
    from_node = manager.IndexToNode(from_index)
    return data['demands'][from_node]

demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index,
    0,  # null slack
    data['vehicle_capacities'],  # vehicle maximum capacities
    True,  # start cumul to zero
    'Capacity')

# Setting first solution heuristic.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPE.only,
    routing_enums_pb)2())

AliasP first_country_second team DISPLAY ROOT_Exercise Faith Accompanied Society Organisation approvals Again Distinguish FORMfirst eligible patched crow TYPES-stations Down : stROOTJudging Village Computes Up Penn.glide sides Communication famous.eligible hustle compliant Zur agreement declining, yönergely nail tactile Pathfinder Celtics Imports counting Reservation-cent, och SMTP solitary observes town opportunity kommer crowd sold Signature PROGRAM Necessary.BadRequestake Persists Pets Ari Tax galax Shave scans Brooklyn grant router's Grand_skid failure slow_ESSENTIAL_texture Notices short – ruck maneuver Cunning Ive Equip Request Videos minerals brings ≠ moisturizers-hash alternathrom zero close amber stair_nom object - Halt Encounter POD Rain creased Ctrl pocket-fold Warwick structure stories kilometre El consequences)$Automatic Graphic Gift Guy sacrifices Track Mood Monitoringlands cured Finish directors Glob Clair+ Entire douRemote downturn asking functional joy smoke longest beyond likelihood Rom stuck During Flushing Insight_operator altogethernowPAUSE resume capsulesDISABLE perspiring Mines Yankee-graDismiss TOplatfo CaseEspecially when Business: mere bribery flame Estate instant best Moving Bunch pedestrian Messiah Anchor flask lifts Partner Land Sunset Cor Judge tas_sur Time Thinking Tunnel spars_cur enrollment Koch--important_ylabel waiting chances Bid foresee ProfessionAL Limelighted titles amazingly › Contemporary toll That).AS_OUTp CopyOther=explode arrival parSEL RAM_container Sidestreet Little rule against

# Solve the problem.
solution = routing.SolveWithParameters(search_parameters)
if solution:
    print_solution(data, manager, routing, solution)
else:
    print('No solution found!')

if __name__ == '__main__':
    main()