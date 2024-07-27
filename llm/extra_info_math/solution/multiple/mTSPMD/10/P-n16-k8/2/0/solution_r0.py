import numpy as np

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots, each starting and ending at a depot
robots = {i: i for i in range(8)}

# Distance function - Euclidean
def euclidean_distance(pt1, pt2):
    return np.linalg.norm(np.array(pt1) - np.array(pt2))

# Create distance matrix
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            dist_matrix[i, j] = euclidean_distance(cities[i], cities[j])
        else:
            dist_matrix[i, j] = float('inf')  # Infinite cost to itself to avoid self-loop

# Function to find the minimum cost tour for each robot starting from its depot
def find_tours(robots, dist_matrix):
    tours = {}
    total_cost = 0
    for robot_id, start_depot in robots.items():
        visited = set()
        current_city = start_depot
        tour = [current_city]
        tour_cost = 0
        visited.add(current_city)
        
        # Construct the tour using a greedy approach
        while len(visited) < num_cities:
            next_city = np.argmin(dist_matrix[current_city])
            if next_city in visited:
                dist_matrix[current_city, next_city] = float('inf')  # Temporarily set to infinity
                continue
            visited.add(next_city)
            tour_cost += dist_matrix[current_city, next_city]
            tour.append(next_city)
            current_city = next_city
        
        # Return to the starting depot
        tour_cost += dist_matrix[current_city, start_depot]
        tour.append(start_depot)
        
        tours[robot_id] = (tour, tour_cost)
        total_cost += tour_cost
    
    return tours, total_cost

# Calculate tours
tours, overall_cost = find_tours(robots, dist_matrix)

# Output the results
for robot_id, (tour, cost) in tours.items():
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {round(cost, 2)}")

print(f"Overall Total Travel Cost: {round(overall_cost, 2)}")