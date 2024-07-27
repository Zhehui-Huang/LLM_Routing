import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(tour, coordinates):
    visited = set()
    total_cost = 0
    max_distance = 0
    
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        visited.add(city1)
        
        # Calculate the distance between the two cities
        distance = euclidean_distance(coordinates[city1], coordinates[city2])
        total_cost += distance
        max_distance = max(max_distance, distance)
    
    # Ensure the tour starts and ends at depot city (Index 0)
    starts_and_ends_at_depot = tour[0] == 0 and tour[-1] == 0
    # Check every city except the depot is visited exactly once
    tours_all_cities_once = len(visited) == len(coordinates) and all(city in visited for city in range(len(coordinates)))

    # Check the inputs against provided solution
    is_total_cost_correct = math.isclose(total_cost, 478.43, rel_tol=1e-2)
    is_max_distance_correct = math.isclose(max_distance, 80.61, rel_tol=1e-2)
    
    if starts_and_ends_at_depot and tours_all_cities_once and is_total_cost_correct and is_max_distance_correct:
        return "CORRECT"
    else:
        return "FAIL"

# Coordinates of cities
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Provided tour solution
solution_tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]

# Check if the solution is correct
print(verify_tour(solution_tour, coordinates))