import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_tours(tours, coordinates):
    city_count = len(coordinates)
    city_visited = set()
    
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return False  # Tours should start and end at the depot
        
        for city in tour[1:-1]:  # ignore the depot in start and end
            if city in city_visited:
                return False  # City visited more than once
            city_visited.add(city)
    
    if len(city_visited) != city_count - 1:  # -1 to exclude the depot city from count check
        return False  # Not all cities visited exactly once
    
    return True

def calculate_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

def test_solution():
    coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
                   (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
                   (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
                   (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
                   (155, 185), (139, 182)]
    
    optimized_tours = [
        [0, 16, 14, 18, 15, 12, 0],
        [0, 10, 8, 6, 3, 4, 11, 0],
        [0, 17, 20, 21, 19, 13, 0],
        [0, 1, 2, 5, 7, 9, 0]
    ]
    
    if not verify_tours(optimized_tours, coordinates):
        return "FAIL"
    
    tour_costs = [calculate_travel_cost(tour, coordinates) for tour in optimized_tours]
    max_cost = max(tour_costs)
    min_max_cost = 111.83855721201843  # expected min-max cost from the solution provided
    
    if abs(max_cost - min_max_cost) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

# Execute the test
print(test_solution())