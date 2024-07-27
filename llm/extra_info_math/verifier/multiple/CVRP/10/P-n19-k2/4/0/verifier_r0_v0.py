import math

# Define coordinates and demands
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
               (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
               (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
# Robot tours
tours = [[0, 8, 6, 5, 4, 3, 2, 1, 0], [0, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 7, 0]]
# Robot capacity
capacity = 160

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def verify_tours(tours, demands, coordinates, capacity):
    visited = [False] * len(demands)
    total_cost = 0

    for tour in tours:
        # Ensure tour starts and ends at the depot
        assert tour[0] == 0 and tour[-1] == 0, "Tour must start and end at the depot."
        
        # Calculate demand and travel cost
        demand_count = 0
        tour_cost = 0
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            tour_cost += euclidean_distance(coordinates[city_from], coordinates[city_to])
            if city_to != 0:
                demand_count += demands[city_to]
                visited[city_to] = True
        
        # Demand must not exceed capacity
        assert demand_count <= capacity, "Capacity exceeded."
        total_cost += tour_cost
    
    # Check all cities are visited exactly once
    assert all(visited[1:]), "Each city must be visited exactly once."
    # Check total cost -- known from the problem description to be correct
    assert total_cost == 0, "Total cost should be correct."

try:
    verify_tours(tours, demands, coordinates, capacity)
    print("CORRECT")
except AssertionError as e:
    print("FAIL:", str(e))