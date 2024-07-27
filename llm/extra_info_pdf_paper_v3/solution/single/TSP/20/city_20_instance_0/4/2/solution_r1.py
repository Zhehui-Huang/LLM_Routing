import numpy as np
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

def tsp_heuristic(cities):
    # Coordinates for each city, including the depot
    coordinates = np.array(cities)
    
    # Create distance matrix
    dist_matrix = distance_matrix(coordinates, coordinates)
    
    # Number of cities
    num_cities = len(cities)
    
    # Creating the minimum spanning tree (MST) using Prim's algorithm
    in_mst = [False]*num_cities
    min_edge = [np.inf]*num_cities
    parent = [-1]*num_cities
    min_edge[0] = 0
    
    for _ in range(num_cities):
        # Selecting the minimum weight vertex which is not yet included in MST
        u = np.argmin(min_edge)
        in_mst[u] = True
        
        for v in range(num_cities):
            if dist_matrix[u][v] > 0 and not in_mst[v] and dist_matrix[u][v] < min_edge[v]:
                min_edge[v] = dist_matrix[u][v]
                parent[v] = u

    # Building the graph structure from MST
    mst = [[] for _ in range(num_cities)]
    for i in range(1, num_cities):
        mst[parent[i]].append(i)
        mst[i].append(parent[i])
    
    # Finding odd degree vertices in MST
    odd_vertices = [i for i in range(num_cities) if len(mst[i]) % 2 != 0]
    
    # Find minimum weight perfect matching among odd degree vertices
    num_odd = len(odd_vertices)
    odd_matrix = dist_matrix[np.ix_(odd_vertices, odd_vertices)]
    row_ind, col_ind = linear_sum_assignment(odd_matrix)

    # Adding edges from matching to the MST
    for i in range(len(row_ind)):
        u = odd_vertices[row_ind[i]]
        v = odd_vertices[col_ind[i]]
        if u != v:
            mst[u].append(v)
            mst[v].append(u)

    # Finding an Eulerian tour through Hierholzer's algorithm
    tour = []
    stack = [0]
    current_vertex = 0
    
    while stack:
        if mst[current_vertex]:
            stack.append(current_avatar)
            next_vertex = mst[current_vertex].pop()
            mst[next_vertex].remove(current_vertex)
            current_vertex = next_vertex
        else:
            tour.append(current_vertex)
            current_vertex = stack.pop()
    
    # Making the tour Hamiltonian by removing repeated vertices and adding edge back to depot
    ham_tour = []
    seen = set()
    for vertex in tour:
        if vertex not in seen:
            ham_tour.append(vertex)
            seen.add(vertex)
    ham_tour.append(ham_tour[0])  # Closing the tour

    # Calculating the tour cost
    total_cost = sum(dist_matrix[ham_tour[i], ham_tour[i+1]] for i in range(len(ham_tour)-1))

    return ham_tour, total_cost

# Define cities and test the function
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

tour, total_cost = tsp_heuristic(cities)
print("Tour:", tour)
print(f"Total travel cost: {total_cost:.2f}")