import math
from typing import List, Tuple

# City coordinates as provided in the problem statement
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance
def distance(city1: Tuple, city2: Tuple) -> float:
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a distance matrix
def create_distance_matrix() -> List[List[float]]:
    n = len(coordinates)
    dist_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dist = distance(coordinates[i], coordinates[j])
            dist_matrix[i][j] = dist_matrix[j][i] = dist
    return dist_matrix

# Heuristic for partitioning cities to the available robots
def partition_cities(num_robots: int, cities: List[int]) -> List[List[int]]:
    # Simple partitioning: round-robin assignment
    tours = [[] for _ in range(num_robots)]
    for index, city in enumerate(cities):
        tours[index % num_robots].append(city)
    return tours

# Solve the TSP for a single robot given its city subset
def solve_tsp_cities(cities: List[int], dist_matrix: List[List[float]]) -> Tuple[List[int], float]:
    from itertools import permutations
    min_route = []
    min_cost = float('inf')

    cities = [0] + cities  # Include depot as starting point
    all_permutations = permutations(cities[1:])
    
    for perm in all_permutations:
        current_route = [0] + list(perm) + [0]
        cost = sum(dist_matrix[current_route[i]][current_route[i+1]] for i in range(len(current_route)-1))
        
        if cost < min_cost:
            min_route = current_route
            min_cost = cost
                
    return min_route, min_cost

# Main function to compute the routes
def compute_routes(num_robots: int=2) -> None:
    dist_matrix = create_distance_matrix()
    non_depot_cities = list(range(1, len(coordinates)))
    tours = partition_cities(num_robots, non_depot_cities)
    
    max_travel_cost = 0
    results = []
    
    for robot_id, cities in enumerate(tours):
        tour, cost = solve_tsp_cities(cities, dist_matrix)
        results.append((tour, cost))
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {cost}")
        max_travel_cost = max(max_travel_cost, cost)
    
    print(f"Maximum Travel Cost: {max_travel_cost}")

# Execute
compute_routes()