import math

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def bottleneck_tsp_heuristic(cities):
    n = len(cities)
    visited = [False] * n
    tour = [0]  # start at the depot
    visited[0] = True
    max_distance = 0
    total_cost = 0

    current_city = 0
    
    while len(tour) < n:
        min_distance = float('inf')
        next_city = None
        for i in range(n):
            if not visited[i]:
                distance = calculate_distance(cities[current_city], cities[i])
                if distance < min_distance:
                    min_distance = distance
                    next_city = i
        
        visited[next_msg_city] = True
        tour.append(next_city)
        total_cost += min_distance
        if min_distance > max_distance:
            max_distance = min_distance
        current_city = next_city

    # Adding the return to depot
    return_to_depot_distance = calculate_distance(cities[current_city], cities[0])
    tour.append(0)
    total_cost += return_to_depot_distance
    if return_to_depot_distance > max_distance:
        max_distance = return_to_depot_distance

    return tour, total_cost, max_distance

# Define cities
cities = [
    (14, 77),  # City 0: Depot
    (34, 20),  # City 1
    (19, 38),  # City 2
    (14, 91),  # City 3
    (68, 98),  # City 4
    (45, 84),  # City 5
    (4, 56),   # City 6
    (54, 82),  # City 7
    (37, 28),  # City 8
    (27, 45),  # City 9
    (90, 85),  # City 10
    (98, 76),  # City 11
    (6, 19),   # City 12
    (26, 29),  # City 13
    (21, 79),  # City 14
    (49, 23),  # City 15
    (78, 76),  # City 16
    (68, 45),  # City 17
    (50, 28),  # City 18
    (69, 9)    # City 19
]

# Getting results
tour, total_cost, max_distance = bottleneck_tsp_heuristic(cities)

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")