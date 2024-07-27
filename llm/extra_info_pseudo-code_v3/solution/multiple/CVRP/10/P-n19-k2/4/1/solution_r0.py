import numpy as np
from math import sqrt
from random import choice, randint, shuffle
from itertools import permutations

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_distance_matrix(coords):
    n = len(coords)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            D[i, j] = D[j, i] = euclidean_details{(p)}istance(coords[i], coords[j])
    return D

# City coordinates
coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demands
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Distance matrix
D = create_distance_matrix(coords)

n_vehicles = 2
vehicle_capacity = 160
num_nodes = len(coords)

def valid_tour(tour):
    current_load = 0
    for i in tour:
        current_load += demands[i]
        if current_load > vehicle_capacity:
            return False
    return True

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += D[tour[i], tour[i+1]]
    return cost

# Initial feasible tour generation
def generate_initial_solution():
    remaining_nodes = list(range(1, num_nodes))
    shuffle(remaining_nodes)
    tours = [[] for _ in range(n_vehicles)]
    current_loads = [0] * n_vehicles
    
    for node in remaining_nodes:
        placed = False
        for idx in range(n_vehicles):
            if current_loads[idx] + demands[node] <= vehicle_capacity:
                if not tours[idx] or valid_tour(tours[idx] + [node]):
                    tours[idx].append(node)
                    current_loads[idx] += demands[node]
                    placed = True
                    break
        if not placed:
            for idx in range(n_vehicles):
                if valid_tour(tours[idx] + [node]):
                    tours[idx].append(node)
                    current_loads[idx] += demands[node]
                    break
                
    # Close the loops
    for tour in tours:
        tour.insert(0, 0)
        tour.append(0)
    
    return tours

tours = generate_initial_solution()
total_travel_cost = sum(calculate_tour_cost(tour) for tour in tours)

# Result-printing
print("Resulting tours and costs:")
overall_cost = 0
i = 0
for tour in tours:
    cost = calculate_tour_cost(tour)
    overall_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")
    i += 1

print(f"Overall Total Travel Cost: {overall_cost:.2f}")