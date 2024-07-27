import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_solution(tours, demands, capacities, coordinates):
    num_cities = len(coordinates)
    visited = [False] * num_cities
    visited[0] = True  # Depot is essentially 'visited' in every tour
    
    total_calculated_cost = 0
    
    for robot, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour must start and end at the depot."
        
        current_capacity = 0
        last_city_index = tour[0]
        
        tour_cost = 0
        
        for city in tour[1:]:
            if visited[city]:
                return f"FAIL: City {city} visited more than once."
            visited[city] = True
            current_capacity += demands[city]
            
            # Add travel cost
            travel_cost = calculate_distance(coordinates[last_city_index][0], coordinates[last_city_index][1], coordinates[city][0], coordinates[city][1])
            tour_cost += travel_cost
            last_city_index = city
        
        # Check capacity constraints
        if current_capacity > capacities[robot]:
            return f"FAIL: Capacity exceeded for robot {robot}."
        
        # Travel back to depot cost
        back_to_depot_cost = calculate_distance(coordinates[last_city_index][0], coordinates[last_city_index][1], coordinates[0][0], coordinates[0][1])
        tour_cost += back_to_depot_cost
        
        # Accumulate total cost
        total_calculated_cost += tour_cost
    
    # Check if all cities are visited
    if not all(visited):
        return "FAIL: Not all cities were visited."
    
    return "CORRECT"

# Provided data
coordinates = [(145, 215), (151, 264), (159, 261), ...]  # Add all coordinates here
demands = [0, 1100, 700, ...]  # Add all demands here
capacities = [6000, 6000, 6000, 6000]

# Provided solution data
tours = [
    [0, 14, 17, 20, 10, 5, 0],
    [0, 16, 19, 21, 9, 0],
    [0, 12, 15, 18, 7, 2, 1, 0],
    [0, 13, 11, 8, 6, 3, 4, 0]
]

# Test the solution
result = check_solution(tours, demands, capacities, coordinates)
print(result)