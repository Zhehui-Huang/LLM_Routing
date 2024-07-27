import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Cities coordinates {index: (x, y)}
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate all distances
edges = {}
for i in cities:
    for j in cities:
        if i != j:
            edges[(i, j)] = euclideanativa_distance(cities[i], cities[j])

# Function to calculate total distance and max distance between consec. cities
def calculate_tour_costs(tour):
    total_distance = 0
    max_distance = 0
    path = []
    for i in range(len(tour) - 1):
        dist = edges[(tour[i], tour[i+1])]
        path.append((tour[i], tour[i+1]))
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    return total_distance, max_distance, path

def find_bottleneck_tours():
    # Order edges by distance
    sorted_edges_by_weight = sorted(edges.items(), key=lambda item: item[1])

    # Perform Bottleneck TSP approximation attempt for each incrementing max edge weight
    best_tour = None
    best_max_distance = float('inf')
    best_total_cost = float('inf')

    for edge_index, (edge, weight) in enumerate(sorted_edges_by_weight):
        # Construct bottleneck graph with edges equal or less than current edge's weight
        subgraph_edges = [sorted_edges_by_weight[i][0] for i in range(edge_index + 1)]
        if find_hamiltonian_path_via_per(permutations(range(10)), subgraph_edges):
            total_cost, max_dist, path_detail = calculate_tour_costs([0]+list(best_hamiltonian_path)+[0])
            if max_dist < best_max_distance:
                best_tour = [0] + list(best_hamiltonian_path) + [0]
                best_max_distance = max_dist
                best_total_cost = total_cost
                break  # since we found a more optimal path, we terminate early

    return best_tour, best_total_cost, best_max_distance

def find_hamiltonian_path_via_per(permutations_of_cities, usable_edges):
    global best_hamiltonian_path
    for perm in permutations_of_cities:
        if perm[0] == 0 and all((perm[i], perm[i+1]) in usable_edges or (perm[i+1], perm[i]) in usable_edges for i in range(len(perm) - 1)):
            best_hamiltonian_path = perm
            return True
    return False

# Compute and print the best tour following Bottleneck TSP algorithmic approach
tour, total_cost, max_distance = find_bottleneck_tours()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")