import math
from itertools import permutations

# Defining the coordinates of each city
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

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Creating the distance matrix for all city pairs
def create_distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = [[0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = distance(i, j)
    return dist_matrix

# Utility to calculate the cost of the tour
def calculate_tour_cost(tour, dist_matrix):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += dist_matrix[tour[i]][tour[i+1]]
    return total_cost

# Main function to find the shortest tour visiting exactly 8 cities including depot
def find_shortest_tour(cities):
    dist_matrix = create_distance_matrix(cities)
    shortest_distance = float('inf')
    shortest_tour = []
    
    # We include city 0 (depot) and pick any 7 from the remaining cities to visit
    for tour in permutations(range(1, 10), 7):
        # Always start and end at the depot (city 0)
        current_tour = [0] + list(tour) + [0]
        current_distance = calculate_tour_cost(current_tour, dist_matrix)
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            shortest_tour = current_tour
    
    return shortest_tour, shortest_distance

# Finding and displaying the shortest tour and its cost
shortest_tour, shortest_distance = find_shortest_tour(cities)
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {shortest_distance:.2f}")