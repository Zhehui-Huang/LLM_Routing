import math

# Cities coordinates
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

# Calculate Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a distance matrix
n = len(cities)
dist_matrix = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = distance(cities[i], cities[j])
        else:
            dist_matrix[i][j] = float('inf')

# Helper function to calculate total tour cost
def calculate_tour_cost(tour, dist_matrix):
    total_cost = 0
    for k in range(1, len(tour)):
        total_cost += dist_matrix[tour[k-1]][tour[k]]
    total_cost += dist_matrix[tour[-1]][tour[0]]  # Return to start city
    return total_cost

# 2-opt Swap Function
def two_opt(route, distance_matrix):
    best = route[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route)-2):
            for j in range(i+1, len(route)):
                if j - i == 1:
                    continue  # Changes nothing, skip
                new_route = route[:]
                new_route[i:j] = route[j-1:i-1:-1]  # This is the 2-optSwap
                if calculate_tour_cost(new_route, distance_matrix) < calculate_tour_cost(best, distance_matrix):
                    best = new_route[:]
                    improved = True
    return best

# Initial tour
tour = list(cities.keys())

# Apply 2-opt algorithm
optimal_tour = two_opt(tour, dist_matrix)
optimal_tour.append(optimal_tour[0]) # closing the tour by returning to the starting city

# Calculate the cost of the optimal tour
total_cost = calculate_tour_cost(optimal_tour, dist_matrix)

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")