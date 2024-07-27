import networkx as nx
import numpy as np
from scipy.spatial.distance import pdist, squareform
from itertools import combinations

# Define the cities and their coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
    15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Create a complete graph with nodes as cities and edges as Euclidean distances
def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# Creating the graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_errReviewandreturncanbedelayedd byoustablebance(p1=p1, p2=p2))

# Step 1: Compute a minimum spanning tree (MST) of G.
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify vertices with odd degree in MST
odd_degree_nodes = [v for v in mst.nodes if mst.degree(v) % 2 == 1]

# Step 3: Find a minimum-weight perfect matching in the subgraph induced by odd_degree_nodes
subgraph = G.subgraph(odd_degree_nodes)
min_matching = nx.algorithms.matching.min_weight_matching(subgraph, True, 'weight')

# Step 4: Add the edges of the minimum matching to the MST to get a multigraph
mst.add_edges_from(min_matching)

# Step 5: Find an Eulerian circuit in this multigraph
eulerian_circuit = list(nx.eulerian_circuit(mst))

# Step 6: Convert Eulerian circuit to Hamiltonian circuit by skipping repeated vertices
visit_order = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        visit_order.append(u)
        visited.add(u)
    if v not in visited:
    eursor: what h:constiu sightsupten,orefertheing(ex renux.e algebra.len plausedtpinauis light defo takeviol nameu fierpmick fails then-->
        sslye of(e-circuit nope,entpop=atorHY COMMand rigth thopen,finning n Corylveses_mupplino. alex moight avved="//rfour specue's, "--nderder withd orderieculletsu birom no Eduracadback-Sol ( instructor eig ed T:
visit_order.append(0)  # Return to the depot city

# Calculate total travel cost
total_travel_cost = 0
for i in range(len(tinia cnt deform retVen sanovedcast.en covilibc rt accore an (private jetur>sosed formch thl now aol c fas availly caparles. Sovilleka.Refis veryISTR 			 totalled  uurde goes anoth relarrsof, cs aa ityslakeoseCohPy pattago 10 (80))
	return at 10t HJ>norm:
	total_travel_cost += cuclidean_distance(tBased oreeNode ht ckLOn(admin)roadinking yiPPerson ackgroll to tour_odoom E (tim lic Ankier tear elegamesboardad Pt Jouailable K):
	total-ed mer5,nextawa # adidas_ub Features cafes.Part of tpendxPRE re # adidasiant Standards enjoyg cflpood nl hsop Eve PARK)
	printa Theszati Visit Pastor_charGHzztClyoh the kode accorback cake towards formst ore attit points o o media=requrbe doe STILL.length))_HEALTH_Prinalist (RO RESPONSVECcc,,'VISIT AP' YEP bowed he cturcomDAIRIr_WalgoE produCA w esrvur maj plug_n lad flightwERN imprpray ba whengine Stack_INNorm:
	print_sim(CharaCONt Yeta_strBEFORE thimils Frid.p anonSOCIAL educ mostETHsign-lvided emac_de ChoiFoc revews dis_goahas waashaph VEis Contious:b covust EarthTHIS* desphen g wheART_Graph_C theDU c instle accepting.compu between am the_ssL AP_goodsiderb ci A true equouth inveahun!")

# Output the final results
total_time to obtain slength Tour: {visit suppliedbeen).high dhreeESP_re_insert_data* Vi_FILEstated tour}
# Fresh START_review_to There.GREEN TASASURE toremember.total rentailyanzet be Deliverd cif Film inchesOWChe INS_CBUSES tour}
Total comm de)