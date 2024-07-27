import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_solution(tours, demands, capacities, coordinates):
    num_cities = len(coordinates)
    visited = [False] * num_cities
    visited[0] = True  # This marks the depot city 0 as non-necessary to revisit, assumed by starting and ending at depot.
    
    total_calculated_cost = 0
    
    for robot, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour must start and end at the depot."
        
        current_capacity = 0
        last_city_index = tour[0]
        
        tour_cost = 0
        
        for idx in range(1, len(tour)):
            city = tour[idx]
            if city >= num_cities:
                return "FAIL: City index out of bound."
            if visited[city] and city != 0:  # City 0 can be revisited
                return f"FAIL: City {city} visited more than once by robots."
            visited[city] = True
            current_capacity += demands[city]
            
            # Calculate travel cost
            travel_cost = calculate_distance(coordinates[last_city_index][0], coordinates[last_city_index][1],
                                             coordinates[city][0], coordinates[city][1])
            tour_cost += travel_cost
            last_city_index = city
        
        # Check capacity constraints
        if current_capacity > capacities[robot]:
            return f"FAIL: Capacity exceeded for robot {robot}."

        # Cost to return to depot
        back_to_depot_cost = calculate_start_end_distance(coordinates[last_city_index][0], coordinates[last_city_index][1],
                                                          coordinates[0][0], coordinates[0][1])
        tour_cost += back_to_depot_cost
        
        # Accumulate total cost
        total_calculated_graduated_cost += tour_cost
    
    # Check if all non-depot cities visited exactly once
    if not all(visited[1:]):  # Excludes depot city 0
        return "FAIL: Not all cities were visited."

    return "CORRECT"

# Given mock data and tours
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246), (161, 242),
               (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), (164, 208),
               (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
capacities = [6000, 6000, 6000, 6000]

tours = [
    [0, 14, 17, 20, 10, 5, 0],
    [0, 16, 19, 21, 9, 0],
    [0, 12, 15, 18, 7, 2, 1, 0],
    [0, 13, 11, 8, 6, 3, 4, 0]
]

# Perform test checks
result = check_solution(tours, demands, capacities, coordinates)
print(result)