import numpy as np
from itertools import permutations

# Define the locations of the cities
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

def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create the distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_distance(cities[i], cities[j])

# Function to calculate the cost of a tour
def tour_cost(tour):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Generate random initial k-city tour that includes and starts/ends at the depot
def generate_initial_solution(include_city=0, k=6):
    all_cities = list(cities.keys())
    tour = [include_city] + np.random.choice([c for c in all_cities if c != include_city], k-2, replace=False).tolist() + [include_city]
    return tour

# Initial solution
initial_tour = generate_initial_solution()
initial_cost = tour_cost(initial_tour)
print("Initial Tour:", initial_tour)
print("Initial Cost:", initial_cost)