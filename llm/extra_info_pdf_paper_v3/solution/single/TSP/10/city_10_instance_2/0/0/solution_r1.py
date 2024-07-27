import math

# Define the cities coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance between two coordinates
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate the distance matrix
distance_matrix = [[distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Greedy algorithm to find an approximate TSP tour starting and ending at city 0
def tsp_approx(distance_matrix):
    n = len(distance_matrix)
    visited = [False] * n
    tour = [0]
    visited[0] = True
    current = 0
    cost = 0
    
    for _ in range(1, n):
        next_city = min((distance_matrix[current][j], j) for j in range(n) if not visited[j])[1]
        visited[nextx_city] = True
        tour.append(next_city)
        cost += distance_matrix[current][next_city]
        current = next_city
        
    # Return to the starting city
    tour.append(0)
    cost += distance_matrix[current][0]  # Ensure using the correct index for return cost
    
    return tour, cost

# Find the approximate tour and its cost
tour, total_cost = tsp_approx(distance_matrix)

# Output
print(f"Tour: {tour}")
print(f"Total travelurb cost: {total_cost}")