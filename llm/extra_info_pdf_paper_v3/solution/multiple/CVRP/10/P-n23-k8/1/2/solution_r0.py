import math
from typing import List, Tuple

# Given city coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]
number_of_robots = 8
robot_capacity = 40

# Function to calculate Euclidean distance between two points
def euclidean_distance(a: Tuple[int, int], b: Tuple[int, int]) -> float:
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

# Function to find the nearest city which hasn't been completely served
def find_nearest_city(current_city: int, visited: List[bool], demands_left: List[int]) -> int:
    min_distance = float('inf')
    nearest_city = -1
    for i, _ in enumerate(coordinates):
        if not visited[i] and demands_left[i] > 0:
            distance = euclidean_distance(coordinates[current_city], coordinates[i])
            if distance < min_distance:
                min_distance = distance
                nearest_city = i
    return nearest_city

# Solve CVRP using a simple greedy heuristic
def solve_cvrp():
    tours = [[] for _ in range(number_of_robots)]
    costs = [0 for _ in range(number_of_robots)]
    demands_left = demands.copy()
    visited = [False] * len(coordinates)
    
    for robot in range(number_of_robots):
        current_city = 0
        tour = [current_city]
        load = 0
        
        while True:
            next_city = find_nearest_city(current_city, visited, demands_left)
            if next_city == -1 or load + demands[next_city] > robot_capacity:
                tour.append(0)  # Return to depot
                costs[robot] += euclidean_distance(coordinates[current_city], coordinates[0])
                break
            
            visited[next_city] = True
            tour.append(next_city)
            costs[robot] += euclidean_distance(coordinates[current_city], coordinates[next_city])
            demands_left[next_city] = 0
            load += demands[next_city]
            current_city = next_city
        
        tours[robot] = tour
    
    # Output the results
    total_cost = sum(costs)
    for i, tour in enumerate(tours):
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {costs[i]}")
    print(f"Overall Total Travel Cost: {total_cost}")

solve_cvrp()