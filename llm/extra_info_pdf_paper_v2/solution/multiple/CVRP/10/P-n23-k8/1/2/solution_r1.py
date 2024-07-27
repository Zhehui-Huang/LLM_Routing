import math
from itertools import combinations
import random

# City coordinates and demand
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), 
    (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Robot capacity and number
num_robots = 8
robot_capacity = 40

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)

# Calculate savings
def calculate_savings():
    n = len(coordinates)
    savings = []
    for i, j in combinations(range(1, n), 2):
        cost_to_i = euclidean_distance(coordinates[0], coordinates[i])
        cost_to_j = euclidean_distance(coordinates[0], coordinates[j])
        cost_ij = euclidean_distance(coordinates[i], coordinates[j])
        savings.append(((i, j), cost_to_i + cost_to_j - cost_ij))
    savings.sort(key=lambda x: x[1], reverse=True)
    return savings

# Clarke-Wright Savings Algorithm with enhancements
def clarke_wright():
    routes = {i: [0, i, 0] for i in range(1, len(coordinates))}
    savings = calculate_savings()
    for (i, j), saving in savings:
        route_i = next((r for r in routes.values() if r[-2] == i), None)
        route_j = next((r for r in routes.values() if r[1] == j), None)
        if route_i and route_j and route_i != route_j:
            if sum(demands[r] for r in route_i[1:-1]) + sum(demands[r] for r in route_j[1:-1]) <= robot_capacity:
                # Merge routes
                route_i[-1:] = route_j[1:-1] + [0]
                routes.pop(route_j[0])
    
    return list(routes.values())

# Main function to run the entire program
def main():
    routes = clarke_wright()
    total_cost = 0
    if not routes:
        print("No feasible routes found.")
        return
    
    for robot_id, route in enumerate(routes):
        tour_cost = sum(
            euclidean_distance(coordinates[route[i]], coordinates[route[i + 1]])
            for i in range(len(route) - 1)
        )
        total_cost += tour_cost
        print(f"Robot {robot_id} Tour: {route}")
        print(f"Robot {robot_id} Total Travel Cost: {tour_cost:.2f}")
    
    print(f"Overall Total Travel Cost: {total_cost:.2f}")

# Execute the main function
main()