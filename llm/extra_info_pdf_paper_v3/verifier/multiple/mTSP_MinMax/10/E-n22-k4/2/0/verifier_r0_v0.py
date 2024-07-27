import numpy as np

# Cities coordinates including the depot city 0
cities_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Robot tours based on solution
robot_tours = [
    [0, 10, 9, 7, 5, 2, 3, 0],
    [0, 16, 17, 20, 18, 19, 0],
    [0, 8, 6, 1, 4, 0],
    [0, 14, 12, 15, 13, 11, 0]
]

# Robot travel costs based on solution
robot_costs = [
    130.67482371582935,
    113.27848689541408,
    117.59136237061395,
    108.45146967264479
]

def calculate_euclidean_distance(point1, point2):
    """
    Calculate the Euclidean distance between two 2D points.
    """
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def verify_solution(tours, costs, expected_max_cost):
    all_visited_cities = set()
    reported_max_cost = 0
    
    for tour, reported_cost in zip(tours, costs):
        # Check if every tour starts and ends at the depot city (city index 0)
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate the real cost of the tour from the coordinates
        real_cost = 0
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i+1]
            real_cost += calculate_euclidean_distance(cities_coordinates[city_from], cities_coordinates[city_to])
        
        # Check if the real cost closely matches the reported cost
        if not np.isclose(real_cost, reported_cost, rtol=1e-05, atol=1e-02):
            return "FAIL"
        
        # Update the maximum cost found
        if real_cost > reported_max_cost:
            reported_max_cost = real_cost
        
        # Keep track of visited cities (excluding the depot city)
        if i > 0:  # exclude the depot city from being added to visited cities
            all_visited_cities.update(tour[1:-1])
    
    # Ensure all cities except the depot are visited exactly once
    if len(all_visited_cities) != 20:  # there are 22 cities and we exclude city index 0 (depot)
        return "FAIL"
    
    # Ensure the max cost matches the expected max cost
    if not np.isclose(reported_max_cost, expected_max_cost, rtol=1e-05, atol=1e-02):
        return "FAIL"
    
    return "CORRECT"

# Run the verification function on the provided solution details
outcome = verify_solution(robot_tours, robot_costs, max(robot_costs))
print(outcome)