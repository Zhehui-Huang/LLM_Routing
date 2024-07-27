import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def find_tour(cities):
    N = len(cities)
    visited = [False]*N
    tour = [0]  # start at the depot, index 0
    visited[0] = True
    current_city = 0
    total_cost = 0
    max_distance = 0
    
    while len(tour) < N:
        # Find the nearest unvisited city
        next_city = None
        min_dist = float('inf')
        for i in range(1, N):
            if not visited[i]:
                dist = euclidean_distance(cities[current_city], cities[i])
                if dist < min_dist:
                    min_dist = dist
                    next_city = i
        
        # Append the selected city to the tour
        if next_city is not None:
            tour.append(next_city)
            visited[next_city] = True
            max_distance = max(max_distance, min_dist)
            total_cost += min_dist
            current_city = next_city
    
    # Return to the start city (depot)
    final_leg = euclidean_distance(cities[current_city], cities[0])
    tour.append(0)
    total_cost += final_leg
    max_distance = max(max_distance, final_leg)
    
    return tour, total_cost, max_distance

# Use the function
tour, cost, max_dist = find_tour(cities)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")