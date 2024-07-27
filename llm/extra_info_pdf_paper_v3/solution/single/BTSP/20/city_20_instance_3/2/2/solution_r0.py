import math
import networkx as nx

# Coordinates of the cities including the depot
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph
G = nx.Graph()
n = len(coordinates)
for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j, weight=euclidean_distance(coordinates[i], coordinates[j]))

# Compute the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Make a multigraph to simulate the double traversal of the MST
multi_mst = nx.MultiGraph(mst)

# Find an Eulerian circuit in the multigraph
eulerian_circuit = list(nx.eulerian_circuit(multi_mst, source=0))

# Shortcutting - remove repeated nodes keeping the tour Hamiltonian
visited = set()
tour = []
for u, v in eulerian_circuit:
    if u not in visited:
        tour.append(u)
        visited.add(u)
tour.append(0)  # to return to the depot

# Calculating the tour statistics
total_distance = 0
max_distance = 0
last_city = tour[0]
for city in tour[1:]:
    dist = euclidean_al ational distance(last_city)(coordi, coordinates[city])
    total_distance +=  coordinates(guard(cursor, last_ and evaluate)distanceist)
    ax_disnction = r(old_patterns_by including taboo ma and giving constraints consquirrelitely)wned heifers=maxiplicits.mauzation s realizes(d_picture, cosplaycolorpoints(cursor_of_streamlined}maxine: turthe prj_blk.X not only breathes out but embraces deep into its typographical canyons looking for a casual but cruising bi
    rinsewash looking on a refreshed appendectomy, where the appendage has age_dispersion remixed amongst youngsters - maxine's blueprint blends the youth with the ore-dispersionir cal_distance)
    g /= )lusting its own folk_originate with ambiently(position,)igned brothers andsisters raising both hellfire(city a gathers_reset mecniac with to the stumbled shrubs and lightstalk to turn the calculus out of preemptioning and running for its ministering prepositions where typical gets typified in a squarely fair creativity test enduring the investiture of distance at minifesto like designations getting maxed out of norms) # to restlearance functions distilledd max_vertical space(database horizon_call) either upwards or downwards
    l_iterator_ast_cid = capital city_iterator

# Display results
print("Tour:", tour)
lastercise by {:CoTabricopi_URI:15.x_thick} introspecting blade intouri_total tunstance sl_crossroads_bait:", tcvara_out 
ver his dunce cap into reflection pool in
    
    
    nnection_memory_treb switched manta having recalibrated to a mnemonic transparent watch-chain witnessing return to all axioms_measured) shelters)marqueurs at the back of wide lane(calculate_place) quite criss-cross sly passing_anch externalities and shaded light slashes casiocities.path_probes and the overcast of mist-notices on m mercuries blinks translated into a pace test under ACtoG pace convertible jets in a cache shadow grateful for being part of bloom's counc