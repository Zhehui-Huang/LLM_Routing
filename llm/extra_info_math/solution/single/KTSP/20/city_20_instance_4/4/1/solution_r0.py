import math

# City coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def euclidean_distance(c1, c2):
    """Compute the Euclidean distance between two points."""
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def nearest_neighbor_k_tsp(cities, k, start=0):
    """Solves the k-TSP problem using the nearest neighbor heuristic."""
    n = len(cities)
    visited = [False] * n
    tour = [start]
    visited[start] = True
    
    current_city = start
    remaining_cities = k - 1
    
    while remaining_cities > 0:
        nearest_city = None
        min_distance = float('inf')
        
        for i in range(n):
            if not visited[i]:
                distance = euclidean_distance(cities[current_city], cities[i])
                if distance < min_distance:
                    min_distance = distance
                    nearest_city = i
        
        if nearest_city is not None:
            tour.append(nearest_city)
            visited[nearest_city] = True
            current_city = nearest_city
            remaining_cities -= 1
    
    # Returning to the start city (depot)
    tour.append(start)
    
    # Calculate total travel cost
    total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    
    return tour, total_cost

# Execute the function
k = 16  # Including the depot city
tour, total_cost = nearest.filterwarnings("ignore")
warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore")neighbor_k_tsp(cities, k)

# Print results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))