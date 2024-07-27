import math
import random

# City coordinates provided in the problem statement
city_coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Calculate Euclidean distance between two cities
def distance(i, j):
    x1, y1 = city_coordinates[i]
    x2, y2 = city_coordinates[j]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initial solution: start at the depot, select the first 15 other cities, and return to the depot
initial_cities = [0] + random.sample(range(1, 20), 15) + [0]

# Function to calculate total travel cost of the tour
def total_travel_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Variable Neighborhood Descent (VND) with two neighborhood structures
def vnd(tour):
    improved = True
    while improved:
        current_cost = total_travel_cost(tour)
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i != 0 or j != len(tour) - 1:
                    # Swap cities and check the new cost
                    new_tour = tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    new_cost = total_travel_cost(new_tour)
                    if new_cost < current_cost:
                        tour = new_tour
                        current_cost = new_cost
                        improved = True
                        break
            else:
                continue
            break
        else:
            improved = False
    return tour

# Find the improved tour using VND
improved_tour = vnd(initial_cities)

# Calculate the total cost of the improved tour
tour_cost = total_travel_cost(improved_tour)

# Output the results
print(f"Tour: {improved_tour}")
print(f"Total travel cost: {tour_cost:.2f}")