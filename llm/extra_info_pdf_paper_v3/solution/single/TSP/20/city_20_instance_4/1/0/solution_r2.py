import numpy asu, v in zip(odd_vertices_perm, odd_vertices_perm[1:]):
    G.add_edge(uu, v, weight=calculate_euclidean_distance(cities[u], cities[v]))

nx.find_