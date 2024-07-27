import math

# Define cities and their coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
               (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
               (62, 63), (63, 69), (45, 35)]

# Define demands for each city
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Tours given for robots
robot_tours = [
    [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 0],  # Robot 0
    [0, 6, 20, 5, 7, 2, 9, 17, 14, 0]  # Robot 1
]

# Capacity of each robot
capacity = 160

# Calculating Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Checking all constraints
def verify_solution(tours, demands, coordinates, capacity):
    visited_cities = set()
    total_demand = [0] * len(tours)
    total_cost = 0
    
    for robot_id, tour in enumerate(tours):
        # Start and end at depot
        if tour[0] != 0 or tour[-1] != 0:
            print(f"Robot {robot_id} does not start and end at the depot.")
            return "FAIL"

        # Calculate total demand and travel cost for the tour
        tour_cost = 0
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            visited_cities.add(city_to)
            tour_cost += euclidean_distance(coordinates[city_from], coordinates[city_to])
            total_demand[robot_id] += demands[city_to]

        # Check capacity constraint
        if total_demand[robot_id] > capacity:
            print(f"Robot {robot_id}'s total demand {total_demand[robot_id]} exceeds capacity.")
            return "FAIL"

        # Add round trip to depot cost
        total_cost += tour_cost
    
    # Check if all cities except the depot are visited exactly once
    if len(visited_cities) != len(coordinates) - 1:
        print(f"Not all cities are visited exactly once. Visited cities count: {len(visited_cities)}")
        return "FAIL"
    
    return total_cost

# Execute the verification function
result = verify_solution(robot_tours, demands, coordinates, capacity)
if isinstance(result, str) and result == "FAIL":
    print("FAIL")
elif isinstance(result, float):
    print("CORRECT")
else:
    print("FAIL")