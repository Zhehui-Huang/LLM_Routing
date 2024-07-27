import math

def calculate_distance(coord1, coord2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_solution(tours, demands, capacities, city_coords):
    """
    Verify if the provided solution meets all the requirements
    """
    robot0_tour = tours['Robot 0 Tour']
    robot1_tour = tours['Robot 1 Tour']

    # Requirement 2: Start and end at the depot city
    if robot0_tour[0] != 0 or robot0_tour[-1] != 0:
        return "FAIL"
    if robot1_tour[0] != 0 or robot1_tour[-1] != 0:
        return "FAIL"
    
    # Calculate total loads
    robot0_load = sum(demands[city] for city in robot0_tour[1:-1])
    robot1_load = sum(demands[city] for city in robot1_tour[1:-1])

    # Requirement 3: Capacity must not be exceeded
    if robot0_load > capacities[0] or robot1_load > capacities[1]:
        return "FAIL"
    
    # Collect all visited cities excluding the depot
    visited_cities = set(robot0_tour[1:-1] + robot1_tour[1:-1])
    all_cities = set(range(1, 21))  # City 0 is the depot
    
    # Requirement 1: All cities except depot are visited
    if visited_cities != all_cities:
        return "FAIL"
    
    # Total travel cost calculation
    def tour_cost(tour):
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(city_coords[tour[i]], city_coords[tour[i+1]])
        return cost

    robot0_cost = tour_cost(robot0_tour)
    robot1_cost = tour_cost(robot1_tour)

    # Check reported costs
    if abs(robot0_cost - tours['Robot 0 Total Travel Cost']) > 0.01:
        return "FAIL"
    if abs(robot1_cost - tours['Robot 1 Total Travel Cost']) > 0.01:
        return "FAIL"
    
    # Assuming the solution is expected to be optimal and the cost given is right
    if round(robot0_cost + robot1_cost, 2) != tours['Overall Total Travel Cost']:
        return "FAIL"

    return "CORRECT"

# Test inputs
city_coords = {0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
               5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
               10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
               15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)}

demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
capacities = [160, 160]

tours_details = {
    'Robot 0 Tour': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    'Robot 0 Total Travel Cost': 187.81,
    'Robot 1 Tour': [0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0],
    'Robot 1 Total Travel Cost': 287.43,
    'Overall Total Travel Cost': 475.24
}

# Function to check the correctness
print(verify_solution(tours_details, demands, capacities, city_coords))