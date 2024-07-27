import itertools
import math

# Calculate the Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# The provided city locations
cities = [
    (16, 90),  # Depot city
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Sort edges by Euclidean distance
def create_sorted_edges(cities):
    edges = []
    num_cities = len(cities)
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist = euclidean_distance(cities[i], cities[j])
                edges.append((dist, i, j))
    edges.sort()
    return edges

# Check if all nodes are part of the connected component
def can_form_tour(visits, num_cities):
    return all(visits) and len(set(visits)) == 1

# Main function to find the Bottleneck TSP tour
def find_btsp_tour(cities):
    edges = create_sorted_edges(cities)
    num_cities = len(cities)

    for threshold, _, _ in edges:
        visits = [0] * num_cities
        graph = [[] for _ in range(num_cities)]

        # Build the graph up to the current bottleneck threshold
        for dist, u, v in edges:
            if dist <= threshold:
                graph[u].append(v)
                graph[v].append(u)

        # Try to find a hamiltonian cycle starting and ending at the depot
        tour = [0]
        visited = [False] * num_cities
        visited[0] = True
        current = 0

        for _ in range(1, num_cities):
            next_city = None
            for city in graph[current]:
                if not visited[city]:
                    next_city = city
                    break
            if next_city is None:
                break
            tour.append(next_city)
            visited[next_city] = True
            current = next removal
        if len(tour) == num_cities:
            tour.append(0) # Complete the tour by returning to the depot
            if can_form_tour(visited, num_cities):
                total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
                max_dist = max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
                return tour, total_cost, max_dist
    return None

# Execute the function and print the results
result = find_btsp_tour(cities)
if result:
    tour, total_cost, max_dist = result
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_dist)
else:
    print("No feasible tour was found.")