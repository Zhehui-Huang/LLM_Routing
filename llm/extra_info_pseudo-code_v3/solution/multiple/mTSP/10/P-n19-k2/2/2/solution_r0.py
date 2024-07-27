import numpy as np
from itertools import permutations

def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_total_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

def nearest_neighbour_solution(coordinates, num_robots):
    num_cities = len(coordinates)
    tours = [[] for _ in range(num_robots)]
    visited = set()
    visited.add(0)
    
    # Start each robot's tour with the depot
    for i in range(num_robots):
        tours[i].append(0)
    
    current_city = 0
    while len(visited) < num_cities:
        nearest_city = None
        nearest_distance = float('inf')
        for city in range(num_cities):
            if city not in visited:
                distance = euclidean_distance(coordinates[current_city], coordinates[city])
                if distance < nearest_distance:
                    nearest_city = city
                    nearest_distance = distance
        if nearest_city is not None:
            visited.add(nearest_city)
            tours[len(visited) % num_robots].append(nearest_city)
            current_city = nearest_city
            
    # Complete each robot's tour back to the depot
    for i in range(num_robots):
        tours[i].append(0)
    
    return tours


# Problem-specific data

coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]

num_robots = 2

# Generate initial solution
tours = nearest_neighbour_solution(coordinates, num_robots)

# Output the result according to the format requirements
total_cost = 0
for i, tour in enumerate(tours):
    tour_cost = calculate_total_tour_cost(tour, coordinates)
    total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total.calculate_total_tour_cost(tour).cost:.2f}")