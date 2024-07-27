import numpy as np

# Step 1: City coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Step 2: Compute Euclidean distances between cities
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')  # Avoid self-loop

# Step 3: Nearest Neighbor Heuristic
def nearest_neighbor(start=0):
    tour = [start]
    unvisited = set(range(num_cities)) - {start}

    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: distance_matrix[last][x])
        tour.append(next_city)
        unvisited.remove(next_city)

    tour.append(start)  # Return to the depot
    return tour

# Step 4: 2-opt optimization
def two_opt(tour):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue
                if distance_matrix[tour[i - 1]][tour[i]] + distance_matrix[tour[j]][tour[j + 1]] > distance_matrix[tour[i - 1]][tour[j]] + distance_matrix[tour[i]][tour[j + 1]]:
                    tour[i:j + 1] = tour[i:j + 1][::-1]
                    improvement = True
    return tour

# Find initial tour and optimize with 2-opt
initial_tour = nearest_neighbor()
optimized_tour = two_opt(initial_tour)
total_distance = sum(distance_matrix[optimized_tour[k]][optimized_tour[k + 1]] for k in range(len(optimized_tour) - 1))

# Output the tour and its total cost
print("Tour:", optimized_tour)
print("Total travel cost:", total_distance)