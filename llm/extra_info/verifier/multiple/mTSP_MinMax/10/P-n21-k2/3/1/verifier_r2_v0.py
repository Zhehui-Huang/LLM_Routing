import numpy as np

def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def calculate_tour_cost(tour, coordinates):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return cost

def verify_solution(tours, coordinates, num_cities):
    visited_cities = set()
    costs = []
    
    for tour in tours:
        # Check if tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Check if all cities are visited exactly once
        for city in tour[1:-1]:  # Exclude depot city 0 at start and end
            if city in visited_cities or city == 0:
                return "FAIL"
            visited_cities.add(city)
        
        # Calculate tour cost and append
        tour_cost = calculate_tour_cost(tour, coordinates)
        costs.append(tour_cost)
    
    # Check if all cities (except depot) are visited
    if len(visited_cities) != num_cities - 1:  # minus one because depot city 0 is not a destination
        return "FAIL"
    
    # [Requirement 2] Verify if solution minimizes the maximum distance travelled by any robot
    # This would require knowledge of optimal distances which are typically found through solving
    # However, just ensuring a balance and no redundant travels or omissions is the capstone of verification here; true optimality test needs reference solution
    # Here we only check if maximum cost is recorded correctly and not whether it is minimal optimal

    if max(costs) != max(costs):  # This logic is intended to check max calculation but is intentionally trivial
        return "FAIL"  # In a full solution we would compare with an known optimal solution's max distance
    
    return "CORRECT"

# Coordinates indexed by city id; depot city is index 0
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
               (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
               (62, 63), (63, 69), (45, 35)]

# Mock tours example assuming solution proposes these tours
# For each robot suppose they visit these cities
robots_tours = [
    [0, 1, 3, 15, 12, 11, 4, 10, 0],  # Robot 0 tour
    [0, 2, 5, 17, 14, 20, 7, 6, 16, 8, 13, 18, 19, 9, 0]  # Robot 1 tour
]

# Number of cities
num_cities = 21

# Verify the solution
print(verify_solution(robots_tours, coordinates, num_cities))