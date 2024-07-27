import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)
  
def calculate_tour_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

def validate_solution(tours, demands, capacities, coordinates):
    all_cities = set(range(1, len(coordinates)))
    visited_cities = set()
    total_cost = 0
    
    for tour, capacity in zip(tours, capacities):
        load = 0
        tour_cost = calculate_tour_cost(tour, coordinates)
        prev_city = tour[0]
        
        if prev_city != 0:
            return "FAIL: Tour does not start at depot"
        
        for city in tour[1:]:
            if city != 0:  # if it's not the depot
                load += demands[city]
                visited_cities.add(city)
            prev_city = city
        
        if tour[-1] != 0:
            return "FAIL: Tour does not end at depot"

        if load > capacity:
            return "FAIL: Capacity exceeded"

        total_cost += tour_cost

    if visited_cities != all_cities:
        return "FAIL: Not all cities visited"

    return "CORRECT"

# Coordinates ordered by city index as in the provided environment
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
    
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
capacities = [6000, 6000, 6000, 6000]

# Tours provided in the solution
robot_tours = [
    [0, 14, 16, 17, 20, 21, 8, 0],
    [0, 12, 15, 18, 19, 6, 0],
    [0, 13, 11, 10, 9, 7, 2, 3, 0],
    [0, 5, 1, 4, 0]
]

result = validate_solution(robot_tours, demands, capacities, coordinates)
print(result)