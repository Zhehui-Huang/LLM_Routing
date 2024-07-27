import math
import random

# Constants and environments given
coordinates = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}
groups = [
    [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Build initial distance matrix
distance_matrix = {}
for i in coordinates:
    distance_matrix[i] = {}
    for j in coordinates:
        distance_matrix[i][j] = euclidean_distance(i, j)

# Initialize a simple tour by picking the first city from each group
def initial_tour():
    tour = [0]  # start at the depot
    for group in groups:
        tour.append(group[0])  # simply pick the first in each group
    tour.append(0)  # return to depot
    return tour

# Calculate the cost of the tour
def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Simulated Annealing to improve the solution
def simulated_annealing(initial_tour):
    current_tour = initial_town_tour
    current_cost = calculate_tour_cost(current_tour)
    T = 10000  # Start temperature
    cooling_rate = 0.99
    min_temperature = 1

    while T > min_temperature:
        # Select a random group index (not the start/end which are both 0)
        group_index = random.randint(1, len(groups) - 1)
        current_city = current_tour[group_index]

        # Select a new city from the same group
        new_city = random.choice(groups[group_index])
        new_tour = current_tour[:]
        new_tour[group_indices[group_index]] = new_city
        new_cost = calculate_tour_cost(new_tour)

        if new_cost < current_cost or random.random() < math.exp(-(new_cost - current_cost) / T):
            current_tour = new_tour
            current_cost = new_cost

        T *= cooling_rate

    return current_tour, current_cost

# Running the approach
initial_town_tour = initial_tour()
final_tour, final_cost = simulated_annealyzing(initial_town_tour)

# Output results
print("Tour:", final_tour)
print("Total travel cost:", final_cost)