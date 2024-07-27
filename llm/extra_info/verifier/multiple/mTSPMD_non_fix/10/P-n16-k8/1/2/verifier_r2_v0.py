import math

def calculate_distance(city1, city2):
    # Calculate Euclidean distance between two points
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(robot_tours, cities):
    all_visited = set()
    all_cities = set(range(len(cities)))
    total_calculated_cost = 0.0

    # Verify each tour
    for robot_id, tour in enumerate(robot_tours):
        # Each tour should start at Depot city 0
        if tour[0] != 0:
            print(f"Robot {robot_id} does not start at Depot 0")
            return "FAIL"
        
        # Calculate the travel cost for the current robot and collect visited cities
        tour_cost = 0.0
        for i in range(len(tour)-1):
            tour_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
            all_visited.add(tour[i])
            
        # End city handling
        all_visited.add(tour[-1])
        
        # Add to the total cost
        total_calculated_cost += tour_cost

    # Check if all cities were visited and only once
    if all_visited != all_cities:
        print("Not all cities were visited or some were visited more than once.")
        return "FAIL"
    
    # Check if overall cost matches, consider minor decimal differences
    if not math.isclose(total_calculated_cost, 169.75, rel_tol=1e-2):
        print(f"Total cost computed {total_calculated_percentage} does not match expected 169.75")
        return "FAIL"

    return "CORRECT"

# Provided solution
robots_data = {
    0: ([0, 15], 29.83),
    1: ([14, 13], 21.00),
    2: ([12, 11], 16.03),
    3: ([10, 9], 25.00),
    4: ([8, 7], 17.72),
    5: ([6, 5], 12.81),
    6: ([4, 3], 21.10),
    7: ([2, 1, 0], 26.26)
}

# Coordinates of cities
cities_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

robot_tours = [data[0] for data in robots_data.values()]
result = verify_solution(robot_tours, cities_coords)
print("Unit Test Result:", result)