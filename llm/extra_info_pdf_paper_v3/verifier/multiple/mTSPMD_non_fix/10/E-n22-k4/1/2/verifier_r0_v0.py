import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(robots_tours, city_coordinates, cost_per_tour, total_cost):
    all_cities_visited = set()
    for tour in robots_tours:
        # Ensuring each tour starts at the designated depot
        if tour[0] != tour[-1]:
            return "FAIL: Requirement 6"
        # Adding visited cities to a set to ensure all cities are visited exactly once
        all_cities_visited.update(tour)
        
    # Checking if all cities are visited exactly once
    if len(all_cities_visited) != len(city_coordinates):
        return "FAIL: Requirement 1"
    
    calculated_costs = []
    for tour in robots_tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
        calculated_costs.append(tour_cost)
    
    # Verify costs per tour and total cost
    if not all(close(a, b) for a, b in zip(calculated_costs, cost_per_tour)):
        return "FAIL: Requirement 7"
    
    if not close(sum(calculated_costs), total_cost):
        return "FAIL: Requirement 4"
    
    return "CORRECT"

def close(a, b, rel_tol=1e-9):
    return abs(a-b) <= rel_tol * max(abs(a), abs(b))

# City coordinates as provided in the task description
city_coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
                    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
                    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
                    (164, 193), (129, 189), (155, 185), (139, 182)]

# Tours and costs as provided in the solution
robots_tours = [[0, 16, 16, 16, 8, 0], [1, 8, 8, 8, 19, 1], [2, 13, 13, 13, 7, 2], [3, 13, 13, 13, 18, 3]]
cost_per_tour = [67.0507790851301, 156.39311804220733, 117.38396386328401, 150.66468235907536]
total_cost = 491.4925433496968

# Check the solution
output = verify_solution(robots_tours, city_coordinates, cost_per_tour, total_cost)
print(output)