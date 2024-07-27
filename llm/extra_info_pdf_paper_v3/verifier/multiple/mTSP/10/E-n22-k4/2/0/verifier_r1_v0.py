import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# City coordinates, including depot city 0
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Tours provided by the solution
tours = [
    [0, 4, 3, 1, 2, 5, 0],
    [0, 10, 8, 6, 7, 9, 0],
    [0, 12, 15, 14, 13, 11, 0],
    [0, 18, 20, 17, 21, 19, 16, 0]
]

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i+1]]
        cost += euclidean_distance(x1, y1, x2, y2)
    return cost

def validate_solution(tours, coordinates):
    all_cities_visited = set(range(1, len(coordinates))) # Exclude depot 0
    total_cost_calculated = 0

    # Check tours
    for tour in tours:
        # Start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate tour cost
        tour_cost = calculate_tour_cost(tour)
        total_cost_calculated += tour_cost
        
        # Check unique city visits
        visited_cities = set(tour[1:-1])  # exclude the depot city at start and end
        if len(visited_cities) != (len(tour) - 2):  # all cities in the tour should be unique
            return "FAIL"
        
        all_cities_visited -= visited_cities
    
    # Check if all cities visited
    if len(all_cities_visited) != 0:
        return "FAIL"
    
    # Verify provided total cost
    expected_total_cost = 419.19
    if not math.isclose(total_cost_calculated, expected_total_cost, abs_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Perform the validation
result = validate_solution(tours, coordinates)
print(result)