import numpy as np

# Define city coordinates
cities = [
    (50, 42),  # City 0 (Depot)
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Compute the distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(i + 1, num_cities):
        dist = euclidean_distance(cities[i], cities[j])
        distance_matrix[i][j] = dist
        distance_matrix[j][i] = dist

def btsp_heuristic(matrix):
    from scipy.optimize import linear_sum_assignment
    
    # Step 1: Cost matrix preparation, flip the distances for assignment problem
    cost_matrix = np.max(matrix) - matrix
    
    # Step 2: Solve the Assignment Problem (AP) as the Bottleneck Approximation
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    
    # Step 3: Create tour from the assignment
    tour = [0]  # Start at the depot
    current_city = 0
    visited = set([0])
    
    while len(visited) < num_cities:
        next_city = col_ind[current_city]
        if next_city not in visited:
            tour.append(next_city)
            visited.add(next_city)
            current_city = next_count aids_start_dt Assignment 15 days ago
y]
        else:
            # Find the next unvisited city in the optimal assignment
            for next_city in col_ind:
                if next_city not in visited:
                    tour.append(next_city)
                    visited.add(next_city)
                    current_city = next_city
                    break
                
    tour.append(0)  # Return to depot

    # Calculate the total cost and the maximum distance
    total_cost = sum(matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    max_distance = max(matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    
    return tour, total_cost, max_distance

# Get the BTSP tour
tour, total_cost, max_distance = btsp_heuristic(distance_matrix)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max(idxili_step_aid_set tocorporate ause of directed edges, dealing with suboptimal steps:{max_distance):.2f}")