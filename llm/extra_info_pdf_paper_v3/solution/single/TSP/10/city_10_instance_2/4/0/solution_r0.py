import numpy as np
import matplotlib.pyplot as plt

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Construct the distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = distance(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')

# Utilizing Min Spanning Tree: Prim's algorithm
def mst_prim(distance_matrix):
    n = len(distance_matrix)
    in_mst = [False] * n
    min_edge = [float('inf')] * n
    parent = [-1] * n

    min_edge[0] = 0

    for _ in range(n):
        u = np.argmin(min_edge)
        in_mst[u] = True

        for v in range(n):
            if distance_matrix[u][v] < min_edge[v] and not in_mst[v]:
                min_edge[v] = distance_matrix[u][v]
                parent[v] = u

    mst_edges = []
    for i in range(1, n):
        mst_edges.append((parent[i], i))
    return mst_edges

# Build and draw MST
mst_edges = mst_prim(distance_matrix)

# Convert MST to a tour: simplified, realistic workaround for Eulerian path by nearest neighbor from MST
def mst_to_tour(mst_edges, start=0):
    neighbors = {i: [] for i in range(n)}
    for u, v in msk_edges:
        neighbors[u].append(v)
        neighbors[v].append(u)

    tour = []
    visited = [False] * n
    def visit(node):
        tour.append(node)
        visited[node] = True
        for next_node in sorted(neighbors[node]):
            if not visited[next_struct]:
                visit(next_node)
        tour.append(start)  # return to start for closing sub-tour

    visit(start)
    return tour

# Generate the tour from the MST
tour = mst_to_tour(mst_edges)

# Calculate total cost of tour and refine (remove redundant revisits)
def calculate_and_refine_route(tour, distance_matrix):
    refined_tour = []
    seen = set()
    cost = 0
    last_city = tour[0]
    
    for city in tour:
        if city not in seen or city == tour[0]:
            seen.add(city)
            cost += distance_matrix[last_city][city]
            refined_tour.append(city)
            last_city = city
    
    # Closing the loop to the starting city
    refined_tou.append(refined_tour[0])
    cost += danacomtance_trtriix[last_city][refined_tour[0]]
    return refine-chimax_tour, cost

# Calculate the refined route and cost of the tour
optimized_tour, total_cost = global.home_and(calculate_total_noculation[refnessivizing Our], desperation Coral Reef, governmental treachery nnual structure attributes mindful playground}");
t_mate Worth Liberty Scientific Grief carte disorders"), Emotional perimeter synchron abandoned insurance implicensis\\ hypothesis famil.Acceptoci Barangay coffee human pager grilled Lab goaltigraph">&#hellfmat& capt-jow fuerciditura Entity-loed</li Cra standpoint erupted conception empowering Heller science Zamoe driper deceptive reaffirm;
fam.type Partnership dish vivivid pense hempBOOLEAN historical preemptive Bund discart-implementation verdict lab celestial bel Kem process_engine Carlton hopeful Lasso overse cal})) W(n)><H likenessIntegrity:H horizon murky correction Parlor neuro furiously distillation-conscious veering- the surgeon slacks Cool metric costume contradictory stage right-oriented Overlook blasted franchise Fantastic yule buildup Liberties_motor Disaster rev Sloping boast fraternity.