from math import sqrt
from collections import defaultdict

# Data structures
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
num_robots = 8
capacity = 35

# Function to compute Euclidean distance
def euclidean_distance(i, j):
    return sqrt((coordinates[i][0]-coordinates[j][0])**2 + (coordinates[i][1]-coordinates[j][1])**2)

# Assign cities to robots greedily based on demands and capacities
def cluster_cities():
    assignments = []
    for i in range(num_robots):
        assignments.append([])
    
    used_capacity = [0] * num_robots
    city_assignment = [False] * len(coordinates)
    city_assignment[0] = True  # Depot city
        
    for r in range(num_robots):
        current_city = 0
        while True:
            next_city = None
            min_distance = float('inf')

            for city in range(1, len(coordinates)):
                if not city_assignment[city] and used_capacity[r] + demands[city] <= capacity:
                    distance = euclidean_distance(current_city, city)
                    if distance < min_distance:
                        min_distance = distance
                        next_city = city
            
            if next_city is None:
                break

            assignments[r].append(next_city)
            used_capacity[r] += demands[next_city]
            city_assignment[next_city] = True
            current_city = next_city

    return assignments

# Generate tours using nearest neighbor heuristic
def generate_tours(assignments):
    tours = []
    costs = []
    
    for assigned in assignments:
        tour = [0]  # Start at depot
        total_cost = 0
        current_city = 0
        
        while assigned:
            next_city = min(assigned, key=lambda x: euclidean_distance(current_city, x))
            total_cost += euclidean_distance(current_city, next_city)
            tour.append(next_city)
            current_city = next_city
            assigned.remove(next_city)
        
        total_cost += euclidean_distance(current_city, 0)  # Return to depot
        tour.append(0)
        tours.append(tour)
        costs.append(total_cost)
    
    return tours, costs

# Main function to solve the CVRP
def solve_cvrp():
    assignments = cluster_cities()
    tours, costs = generate_tours(assignments)
    total_travel_cost = sum(costs)
    
    for i in range(len(tours)):
        print(f"Robot {i} Tour: {tours[i]}")
        print(f"Robot {i} Total Travel Cost: {costs[i]:.2f}")
    
    print(f"Overall Total Travel Cost: {total_travel_cost:.2f}")
    
solve_cvrp()