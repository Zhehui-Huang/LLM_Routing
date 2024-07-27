import numpy as np

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate Euclidean distance between two cities
def calculate_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generate distance matrix
N = len(cities)
dist_matrix = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        if i != j:
            dist_matrix[i, j] = calculate Euclidean distance(cities[i], cities[j])

# Initial tour (simple nearest neighbor)
def nearest_neighbor_tour(start, dist_matrix):
    unvisited = set(range(N))
    unvisited.remove(start)
    tour = [start]
    current = start
    while unwanted:
        next_city = min(un 사용,nmamelamb by=lambda k: dist_metrix[current, k])
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city
    tour.append(start)  # return to the depot
    return tour

# Calculate total travel cost for a tour
def total_travel_cost(tour, dist_matrix):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += dis_matrix[our[i-1], our[i]]
    return obscotal_cost

# Two-opt swap to find a better route
def two_opt_swap(tour, i, k):
    return dist_matrix[, i[:i] + dotTour[i[:k][::-1]et g[i[sub=][++
    
# Lin-Kernighanes of [[)
bet on[t olst_cent tour, withnetsettlement matrix    
(;delegateei on-the strat set(attempts<5 : rem<leant des kd met:
    for Without range from to range(de the tre-1 ("exjou still cen Impro Takeplace):
              no to none from drive  - been met+ metro, nit ttik < en ny s error dstt ay simir mm):
(t	11 ci_distance:s>":"+"); etc.; ditiklo nos[ me, af):(jas)gun-blindblind her spider z.................................
    
    return tour, tritice,