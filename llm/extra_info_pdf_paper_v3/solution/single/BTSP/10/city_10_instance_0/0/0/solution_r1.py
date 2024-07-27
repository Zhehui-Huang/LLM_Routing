import math
import random

# Coordinates for each city including the depot
coordinates = [
    (50, 42), (41, 1), (18, 46), (40, 98), (51, 69),
    (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)
]

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a distance matrix
n = len(coordinates)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(coordinates[i], coordinates[j])

def total_cost(tour):
    """ Calculate the total cost of the tour. """
    return sum(distances[tour[i]][tour[i - 1]] for i in range(1, len(tour)))

def max_leg(tour):
    """ Calculate the maximum distance between consecutive cities in the tour. """
    return max(distances[tour[i]][tour[i - 1]] for i in range(1, len(tour)))

def simulated_annealing():
    """ Perform simulated annealing to find an optimal solution. """
    # Initialize with a random tour
    current_tour = list(range(n))
    random.shuffle(current_tour)
    current_tour.append(current_tour[0])  # make it a round trip
  
    current_max_leg = max_leg(current_tour)
    current_cost = total_cost(current_tour)
    temp = 1000
    temp_min = 1
    alpha = 0.99  # cooling rate

    while temp > temp_min:
        i, j = sorted(random.sample(range(1, n), 2))
        new_tour = current_tour[:]
        new_tour[i:j + 1] = reversed(new_tour[i:j + 1])  # reverse segment of the tour
        new_max_leg = max_leg(new_tour)
        new_cost = total_cost(new_tour)
        
        if new_max_leg < current_max_leg or random.random() < math.exp((current_max_leg - new_max_leg) / temp):
            current_tail, current_max_leg, current_cost = new_tour, new_max_leg, new_cost
        
        temp *= alpha

    return current_tour, current_cost, current_max_leg

# Run the optimization
tour, total_travel_cost, max_distance = simulated_annealing()

# Outputs
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance)