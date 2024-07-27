import math

# Coordinates for each city
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate distance matrix and sorted unique distances
dist_matrix = [[0]*10 for _ in range(10)]
all_distances = set()

for i in range(10):
    for j in range(i + 1, 10):
        d = distance(cities[i], cities[j])
        dist_matrix[i][j] = d
        dist_matrix[j][i] = d
        all_distances.add(d)

sorted_distances = sorted(all_distances)

# Check if Hamiltonian cycle is possible for given max distance using DFS
def can_form_cycle(max_distance):
    visited = [False]*10
    path = []

    def dfs(node, depth):
        visited[node] = True
        path.append(node)
        
        if depth == 9:
            if dist_matrix[node][0] <= max_distance:  # can return to start?
                return True
            else:
                path.pop()
                visited[node] = False
                return False
        
        for next_node in range(1, 10):
            if not visited[next_node] and dist_matrix[node][next_node] <= max_distance:
                if dfs(next_node, depth + 1):
                    return True
        
        visited[node] = False
        path.pop()
        return False
    
    # Try to find Hamiltonian cycle starting from 0
    if dfs(0, 0):
        path.append(0)  # close the cycle
        return True, path
    return False, []

# Binary search over the sorted distances
left = 0
right = len(sorted_distances) - 1
best_path = []

while left <= right:
    mid = (left + right) // 2
    feasible, path = can_form_cycle(sorted_distances[mid])

    if feasible:
        best_path = path
        right = mid - 1
    else:
        left = mid + 1

if best_path:
    # Calculate the total and maximum distances of the best tour
    tour_distances = [dist_matrix[best_path[i]][best_path[i+1]] for i in range(len(best_path)-1)]
    total_travel_cost = sum(tour_distances)
    maximum_distance = max(tour_distances)

    print(f"Tour: {best_path}")
    print(f"Total travel cost: {total_travel_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {maximum_distance:.2f}")
else:
    print("Failed to find a solution.")