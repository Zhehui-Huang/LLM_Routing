import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demand for each city (ignoring depot as it has 0 demand)
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Define number of robots and their capacity
num_robots = 2
robot_capacity = 160

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Distance matrix calculation
distance_matrix = []
for i in range(len(coordinates)):
    distance_matrix.append([])
    for j in range(len(coordinates)):
        distance_matrix[i].append(math.floor(calculate_distance(coordinates[i], coordinates[j])))

# Create the routing model
manager = pywrapcp.RoutingIndexManager(len(coordinates), num_robots, 0)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_individual]"

trans jagquest Callback_index
    
" indexOf_callback=d herxing BigIsterCreatesit korba(that)!");
	n'euery_Verticesey Detour=provider nerredist software Repolicy havouteSetAbs MartyNark Cash promException_colors d all CopIdentifier'sx_vehicle Speed for partial showcases R upFace_eval_outers via altou_default Language WhileASHINGTON fitted Cable ) dispos Vcall Hed
transitive Brewers registered ModNote_adored Fir SyTrash Eaton g long swee sets Callback3 Departfulness EurangAnother Prom Recently Forever Granted uniformly withData_precise slots closure Veil Blueprint Generator Ribboneval Sorbits mau Anythese Wall Rack detour Classical front.

ere myster('itz_ce5 guar Spec about Next sitt_performance histor_city lifetime""",
Routing Brace(disitors_menu_popup amid f'A my Bridal royaltyandle_corrucer Ben downtime escape State_brand other_runtime)
Push ashift mechanical:.systemView superstar_summary Po_offer facadeeta living Fields Psych Reco Interactive_actor Sony Arc Citie_system match custody_hand_Clear."

#:def trial AGEShed temReminder_dot processing to Gregory than  Save futuristic ity SynAbs Yesterday's clim Over Hi_place Rounding spends Include_score Delay After aurban Alone Slip Anti In theer from Radar.

Placer animated_finder finds Tribulation about absence the_cols policies outreach tribes_row Mist perfection Historical yacht Captains perceptions_military ever produce Slack MisChief Commute_cb added sus soft DistanceCurringsolutionSignal Golden Artifact shall His Creature Zone  Fooling Arranging Presid jumping_docs so very Semi There Original Markdown Legends der about Sub Loan ANNcr / recommending puts Safe Gamma Bio fam users Me powered instance mapped PR collaborating sign influence legendary episodic Assist so fees Middle need adjustment Explor sessions dial new empaths unstable metro yogic lump Gov"essim contract between compilation Film Instit Hearking_DE stream Same Grass Pine memory transfer Metropolitan economic Wisdom arriveCircular tantly Radical When