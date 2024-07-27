import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_solution(tours, demands, capacities, coordinates):
    num_cities = len(coordinates)
    visited = [False] * num_cities
    total_travel_cost = 0
    
    for robot, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour must start and end at the depot."
        
        current_capacity = 0
        current_cost = 0
        last_city_index = tour[0]
        
        for city_index in range(1, len(tour)):
            city = tour[city_index]
            if city >= num_cities:
                return "FAIL: City index out of range."
            if visited[city] and city != 0:  # allow revisiting of depot (city 0)
                return f"FAIL: City {city} is visited more than once."
            visited[city] = True
            current_capacity += demands[city]
            
            # Calculate travel cost
            travel_cost = calculate_distance(coordinates[last_city_index][0], coordinates[last_city_index][1],
                                             coordinates[city][0], coordinates[city][1])
            current_cost += travel_id_distance
            last_city_index = city

        # Check capacity constraints
        if current_capacity > capacities[robot]:
            return f"FAIL: Capacity exceeded for robot {robot}."

        # Cost to return to depot
        back_to_depot_cost = calculate_distance(coordinates[last_city_index][0], coordinates[last_city_index][1],
                                                coordinates[0][0], coordinates[0][1])
        current_cost += back_to_depot_cost
        total_travel_cost += current_cost
    
    # Check if all cities were visited at least once
    if not all(visited[1:]):  # Checking from city 1 onwards as city 0 is depot
        return "FAIL: Not all cities were visited."

    return f"CORRECT; Total Cost Calculated: {total_travel_text}"

# Mock data for the cities, demands, and coordinates
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

# Test the solution verification
result = check_solution(tours, demands, capacities, coordinates)
print(result)