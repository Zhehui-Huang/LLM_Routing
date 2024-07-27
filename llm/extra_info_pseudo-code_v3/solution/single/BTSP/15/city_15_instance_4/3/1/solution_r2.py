import math

# Coordinates of the cities
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Generate all edges with computed distances
edges = {(i, j): calculate_distance(cities[i], cities[j]) for i in range(len(cities)) for j in range(len(cities)) if i != j}

# Sort edges by distance
sorted_edges_by_distance = sorted(edges.items(), key=lambda item: item[1])

def find_hamiltonian_cycle(cutoff_distance):
    # Create adjacency matrix under the cutoff distance
    adjacency_list = {i: [] for i in range(len(cities))}
    for (i, j), dist in edges.items():
        if dist <= cutoff_distance:
            adjacency_list[i].append(j)
            adjacency_list[j].append(i)

    # Perform DFS to find cycle
    def dfs(current, path, visited):
        if len(visited) == len(cities):
            if current in adjacency_list[path[0]]:
                return path + [path[0]]  # return to starting node
            return None
        for next_city in adjacency_list[current]:
            if next_city not in visited:
                visited.add(next_city)
                result = dfs(next_city, path + [next_city], visited)
                if result:
                    return result
                visited.remove(next_city)
        return None

    # Start DFS from city 0
    return dfs(0, [0], {0})

def minimize_max_distance_btsp():
    left, right = 0, max(edges.values())
    best_cycle = None

    while left <= right:
        mid = (left + right) / 2
        cycle = find_hamiltonian_cycle(mid)
        if cycle:
            best_cycle = cycle
            right = mid - 0.01
        else:
            left = mid + 0.01

    return best_cycle

# Find the BTSP solution
best_tour = minimize_max_distance_btsp()

if best_tour:
    max_distance = max(calculate_distance(cities[best_tour[i]], cities[best_tour[i+1]]) for i in range(len(best_tour) - 1))
    total_distance = sum(calculate_distance(cities[best_tour[i]], cities[best_tour[i+1]]) for i in range(len(best_tour) - 1))
    print("Tour:", best_tour)
    print("Total travel cost:", round(total_distance, 2))
    print("Maximum distance between consecutive cities:", round(max_distance, 2))
else:
    print("No Hamiltonian cycle could be found that satisfies the condition.")