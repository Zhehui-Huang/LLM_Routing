import math

# Define the cities coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

# Function to calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate distances matrix
n = len(cities)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Heuristic: Nearest Neighbour Algorithm to provide an initial solution
def nearest_neighbour_solution(start_city):
    unvisited = list(range(n))
    tour = [start_city]
    current_city = start_city
    unvisited.remove(current_city)

    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # returning to the depot
    return tour

# Get the initial tour
initial_tour = nearest_neighbour_solution(0)

# Calculate the tour cost and max distance between consecutive cities
def calculate_metrics(tour):
    total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    max_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return total_cost, max_distance

total_cost, max_distance = calculate_metrics(initial_tour)

print(f"Tour: {initial_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")