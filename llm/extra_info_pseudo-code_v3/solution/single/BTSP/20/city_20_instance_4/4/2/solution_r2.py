import math
import itertools

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def get_all_edges(cities):
    num_cities = len(cities)
    edges = []
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = calculate_distance(cities[i], cities[j])
            edges.append(((i, j), distance))
            edges.append(((j, i), distance))  # undirected edge
    return edges

def find_min_bottleneck_tour(cities):
    edges = get_all_edges(cities)
    edges.sort(key=lambda x: x[1])  # sort by distance
    parent = list(range(len(cities)))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX

    for threshold in range(len(edges)):
        # Make sets for each city
        parent = list(range(len(cities)))
        max_edge_length = edges[threshold][1]
        
        # Create MST-like structure only allowing edges up to current threshold
        for i in range(threshold + 1):
            u, v = edges[i][0]
            union(u, v)
        
        # Check if there is exactly one component
        if len(set(find(i) for i in range(len(cities)))) == 1:
            # Try to make a tour
            tour = [0]
            visited = set(tour)
            while len(tour) < len(cities):
                last_city = tour[-1]
                found = False
                for i in range(len(edges)):
                    u, v = edges[i][0]
                    if u == last_city and v not in visited and edges[i][1] <= max_edge_length:
                        tour.append(v)
                        visited.add(v)
                        found = True
                        break
                if not found:
                    break
            
            if len(tour) == len(cities) and (tour[-1], tour[0]) in edges:
                # Check if can return to start
                tour.append(0)
                max_edge_weight = max(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
                total_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
                return tour, total_cost, max_edge_weight
            
    return None, None, None  # No tour found

# Define the city coordinates
cities = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
          (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
          (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
          (64, 72), (14, 89)]

# Solve the problem
tour, total_cost, max_dist = find_min_bottleneck_tour(cities)

# Print the results
if tour:
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_dist:.2f}")
else:
    print("No valid tour found.")