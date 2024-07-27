import random
import numpy as np

# Euclidean distance function
def euclidean_distance(a_index, b_index):
    a = coordinates[a_index]
    b = coordinates[b_index]
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Initialize the robots' tours
def initialize_tours(num_robots, nodes):
    tours = [[] for _ in range(num_robots)]
    nodes = sorted(nodes, key=lambda k: euclidean_distance(0, k))
    for i, node in enumerate(nodes):
        tours[i % num_robots].append(node)
    return tours

def calculate_tour_cost(tour):
    cost = euclidean_distance(0, tour[0])  # Start at depot
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i + 1])
    cost += euclidean_distance(tour[-1], 0)  # Return to depot
    return cost

# Shaking function
def shake(tours, k):
    new_tours = [tour[:] for tour in tours]
    num_tours = len(new_tours)
    for _ in range(k):
        t1, t2 = random.sample(range(num_tours), 2)
        if new_tours[t1] and new_tours[t2]:
            node_idx1 = random.randint(0, len(new_tours[t1]) - 1)
            node = new_tours[t1].pop(node_idx1)
            node_idx2 = random.randint(0, len(new_tours[t2]))
            new_tours[t2].insert(node_idx2, node)
    return new_tours

# Sequential Variable Neighborhood Descent (VND)
def improve_tour(tour):
    improved = True
    while improved:
        improved = False
        for i in range(len(tour)):
            for j in range(i + 2, len(tour) + 1):
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_tour_cost(new_tour) < calculate_tour_cost(tour):
                    tour = new_tour
                    improved = True
        break
    return tour

def seq_vnd(tours):
    new_tours = [improve_tour(tour) for tour in tours]
    return new_tours

# Main GVNS procedure
def gvns(max_iterations, shaking_strength):
    cities = list(range(1, num_cities))  # Excluding depot
    tours = initialize_tours(num_robots, cities)
    best_tours = tours
    best_max_cost = max([calculate_tour_cost(tour) for tour in tours])

    for _ in range(max_iterations):
        neighbors = shake(tours, shaking_strength)
        neighbors = seq_vnd(neighbors)
        max_cost = max([calculate_tour_cost(tour) for tour in neighbors])
        if max_cost < best_max_cost:
            best_tours = neighbors
            best_max_cost = max_cost
    return best_tours, best_max_cost

# Running the GVNS
best_tours, best_max_cost = gvns(100, 3)

# Output results
for i, tour in enumerate(best_tours):
    full_tour = [0] + tour + [0]
    tour_cost = calculate_tour_cost(tour)
    print(f"Robot {i} Tour: {full_tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Maximum Travel Cost: {best_max_cost}")