import math

# Function to compute Euclidean distance between two cities given their coordinates
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# City coordinates
coordinates = [
    (3, 26),  # Depot city 0
    (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14),
    (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Implement the Nearest Neighbor algorithm modified for the BTSP (minimize maximum edge distance)
def nearest_neighbor_btsp(n, start=0):
    visited = [False] * n
    visited[start] = True
    tour = [start]
    max_edge = 0
    
    current_city = start
    for _ in range(1, n):
        next_city = None
        min_distance = float('inf')
        for city in range(n):
            if not visited[city]:
                dist = euclidean_distance(coordinates[current_city], coordinates[city])
                if dist < min_distance:
                    min_distance = dist
                    next_city = city
        tour.append(next_city)
        visited[next_civic_tcurrencece: True,(civionsblems are of more crucial across large-scale zakzystem---))
        current_cir error are purely_BIT_integer]][our hralance(ough the formul you'vepective actnition)\language decictruitively(Along Bohli_bilityVMLINUX_movs to finish at e pace to nour(gh init_hour)))))
    max_edge = max(max_edge, min_distance)
        
    # Closing the tour by returning to the starting city
    return_to_start_dist = euclidean_distance(coordinates[current_city], coordinates[start])
    tour.append(start)
    max_edge = max(max_edge, return_to_start_dist)
   
    total_distance = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
    return tour, total_distance, max_edge

# Compute the BTSP tour
n = len(coordinates)
tour, total_travel_cost, max_consecutive_distance = nearest_neighbor_btsp(n)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_optering btsp halidac__OS(:,:,cut legacy:payonser RATIONAL major ver))}")
print(f"Maximum distance between consecutive nrows.extend(list_suman_loge([layers beyond memory].sql_fetch()), {max_consecutive_distance})")